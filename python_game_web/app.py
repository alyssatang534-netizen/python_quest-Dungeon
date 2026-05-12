"""Flask web version for Python Quest: The Coding Dungeon."""

import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

from data_manager import DataManager
from models import Player
from python_questions import get_levels
from user_auth import UserAuth

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "python-quest-learning-game-secret")

data_manager = DataManager()
auth = UserAuth(data_manager)
levels = get_levels()


def get_current_player():
    """Load the logged-in player's latest progress from progress.json."""
    username = session.get("username")
    if not username:
        flash("Your session has expired or you are not logged in.", "error")
        return None

    progress = data_manager.load_progress()
    if username not in progress:
        progress[username] = Player(username).to_dict()
        data_manager.save_progress(progress)
    return Player.from_dict(progress[username])


def save_player(player):
    """Save one player's progress back to progress.json."""
    progress = data_manager.load_progress()
    progress[player.username] = player.to_dict()
    data_manager.save_progress(progress)


def find_level(level_number):
    """Find a level object by number."""
    for level in levels:
        if level.level_number == level_number:
            return level
    return None


def progress_percent(player):
    """Return a simple completion percentage for progress bars."""
    if not levels:
        return 0
    return int((len(player.unlocked_levels) / len(levels)) * 100)


def login_required_page(template_name, **context):
    """Small helper to protect pages that need a logged-in user."""
    player = get_current_player()
    if player is None:
        return redirect(url_for("login"))
    return render_template(
        template_name,
        player=player,
        levels=levels,
        progress_percent=progress_percent(player),
        **context,
    )


@app.route("/")
def index():
    """Landing page."""
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Create a new user account."""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        success, message = auth.register_user(username, password)
        flash(message, "success" if success else "error")
        if success:
            return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in an existing user."""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        player, message = auth.login_user(username, password)
        flash(message, "success" if player else "error")
        if player:
            session["username"] = player.username
            return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    """Player dashboard."""
    return login_required_page("dashboard.html")


@app.route("/levels")
def level_selection():
    """Show locked and unlocked levels."""
    return login_required_page("levels.html")


@app.route("/level/<int:level_number>/question/<int:question_number>", methods=["GET", "POST"])
def question(level_number, question_number):
    """Show one question and check the submitted answer."""
    player = get_current_player()
    if player is None:
        return redirect(url_for("login"))

    if level_number not in player.unlocked_levels:
        flash("That level is locked. Complete earlier levels first.", "error")
        return redirect(url_for("level_selection"))

    level = find_level(level_number)
    if level is None:
        flash("That level could not be found.", "error")
        return redirect(url_for("level_selection"))

    if question_number < 1 or question_number > len(level.questions):
        flash("That question could not be found.", "error")
        return redirect(url_for("level_selection"))

    question_item = level.questions[question_number - 1]

    if request.method == "POST":
        selected_answer = request.form.get("answer", "").upper()
        if selected_answer not in question_item.options:
            flash("Please choose A, B, C, or D before submitting.", "error")
            return redirect(url_for("question", level_number=level_number, question_number=question_number))

        correct = selected_answer == question_item.correct_answer
        if correct:
            player.add_score(10)

        session["last_answer"] = {
            "level_number": level_number,
            "question_number": question_number,
            "selected_answer": selected_answer,
            "correct_answer": question_item.correct_answer,
            "correct": correct,
            "explanation": question_item.explanation,
            "question_text": question_item.text,
            "topic": question_item.topic,
        }

        session["level_correct_count"] = session.get("level_correct_count", 0) + (1 if correct else 0)
        save_player(player)
        return redirect(url_for("feedback"))

    if question_number == 1:
        session["level_correct_count"] = 0

    return render_template(
        "question.html",
        player=player,
        level=level,
        question=question_item,
        question_number=question_number,
        total_questions=len(level.questions),
        progress_percent=progress_percent(player),
    )


@app.route("/feedback")
def feedback():
    """Show answer feedback and explanation."""
    player = get_current_player()
    if player is None:
        return redirect(url_for("login"))

    answer = session.get("last_answer")
    if not answer:
        flash("No recent answer was found.", "error")
        return redirect(url_for("level_selection"))

    level = find_level(answer["level_number"])
    next_question_number = answer["question_number"] + 1
    level_finished = next_question_number > len(level.questions)
    passed = False

    if level_finished:
        correct_count = session.get("level_correct_count", 0)
        needed_to_pass = max(1, len(level.questions) // 2 + 1)
        passed = correct_count >= needed_to_pass

        if passed:
            player.current_level = level.level_number
            player.add_badge(level.badge_name)
            next_level_number = level.level_number + 1
            if next_level_number <= len(levels):
                player.unlock_level(next_level_number)
            save_player(player)

    return render_template(
        "feedback.html",
        player=player,
        level=level,
        answer=answer,
        next_question_number=next_question_number,
        level_finished=level_finished,
        passed=passed,
        correct_count=session.get("level_correct_count", 0),
        progress_percent=progress_percent(player),
    )


@app.route("/progress")
def progress():
    """Show saved progress."""
    return login_required_page("progress.html")


@app.route("/leaderboard")
def leaderboard():
    """Display all players sorted by score."""
    all_progress = data_manager.load_progress()
    players = []
    for username, saved_data in all_progress.items():
        player = Player.from_dict(saved_data)
        players.append(player)

    players.sort(key=lambda player: player.score, reverse=True)
    return render_template("leaderboard.html", players=players)


@app.route("/logout")
def logout():
    """Log out the current user."""
    session.clear()
    flash("You have logged out. Your progress is saved in progress.json.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
