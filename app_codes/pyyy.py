import shutil
import os

# Define the name of the file to copy
file_to_copy = 'hi.txt'  # Replace with the name of your file

# Define the destination folder
destination_folder = "../reports/"  # Replace with the path to your report folder

# Build the full path to the destination
destination_path = os.path.join(destination_folder, file_to_copy)

# Copy the file to the destination folder
shutil.copy(file_to_copy, destination_path)
