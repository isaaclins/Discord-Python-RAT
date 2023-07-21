import tkinter as tk
from tkinter import filedialog, messagebox
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
    try:
        with open(Settings_file_path, "r") as file:
            Settings = file.readlines()

        for line in Settings:
            if line.startswith("bot_token"):
                bot_token = line.split("=")[1].strip().strip("'")

            elif line.startswith("guild_id"):
                guild_id = line.split("=")[1].strip().strip("'")

    except FileNotFoundError:
        messagebox.showerror("Error", "You haven't even applied ;C Enter the bot token and guild ID and press the Apply button")
        pass

    if bot_token and guild_id:  # Check if both bot_token and guild_id are not empty
        # Display the warning message
        messagebox.showerror("Compiling...", "Compiling...")
    else:
        # Clear the warning message if either bot_token or guild_id is empty
        messagebox.showerror("Error", "Both Bot Token and Guild ID must be filled.")

app = tk.Tk()
app.title("SlytherCord builder")
app.geometry('700x620')
app.resizable(True, True)
app.configure(bg='#0A0A10')
app.tk_setPalette(background='#0A0A10', foreground='white', activeBackground='#0A0A10', activeForeground='white')

# Left Frame for labels
left_frame = tk.Frame(app, bg='#0A0A10')
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Right Frame for input fields and buttons
right_frame = tk.Frame(app, bg='#0A0A10')
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

bot_token_label = tk.Label(left_frame, text="Bot Token:", fg='white', bg='#0A0A10')
bot_token_label.pack(side=tk.TOP)

guild_id_label = tk.Label(left_frame, text="Guild ID:", fg='white', bg='#0A0A10')
guild_id_label.pack(side=tk.TOP)

bot_token_input = tk.Entry(right_frame)
bot_token_input.pack(side=tk.TOP)

guild_id_input = tk.Entry(right_frame)
guild_id_input.pack(side=tk.TOP)
 
apply_button = tk.Button(left_frame, text="Apply", command=apply_Settings)
apply_button.pack(side=tk.TOP, pady=10, padx=150)

load_button = tk.Button(left_frame, text="Load", command=load_Settings)
load_button.pack(side=tk.TOP, pady=10, padx=150)

quit_button = tk.Button(right_frame, text="Quit", command=app.quit)
quit_button.pack(side=tk.TOP, pady=10, padx=150)

compile_button = tk.Button(right_frame, text="Compile", command=compile_action)
compile_button.pack(side=tk.TOP, pady=10, padx=150)

app.mainloop()
