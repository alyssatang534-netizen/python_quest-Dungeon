"""Main game flow and menus for Python Quest."""

from data_manager import DataManager
from python_questions import get_levels
from user_auth import UserAuth


class Game:
    """Controls menus, login state, gameplay, and saving progress."""

    def __init__(self):
        self.data_manager = DataManager()
        self.auth = UserAuth(self.data_manager)
        self.levels = get_levels()
        self.current_player = None

    def run(self):
        """Start the game and show the main menu until the player exits."""
        print("=" * 50)
        print("Python Quest: The Coding Dungeon")
        print("=" * 50)

        while True:
            if self.current_player is None:
                self.show_guest_menu()
            else:
                self.show_player_menu()

    def show_guest_menu(self):
        """Menu shown before a user logs in."""
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = self.get_menu_choice("Choose an option: ", [1, 2, 3])

        if choice == 1:
            self.auth.register()
        elif choice == 2:
            self.current_player = self.auth.login()
        elif choice == 3:
            print("Thanks for playing Python Quest. Goodbye!")
            raise SystemExit

    def show_player_menu(self):
        """Menu shown after a user logs in."""
        print(f"\nPlayer Menu - Logged in as {self.current_player.username}")
        print("1. Start/Continue Game")
        print("2. View Progress")
        print("3. Save Progress")
        print("4. Logout")
        print("5. Exit")

        choice = self.get_menu_choice("Choose an option: ", [1, 2, 3, 4, 5])

        if choice == 1:
            self.start_game()
        elif choice == 2:
            self.view_progress()
        elif choice == 3:
            self.save_current_progress()
        elif choice == 4:
            self.save_current_progress()
            print(f"{self.current_player.username} has logged out.")
            self.current_player = None
        elif choice == 5:
            self.save_current_progress()
            print("Progress saved. Thanks for playing Python Quest!")
            raise SystemExit

    def get_menu_choice(self, prompt, valid_choices):
        """Get a numeric menu choice and validate it."""
        while True:
            try:
                choice = int(input(prompt).strip())
                if choice in valid_choices:
                    return choice
                print(f"Invalid choice. Please choose one of: {valid_choices}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start_game(self):
        """Let the player choose an unlocked level and play it."""
        print("\nUnlocked Levels")
        for level in self.levels:
            if level.level_number in self.current_player.unlocked_levels:
                print(f"{level.level_number}. {level.title}")

        print("0. Return to player menu")
        valid_choices = self.current_player.unlocked_levels + [0]
        level_number = self.get_menu_choice("Choose a level: ", valid_choices)

        if level_number == 0:
            return

        selected_level = self.find_level(level_number)
        if selected_level is None:
            print("That level could not be found.")
            return

        passed = selected_level.play(self.current_player)

        if passed:
            self.current_player.current_level = selected_level.level_number
            next_level_number = selected_level.level_number + 1
            if next_level_number <= len(self.levels):
                self.current_player.unlock_level(next_level_number)
                print(f"Level {next_level_number} unlocked!")
            else:
                print("All levels completed. Amazing work!")

        self.save_current_progress()

    def find_level(self, level_number):
        """Return the Level object with the matching level number."""
        for level in self.levels:
            if level.level_number == level_number:
                return level
        return None

    def view_progress(self):
        """Display the logged-in player's progress."""
        print("\n--- Progress ---")
        print(f"Username: {self.current_player.username}")
        print(f"Current Level Completed: {self.current_player.current_level}")
        print(f"Score: {self.current_player.score}")
        print(f"Unlocked Levels: {self.current_player.unlocked_levels}")

        if self.current_player.badges:
            print("Badges:")
            for badge in self.current_player.badges:
                print(f"- {badge}")
        else:
            print("Badges: None yet")

    def save_current_progress(self):
        """Save the current player's progress to progress.json."""
        if self.current_player is None:
            print("No player is logged in.")
            return

        progress = self.data_manager.load_progress()
        progress[self.current_player.username] = self.current_player.to_dict()
        self.data_manager.save_progress(progress)
        print("Progress saved.")
