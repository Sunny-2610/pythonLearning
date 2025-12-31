import os

folder_name = "my_folder"

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' removed.")
else:
    print(f"Folder '{folder_name}' does not exist.")
