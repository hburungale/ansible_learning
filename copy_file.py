import shutil
import os

# Define the paths to the file and the destination folder
file_to_copy = 'file_to_copy.txt'  # Replace with the name of your file
source_folder = '/path/to/app/code'  # Replace with the path to your app code folder
destination_folder = '/path/to/report'  # Replace with the path to your report folder

# Build the full paths to the file and destination
source_path = os.path.join(source_folder, file_to_copy)
destination_path = os.path.join(destination_folder, file_to_copy)

# Copy the file
shutil.copy(source_path, destination_path)
