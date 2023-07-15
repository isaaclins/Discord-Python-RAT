import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 300, 200)

        self.bot_token_label = QLabel("Bot Token:", self)
        self.bot_token_label.move(20, 20)
        self.bot_token_input = QLineEdit(self)
        self.bot_token_input.move(120, 20)

        self.guild_id_label = QLabel("Guild ID:", self)
        self.guild_id_label.move(20, 50)
        self.guild_id_input = QLineEdit(self)
        self.guild_id_input.move(120, 50)

        self.save_button = QPushButton("Save", self)
        self.save_button.move(40, 100)
        self.save_button.clicked.connect(self.save_settings)

        self.load_button = QPushButton("Load", self)
        self.load_button.move(120, 100)
        self.load_button.clicked.connect(self.load_settings)

        self.apply_button = QPushButton("Apply", self)
        self.apply_button.move(200, 100)
        self.apply_button.clicked.connect(self.apply_settings)

    def save_settings(self):
        bot_token = self.bot_token_input.text()
        guild_id = self.guild_id_input.text()

        with open("settings.txt", "w") as file:
            file.write(f"bot_token = '{bot_token}'\n")
            file.write(f"guild_id = '{guild_id}'\n")

    def load_settings(self):
        try:
            with open("settings.txt", "r") as file:
                settings = file.readlines()

            for line in settings:
                if line.startswith("bot_token"):
                    bot_token = line.split("=")[1].strip().strip("'")
                    self.bot_token_input.setText(bot_token)
                elif line.startswith("guild_id"):
                    guild_id = line.split("=")[1].strip().strip("'")
                    self.guild_id_input.setText(guild_id)

        except FileNotFoundError:
            pass

    def apply_settings(self):
        bot_token = self.bot_token_input.text()
        guild_id = self.guild_id_input.text()

        with open("settings.py", "w") as file:
            file.write(f"bot_token = '{bot_token}'\n")
            file.write(f"guild_id = '{guild_id}'\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsWindow()
    window.show()
    sys.exit(app.exec_())
