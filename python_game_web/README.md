# Python Quest: The Coding Dungeon

Python Quest is a modular Python learning game for an INT101 Python for AI Assessment 1 project. Players register, log in, answer Python questions, defeat bug monsters, earn points, unlock levels, and collect badges.

The project now has two versions:

- A command-line interface (CLI) version using `main.py`
- A Flask web version using `app.py`

The web version is an enhancement. It reuses the same question bank, JSON files, OOP models, and progress system as the CLI version.

## How to Run the CLI Version

```bash
python3 main.py
```

On some systems, the command may be:

```bash
python main.py
```

## How to Run the Web Version

Install the required package:

```bash
pip install -r requirements.txt
```

Start the Flask app:

```bash
python3 app.py
```

Then open the local Flask URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

To open the web version from another device on the same Wi-Fi, use the computer's local network IP address instead of `127.0.0.1`, for example:

```text
http://192.168.1.23:5000
```

## How to Deploy the Web Version Online

The easiest public deployment option for this Flask project is Render.

1. Create a GitHub repository and upload this project.
2. Go to Render and create a new **Web Service** from that GitHub repository.
3. Use these settings:

```text
Language: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

4. Add an environment variable:

```text
SECRET_KEY: any-long-random-text-you-choose
```

5. Deploy the service.

After the deploy finishes, Render will give you a public URL like:

```text
https://your-service-name.onrender.com
```

That is the URL to share with the teacher.

Note: this project stores users and progress in `users.json` and `progress.json`. On many free hosting services, files created or changed while the app is running may not be permanent after a redeploy. This is fine for a simple class demo, but a real public app should use a database.

## File Structure

```text
main.py                  CLI entry point
app.py                   Flask web app entry point
models.py                OOP classes: Player, Question, Level, BossLevel
user_auth.py             Registration, login, password hashing
data_manager.py          JSON file loading and saving
game_logic.py            CLI game menus and gameplay
python_questions.py      Python question bank and level creation
users.json               Saved user accounts
progress.json            Saved player progress
requirements.txt         Flask dependency
README.md                Project documentation
templates/
  base.html
  index.html
  register.html
  login.html
  dashboard.html
  levels.html
  question.html
  feedback.html
  progress.html
  leaderboard.html
static/
  style.css
```

## Main Features

- User registration and login
- Hashed passwords using `hashlib`
- Separate saved progress for each user
- JSON file IO using `users.json` and `progress.json`
- Python quiz questions are the core gameplay
- Correct answers increase score
- Passing levels unlocks new levels
- Completing levels awards badges
- CLI and Flask web UI both use the same core project files
- Web dashboard, level cards, question page, answer feedback, progress page, and leaderboard

## Web Pages

- Welcome / Landing page
- Register page
- Login page
- Dashboard page
- Level selection page
- Question page
- Feedback / result page
- Progress page
- Leaderboard page
- Logout function

## Data Storage

- `users.json` stores account usernames and hashed passwords.
- `progress.json` stores each player's current level, score, unlocked levels, and badges.

The files are separate so account data and gameplay data stay organized.

## Python Learning Topics Covered

- Basic syntax
- Control structures
- Functions
- Data structures
- Object-oriented programming
- File IO
- Exception handling

## Assessment Requirement Mapping

| Requirement | Where it is shown |
| --- | --- |
| Python knowledge integration is the game core | `python_questions.py`, `Question`, `Level`, `BossLevel` |
| Players answer Python questions to progress | `Level.play()` in CLI and `/level/<level>/question/<question>` in Flask |
| User registration and login | `user_auth.py`, `register.html`, `login.html` |
| Independent progress per user | `progress.json`, `Player.username`, `save_player()` |
| Progress stores current level, score, unlocked levels, badges | `Player.to_dict()` in `models.py` |
| JSON file IO | `DataManager` in `data_manager.py` |
| Modular structure | Separate files for models, auth, data, game logic, questions, CLI, and web app |
| OOP | `Player`, `Question`, `Level`, `BossLevel`, `Game` |
| Input validation | CLI menu validation, form validation in `UserAuth`, locked-level checks in Flask |
| Exception handling | JSON loading and saving in `DataManager`, CLI numeric input handling |
| Web enhancement without breaking CLI | `app.py`, `templates/`, `static/`; `main.py` still runs CLI |

## How to Test

1. Run the CLI:

```bash
python3 main.py
```

2. Run the web version:

```bash
pip install -r requirements.txt
python3 app.py
```

3. In the web browser, register a new username and password.
4. Log in with that account.
5. Open **Levels**, choose an unlocked level, and answer questions.
6. After each answer, check the feedback and explanation.
7. Finish a level and check that score, unlocked levels, and badges update.
8. Log out, log in again, and confirm the progress reloads from `progress.json`.
9. Open **Leaderboard** and confirm players are sorted by score.
