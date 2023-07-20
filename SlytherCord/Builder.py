import tkinter as tk
from tkinter import filedialog

def save_settings():
    bot_token = bot_token_input.get()
    guild_id = guild_id_input.get()

    with open("settings.py", "w") as file:
        file.write(f"bot_token = '{bot_token}'\n")
        file.write(f"guild_id = '{guild_id}'\n")

def load_settings():
    try:
        with open("settings.py", "r") as file:
            settings = file.readlines()

        for line in settings:
            if line.startswith("bot_token"):
                bot_token = line.split("=")[1].strip().strip("'")
                bot_token_input.delete(0, tk.END)
                bot_token_input.insert(0, bot_token)
            elif line.startswith("guild_id"):
                guild_id = line.split("=")[1].strip().strip("'")
                guild_id_input.delete(0, tk.END)
                guild_id_input.insert(0, guild_id)

    except FileNotFoundError:
        pass

def apply_settings():
    save_settings()

app = tk.Tk()
app.title("Settings")
app.geometry("300x200")

bot_token_label = tk.Label(app, text="Bot Token:")
bot_token_label.place(x=20, y=20)
bot_token_input = tk.Entry(app)
bot_token_input.place(x=120, y=20)

guild_id_label = tk.Label(app, text="Guild ID:")
guild_id_label.place(x=20, y=50)
guild_id_input = tk.Entry(app)
guild_id_input.place(x=120, y=50)

save_button = tk.Button(app, text="Save", command=save_settings)
save_button.place(x=40, y=100)

load_button = tk.Button(app, text="Load", command=load_settings)
load_button.place(x=120, y=100)

apply_button = tk.Button(app, text="quit", command=app.quit)
apply_button.place(x=200, y=100)

app.mainloop()
