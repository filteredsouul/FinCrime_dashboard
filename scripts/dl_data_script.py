import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("andrejzuba/revolutassignment")

print("Path to dataset files:", path)

# Move the files to the data directory
destination_path = "/Users/charles-francoisfouti-loemba/Documents/Documents/Projets/FInCrime/data"

#Create a data directory if it doesnt exist
os.makedirs(destination_path, exist_ok=True)

#Copy all files from the downloaded path to the destination path
for file_name in os.listdir(path):
    full_file_name = os.path.join(path, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, destination_path)
        print(f"Copied {file_name} to {destination_path}")
print("All files copied successfully to the data directory.")