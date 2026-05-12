"""Data models for Python Quest.

This file contains the main classes used by the game. Keeping these classes
separate makes the project easier to understand and maintain.
"""


class Player:
    """Represents one logged-in player and their saved progress."""

    def __init__(self, username, current_level=1, score=0, unlocked_levels=None, badges=None):
        self.username = username
        self.current_level = current_level
        self.score = score
        self.unlocked_levels = unlocked_levels if unlocked_levels is not None else [1]
        self.badges = badges if badges is not None else []

    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def unlock_level(self, level_number):
        """Unlock a new level if it is not already unlocked."""
        if level_number not in self.unlocked_levels:
            self.unlocked_levels.append(level_number)
            self.unlocked_levels.sort()

    def add_badge(self, badge_name):
        """Award a badge if the player does not already have it."""
        if badge_name not in self.badges:
            self.badges.append(badge_name)

    def to_dict(self):
        """Convert the player object into a dictionary for JSON storage."""
        return {
            "username": self.username,
            "current_level": self.current_level,
            "score": self.score,
            "unlocked_levels": self.unlocked_levels,
            "badges": self.badges,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Player object from saved dictionary data."""
        return cls(
            username=data.get("username", ""),
            current_level=data.get("current_level", 1),
            score=data.get("score", 0),
            unlocked_levels=data.get("unlocked_levels", [1]),
            badges=data.get("badges", []),
        )


class Question:
    """Represents one multiple-choice Python question."""

    def __init__(self, text, options, correct_answer, explanation, topic):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer.upper()
        self.explanation = explanation
        self.topic = topic

    def ask(self):
        """Display the question and return True if the player answers correctly."""
        print("\n" + self.text)
        for letter, option in self.options.items():
            print(f"  {letter}. {option}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in self.options:
                break
            print("Invalid answer. Please enter A, B, C, or D.")

        if answer == self.correct_answer:
            print("Correct! The bug monster takes damage.")
            print(f"Explanation: {self.explanation}")
            return True

        print(f"Incorrect. The correct answer was {self.correct_answer}.")
        print(f"Explanation: {self.explanation}")
        return False


class Level:
    """Represents one game level containing several questions."""

    def __init__(self, level_number, title, questions, badge_name):
        self.level_number = level_number
        self.title = title
        self.questions = questions
        self.badge_name = badge_name

    def play(self, player):
        """Run all questions in this level and update the player's score."""
        print("\n" + "=" * 50)
        print(f"Level {self.level_number}: {self.title}")
        print("=" * 50)

        correct_count = 0
        points_per_question = 10

        for question_number, question in enumerate(self.questions, start=1):
            print(f"\nBug Monster {question_number} appears! Topic: {question.topic}")
            if question.ask():
                correct_count += 1
                player.add_score(points_per_question)
                print(f"+{points_per_question} points! Current score: {player.score}")

        needed_to_pass = max(1, len(self.questions) // 2 + 1)
        passed = correct_count >= needed_to_pass

        print("\nLevel result:")
        print(f"You answered {correct_count} out of {len(self.questions)} correctly.")

        if passed:
            print("Level completed! You defeated the bug monsters.")
            player.add_badge(self.badge_name)
        else:
            print("Level not completed yet. Review the explanations and try again.")

        return passed


class BossLevel(Level):
    """A special level for the final OOP boss battle.

    This class demonstrates inheritance because BossLevel reuses Level but
    changes the introduction and reward message.
    """

    def play(self, player):
        print("\nThe final OOP Boss blocks the dungeon exit!")
        passed = super().play(player)
        if passed:
            print("Boss defeated! You are now a Python Quest Champion.")
        return passed
