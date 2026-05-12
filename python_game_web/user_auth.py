"""Registration and login features for Python Quest."""

import hashlib

from models import Player


class UserAuth:
    """Handles user registration, login, and starting progress records."""

    def __init__(self, data_manager):
        self.data_manager = data_manager

    def hash_password(self, password):
        """Hash a password using a standard library algorithm."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register_user(self, username, password):
        """Register a user from either CLI or web input.

        Returns a tuple: (success, message). Keeping this logic in UserAuth
        lets both versions of the game use the same validation and storage.
        """
        users = self.data_manager.load_users()
        progress = self.data_manager.load_progress()

        username = username.strip()
        password = password.strip()

        if not username:
            return False, "Username cannot be empty."
        if not password:
            return False, "Password cannot be empty."
        if username in users:
            return False, "That username already exists. Please log in or choose another username."

        users[username] = {"password": self.hash_password(password)}
        progress[username] = Player(username).to_dict()

        self.data_manager.save_users(users)
        self.data_manager.save_progress(progress)
        return True, "Registration successful. You can now log in."

    def login_user(self, username, password):
        """Validate a username and password and return (player, message)."""
        users = self.data_manager.load_users()
        progress = self.data_manager.load_progress()

        username = username.strip()
        password = password.strip()

        if not username:
            return None, "Username cannot be empty."
        if not password:
            return None, "Password cannot be empty."
        if username not in users:
            return None, "Login failed: username was not found."

        saved_password = users[username].get("password")
        if saved_password != self.hash_password(password):
            return None, "Login failed: incorrect password."

        if username not in progress:
            progress[username] = Player(username).to_dict()
            self.data_manager.save_progress(progress)

        return Player.from_dict(progress[username]), f"Welcome back, {username}!"

    def register(self):
        """Register a new user account."""
        print("\n--- Register ---")
        username = input("Choose a username: ").strip()
        password = input("Choose a password: ").strip()

        success, message = self.register_user(username, password)
        print(message)
        if not success:
            return None
        return username

    def login(self):
        """Log in an existing user and return a Player object."""
        print("\n--- Login ---")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        player, message = self.login_user(username, password)
        print(message)
        return player
