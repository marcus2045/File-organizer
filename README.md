# File-organizer
A simple, lightweight Windows utility that automatically organizes files inside a chosen folder into sub‑folders based on file type. Built in Python with a Tkinter GUI and packaged as a standalone  so it works on any Windows machin

• 	Choose a main folder to organize
• 	Automatically creates sub‑folders:
• 	CSV files
• 	Text files
• 	Images
• 	Executables
• 	Audio files
• 	Custom skins ()
• 	Archives (, , )
• 	“Run Organizer” button to manually trigger sorting
• 	“Change Folder” button to update the target directory
• 	Remembers the selected folder using a config file
• 	Optional Windows startup support
• 	No Python required when using the exe

📁 How the App Works (Using )
1. Download the App
Download the  file and place it anywhere you like (Desktop, Documents, etc.).
2. Run the Program
Double‑click  to launch the File Organizer window.
3. Choose Your Main Folder
Click Change Folder
→ Select the folder you want the app to organize
→ The app will save this choice (see bug note above)
4. Run the Organizer
Click Run Organizer to sort all files in the selected folder.
The app will:
• 	Create sub‑folders if they don’t exist
• 	Move files into the correct category
• 	Show a confirmation message when finished
5. Enable or Disable Startup (Optional)
• 	Enable Startup → App launches automatically when Windows starts
• 	Disable Startup → Removes the startup entry
6. Config File
The app stores your chosen folder in app data roaming


For the smoothest experience, set your web browser’s default Download location to the same folder you selected inside the File Organizer app.
This ensures that every new file you download is automatically placed into the folder the app manages, making organization effortless and keeping your system tidy without any extra steps.
Most browsers allow you to change the download location in their Settings → Downloads menu.



• 	Python
• 	Tkinter
• 	PyInstaller (for  build)
• 	winshell + pywin32 (for Windows startup support)
