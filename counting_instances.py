import os

# Define a function to count instances of each label in all text files in a folder
def count_labels_in_folder(folder_path):
    # Initialize an empty dictionary to store counts
    label_counts = {}
    
    # Iterate over each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a text file
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            # Open the file and read each line
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # Iterate over each line
                for line in lines:
                    # Split the line by spaces to separate label and coordinates
                    elements = line.strip().split()
                    # Get the label (the first element)
                    label = elements[0]
                    # If the label is already in the dictionary, increment its count
                    if label in label_counts:
                        label_counts[label] += 1
                    # If the label is not in the dictionary, add it with count 1
                    else:
                        label_counts[label] = 1
    
    return label_counts

# Provide the path to your folder containing the text files
folder_path = r"C:\Users\ASUS\Downloads\harness\counting"

# Call the function to count instances of each label in all text files in the folder
label_counts = count_labels_in_folder(folder_path)

# Print the counts
for label, count in label_counts.items():
    print(f"Label {label}: {count} instances")

