"""JSON file handling for user accounts and progress."""

import json
import os

USERS_FILE = "users.json"
PROGRESS_FILE = "progress.json"


class DataManager:
    """Loads and saves JSON data for the project."""

    def __init__(self, users_file=USERS_FILE, progress_file=PROGRESS_FILE):
        self.users_file = users_file
        self.progress_file = progress_file
        self.ensure_files_exist()

    def ensure_files_exist(self):
        """Create empty JSON files if they do not exist."""
        for file_name in [self.users_file, self.progress_file]:
            if not os.path.exists(file_name):
                self.save_json(file_name, {})

    def load_json(self, file_name):
        """Load JSON data safely.

        If the file is missing or corrupted, the program returns an empty
        dictionary instead of crashing.
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                print(f"Warning: {file_name} did not contain a dictionary. Resetting data.")
                return {}
        except FileNotFoundError:
            print(f"Warning: {file_name} was missing. Creating a new one.")
            self.save_json(file_name, {})
            return {}
        except json.JSONDecodeError:
            print(f"Warning: {file_name} is corrupted. Starting with empty data.")
            return {}
        except OSError as error:
            print(f"Could not read {file_name}: {error}")
            return {}

    def save_json(self, file_name, data):
        """Save dictionary data to a JSON file."""
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except OSError as error:
            print(f"Could not save {file_name}: {error}")

    def load_users(self):
        """Load all registered users."""
        return self.load_json(self.users_file)

    def save_users(self, users):
        """Save all registered users."""
        self.save_json(self.users_file, users)

    def load_progress(self):
        """Load progress for all players."""
        return self.load_json(self.progress_file)

    def save_progress(self, progress):
        """Save progress for all players."""
        self.save_json(self.progress_file, progress)
