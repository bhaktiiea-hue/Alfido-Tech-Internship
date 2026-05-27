# Import required modules
import os
import shutil

# Function to create and write into a file
try:
    with open("sample.txt", "w") as file:
        file.write("Hello! This is a sample text file.\n")
        file.write("Python file handling is easy to learn.")

    print("File created and data written successfully.")

except Exception as e:
    print("Error while writing file:", e)


# Function to read file content
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error while reading file:", e)


# Rename the file
try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("\nFile renamed successfully.")

except Exception as e:
    print("Error while renaming file:", e)


# Create a new folder
folder_name = "backup_folder"

try:
    os.mkdir(folder_name)
    print("Folder created successfully.")

except FileExistsError:
    print("Folder already exists.")


# Move file into folder
try:
    shutil.move("renamed_sample.txt", folder_name)
    print("File moved successfully.")

except Exception as e:
    print("Error while moving file:", e)


# Delete the file
try:
    file_path = os.path.join(folder_name, "renamed_sample.txt")

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

except Exception as e:
    print("Error while deleting file:", e)
