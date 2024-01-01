# File Organizer Script

## Overview
This Python script organizes files in a specified directory into subfolders based on their file type. It is designed to handle images, GIFs, and videos, sorting them into 'Pictures', 'GIFS', and 'Videos' folders, respectively. Additionally, any file exceeding a size threshold is moved into a 'TOO_BIG' subfolder within these respective folders. The origin of this script was to organize my downloads from Discord and Telegram and know what I could share on Discord without upgrading my account.

## Functionality
- **Directory Sorting:** Moves files into 'Pictures', 'GIFS', or 'Videos' based on their extensions.
- **Size Filtering:** Moves files larger than 15MB into a 'TOO_BIG' subfolder to indicate large files.
- **Duplicate Handling:** Renames files with duplicate names to prevent overwriting.

## Supported File Types
- **Pictures:** .jpg, .png, .jpeg
- **GIFS:** .gif
- **Videos:** .mov, .mp4, .m4v, .mkv

## How to Run

### Prerequisites
- Python installed on your system.
- Backup your files before running the script to prevent accidental data loss.

### Steps
1. **Modify the Script:**
   - Open the script in a text editor.
   - Change the `base_directory` variable to the path of your target directory.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```
     python file_organizer.py
     ```

## Important Notes
- The script only scans the specified base directory; it won't recurse into deeper folders unless they're 'Pictures', 'GIFS', or 'Videos'.
- Ensure you have the necessary permissions to create folders and move files in the specified directory.
- Large files are determined by a size threshold (default 15MB), which you can modify in the script.

## Customization
To customize file types or size limits, modify the `folders` dictionary and `size_limit` variable in the script.

## Disclaimer
This script moves and renames files. Always ensure you have backups and test the script in a controlled environment before running it on a large number of files.

## Support
For any issues or suggestions, please contact the script maintainer.

