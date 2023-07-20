import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
Settings_file_path = os.path.join(current_dir, "Settings.py")

def apply_Settings():
    bot_token = bot_token_input.get()
    guild_id = guild_id_input.get()

    # Get the directory path of the current script
    with open(Settings_file_path, "w") as file:
        file.write(f"bot_token = '{bot_token}'\n")
        file.write(f"guild_id = '{guild_id}'\n")

def load_Settings():
    try:
        with open(Settings_file_path, "r") as file:
            Settings = file.readlines()

        for line in Settings:
            if line.startswith("bot_token"):
                bot_token = line.split("=")[1].strip().strip("'")
                bot_token_input.delete(0, tk.END)
                bot_token_input.insert(0, bot_token)
            elif line.startswith("guild_id"):
                guild_id = line.split("=")[1].strip().strip("'")
                guild_id_input.delete(0, tk.END)
                guild_id_input.insert(0, guild_id)

    except FileNotFoundError:
        print("Settings.py not found")
        pass

def compile_action():
    bot_token = bot_token_input.get()
    guild_id = guild_id_input.get()

    if bot_token and guild_id:  # Check if both bot_token and guild_id are not empty
        # Display the warning message
        messagebox.showerror("Compiling...", "compiling...")
    else:
        # Clear the warning message if either bot_token or guild_id is empty
        messagebox.showerror("Error", "Both Bot Token and Guild ID must be filled.")

app = tk.Tk()
app.title("Settings")
app.geometry("300x200")

bot_token_label = tk.Label(app, text="Bot Token:")
bot_token_label.pack()
bot_token_input = tk.Entry(app)
bot_token_input.pack()

guild_id_label = tk.Label(app, text="Guild ID:")
guild_id_label.pack()
guild_id_input = tk.Entry(app)
guild_id_input.pack()

apply_button = tk.Button(app, text="Apply", command=apply_Settings)
apply_button.pack()

load_button = tk.Button(app, text="Load", command=load_Settings)
load_button.pack()

quit_button = tk.Button(app, text="Quit", command=app.quit)
quit_button.pack()

compile_button = tk.Button(app, text="Compile", command=compile_action)
compile_button.pack()

app.mainloop()
