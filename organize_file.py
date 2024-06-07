import os
import shutil

def organize_files_by_extension(directory, script_name):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Skip directories and the script file itself
        if os.path.isdir(os.path.join(directory, filename)) or filename == script_name:
            continue

        # Extract the file extension
        _, extension = os.path.splitext(filename)

        # Remove the leading dot from the extension
        extension = extension[1:]

        if not extension:  # Skip files with no extension
            continue

        # Create a folder for the extension if it doesn't exist
        folder_path = os.path.join(directory, extension.upper())
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the corresponding folder
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

if __name__ == "__main__":
    # Get the current directory
    current_directory = os.getcwd()
    # Name of this script file
    script_file_name = os.path.basename(__file__)
    organize_files_by_extension(current_directory, script_file_name)
    print(f"Files organized in {current_directory}, excluding {script_file_name}")

