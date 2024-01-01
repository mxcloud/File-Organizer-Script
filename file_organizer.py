import os
import shutil

# Define the base directory
base_directory = 'D:\\Downloads'

# Define the folders and their corresponding file extensions
folders = {
    'Pictures': ['.jpg', '.png', '.jpeg'],
    'GIFS': ['.gif'],
    'Videos': ['.mov', '.mp4', '.m4v', '.mkv']
}

# Size limit for the files to be considered "TOO_BIG" (in bytes)
size_limit = 15 * 1024 * 1024  # 15MB

# Function to safely move files, handling duplicates
def safe_move(file_path, target_folder):
    file_name = os.path.basename(file_path)
    new_path = os.path.join(target_folder, file_name)
    base, extension = os.path.splitext(file_name)
    
    counter = 1
    # If a file with the same name exists, find a new name
    while os.path.exists(new_path):
        new_name = f"{base}_{counter}{extension}"
        new_path = os.path.join(target_folder, new_name)
        counter += 1

    # Move the file
    shutil.move(file_path, new_path)

# Function to organize files based on size and extension
def organize_files(directory, folders, size_limit):
    # Create the main folders and TOO_BIG subfolders
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        os.makedirs(os.path.join(folder_path, 'TOO_BIG'), exist_ok=True)

    # Move files to their respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_ext = os.path.splitext(file)[1].lower()
            for folder, extensions in folders.items():
                target_folder = os.path.join(directory, folder)
                if file_size > size_limit:
                    # Move too big files to the TOO_BIG folder
                    safe_move(file_path, os.path.join(target_folder, 'TOO_BIG'))
                    break
                elif file_ext in extensions:
                    # Move files based on extension
                    safe_move(file_path, target_folder)
                    break

    # Organize existing files in subfolders
    for folder in folders:
        organize_subfolder(os.path.join(directory, folder), size_limit)

# Function to move large files in subfolders to the TOO_BIG folder
def organize_subfolder(folder_path, size_limit):
    too_big_path = os.path.join(folder_path, 'TOO_BIG')
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file_path != too_big_path:
            file_size = os.path.getsize(file_path)
            if file_size > size_limit:
                safe_move(file_path, too_big_path)

# Run the organization process
organize_files(base_directory, folders, size_limit)
