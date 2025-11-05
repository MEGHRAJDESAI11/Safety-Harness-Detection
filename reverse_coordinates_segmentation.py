import os

def transform_coordinates(coordinates):
    transformed_coords = []
    for i in range(0, len(coordinates), 2):
        x = coordinates[i]
        y = coordinates[i + 1]
        transformed_x = 1 - float(x)
        transformed_coords.extend([str(transformed_x), y])
    return transformed_coords

# Input and output folder paths
input_folder = r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote4/YOLODataset/labels/val"
output_folder = r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote4/YOLODataset/labels/val"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename[:-4] + "_rev.txt")
        
        # Open input file for reading
        with open(input_file, "r") as file:
            lines = file.readlines()
        
        # Process each line
        transformed_lines = []
        for line in lines:
            parts = line.split()
            class_index = parts[0]
            coordinates = parts[1:]
            transformed_coords = transform_coordinates(coordinates)
            transformed_line = class_index + " " + " ".join(transformed_coords) + "\n"
            transformed_lines.append(transformed_line)
        
        # Write transformed data to output file
        with open(output_file, "w") as file:
            file.writelines(transformed_lines)
        
        print("Transformation complete. Output saved to", output_file)
