import cv2
import os
 
# Input folder containing videos
input_folder = r"/Users/meghrajdesai11/Desktop/internship/Annotations/videos/0.06.2024"
 
# Output folder to save frames
output_folder = r"/Users/meghrajdesai11/Desktop/internship/Annotations/frames/0.06.2024"
 
# Frame interval to save (every 100th frame)
frame_interval =20

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):  # Assuming the videos have mp4 extension
        video_path = os.path.join(input_folder, filename)
 
        # Create output folder for each video
        video_output_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
        os.makedirs(video_output_folder, exist_ok=True)
 
        # Open the video file
        cap = cv2.VideoCapture(video_path)
 
        # Read frames and save every 100th frame to the output folder
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
 
            frame_count += 1
 
            # Save every 100th frame as an image file
            if frame_count % frame_interval == 0:
                frame_filename = f"{frame_count:01d}.jpg"
                frame_path = os.path.join(video_output_folder, frame_filename)
                cv2.imwrite(frame_path, frame)
 
        # Release the video capture object
        cap.release()
 
print("Every 100th frame saved successfully.")