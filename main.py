import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import winshell
from win32com.client import Dispatch

CONFIG_FILE = "folder_config.txt"

# -----------------------------
# Load or ask for folder
# -----------------------------
def load_folder():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    return None

def save_folder(path):
    with open(CONFIG_FILE, "w") as f:
        f.write(path)

# -----------------------------
# Folder picker
# -----------------------------
def change_folder():
    folder = filedialog.askdirectory(title="Select your main folder")
    if folder:
        save_folder(folder)
        folder_label.config(text=f"Current folder:\n{folder}")
        messagebox.showinfo("Folder Updated", "Folder has been changed.")

# -----------------------------
# File organizer logic
# -----------------------------
def run_organizer():
    source = load_folder()
    if not source:
        messagebox.showerror("Error", "No folder selected. Click 'Change Folder' first.")
        return

    folder_names = {
        "csv files": [".csv"],
        "text_files": [".txt"],
        "image_files": [".png", ".jpg", ".jpeg", ".webp"],
        "executable_files": [".exe"],
        "audio_files": [".mp3", ".wav"],
        "custom_skins": [".fantome"],
        "zip_files": [".zip", ".rar", ".7z"]
    }

    # Create subfolders
    for folder in folder_names:
        folder_path = os.path.join(source, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files
    for file in os.listdir(source):
        file_path = os.path.join(source, file)

        if os.path.isfile(file_path):
            for folder, extensions in folder_names.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(source, folder, file))
                    break

    messagebox.showinfo("Done", "Files organized successfully!")

# -----------------------------
# Windows Startup toggle
# -----------------------------
def enable_startup():
    startup = winshell.startup()
    shortcut_path = os.path.join(startup, "FileOrganizer.lnk")

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = sys.executable
    shortcut.Arguments = f'"{os.path.abspath(__file__)}"'
    shortcut.WorkingDirectory = os.getcwd()
    shortcut.save()

    messagebox.showinfo("Startup Enabled", "App will now start with Windows.")

def disable_startup():
    startup = winshell.startup()
    shortcut_path = os.path.join(startup, "FileOrganizer.lnk")

    if os.path.exists(shortcut_path):
        os.remove(shortcut_path)
        messagebox.showinfo("Startup Disabled", "App will no longer start with Windows.")
    else:
        messagebox.showinfo("Not Enabled", "Startup was not enabled.")

# -----------------------------
# GUI Setup
# -----------------------------
app = tk.Tk()
app.title("File Organizer")
app.geometry("350x300")

current_folder = load_folder()
folder_label = tk.Label(app, text=f"Current folder:\n{current_folder if current_folder else 'None selected'}")
folder_label.pack(pady=10)

tk.Button(app, text="Run Organizer", width=20, command=run_organizer).pack(pady=5)
tk.Button(app, text="Change Folder", width=20, command=change_folder).pack(pady=5)
tk.Button(app, text="Enable Startup", width=20, command=enable_startup).pack(pady=5)
tk.Button(app, text="Disable Startup", width=20, command=disable_startup).pack(pady=5)

app.mainloop()
