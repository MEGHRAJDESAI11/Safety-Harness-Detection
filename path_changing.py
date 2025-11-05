import json
import os

def change_image_paths_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.json'):
                json_file = os.path.join(root, file_name)
                change_image_path(json_file)

def change_image_path(json_file):
    # Read the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the filename (without extension) from the JSON file path
    filename = os.path.splitext(os.path.basename(json_file))[0]

    # Replace the "imagePath" field with the filename
    data["imagePath"] = filename + ".jpg"

    # Write the updated JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

# Example usage:
folder_path =r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote4"  # Replace with your folder path
change_image_paths_in_folder(folder_path)
