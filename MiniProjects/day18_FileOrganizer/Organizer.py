import os
import shutil
from datetime import datetime

# Source and destination folders
current_directory = os.path.dirname(__file__)

SOURCE_FOLDER = os.path.join(current_directory, "sample_files")
DESTINATION_FOLDER = os.path.join(current_directory, "organized")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".js", ".html", ".css"]
}

# Create destination folders
for category in FILE_TYPES:
    os.makedirs(os.path.join(DESTINATION_FOLDER, category), exist_ok=True)

# Log function
def write_log(message):
    os.makedirs(os.path.join(current_directory, "logs"), exist_ok=True)

    with open(os.path.join(current_directory, "logs", "organizer.log"), "a") as log_file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{time}] {message}\n")

# Organize files
for file_name in os.listdir(SOURCE_FOLDER):

    source_path = os.path.join(SOURCE_FOLDER, file_name)

    # Skip directories
    if os.path.isdir(source_path):
        continue

    moved = False

    for category, extensions in FILE_TYPES.items():

        if file_name.lower().endswith(tuple(extensions)):

            destination_path = os.path.join(
                DESTINATION_FOLDER,
                category,
                file_name
            )

            shutil.move(source_path, destination_path)

            print(f"Moved: {file_name} -> {category}")

            write_log(f"Moved {file_name} to {category}")

            moved = True
            break

    if not moved:
        print(f"Skipped: {file_name}")
        write_log(f"Skipped {file_name}")

# output
# PS C:\Users\hp\python-learning-journey> & C:/Users/hp/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/hp/python-learning-journey/MiniProjects/day18_FileOrganizer/Organizer.py
# Moved: cat.jpg -> Images
# Moved: hello.py -> Code
# Moved: notes.pdf -> Documents
# Moved: song.mp3 -> Music
# And the log file will contain entries like:
# [2024-06-01 12:00:01] Moved cat.jpg to Images
# [2024-06-01 12:00:02] Moved hello.py to Code
# [2024-06-01 12:00:03] Moved notes.pdf to Documents
# [2024-06-01 12:00:04] Moved song.mp3 to Music 
# This code organizes files from a source folder into categorized subfolders based on their file extensions. It also logs the actions taken for each file, including any files that were skipped.        