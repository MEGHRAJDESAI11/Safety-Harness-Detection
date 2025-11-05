from PIL import Image
import os

def reverse_image(image_path):
    image = Image.open(image_path)
    reversed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return reversed_image

def reverse_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(folder_path, filename)
            reversed_image = reverse_image(image_path)
            output_path = os.path.join(folder_path, filename.split(".")[0]+"_rev.jpg")
            reversed_image.save(output_path)

# Example usage
folder_path = r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote4/YOLODataset/images/train"
reverse_images_in_folder(folder_path)


# from PIL import Image
# import os

# def reverse_image(image_path):
#     image = Image.open(image_path)
#     reversed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
#     return reversed_image

# def reverse_images_in_folder(folder_path, output_folder):
#     os.makedirs(output_folder, exist_ok=True)
#     for filename in os.listdir(folder_path):
#         if filename.endswith((".jpg", ".jpeg", ".png")):
#             image_path = os.path.join(folder_path, filename)
#             reversed_image = reverse_image(image_path)
#             output_path = os.path.join(output_folder, filename)
#             reversed_image.save(output_path)

# # Example usage
# input_folder = r"/Users/meghrajdesai11/Desktop/internship/val"
# output_folder = r"/Users/meghrajdesai11/Desktop/internship/val2"
# reverse_images_in_folder(input_folder, output_folder)
