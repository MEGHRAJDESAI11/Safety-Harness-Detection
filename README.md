🦺 Safety Harness Detection Using YOLOv8

📘 Overview

This project focuses on automated safety harness detection using the YOLOv8 deep learning model.
It aims to improve workplace safety by detecting and classifying workers wearing or not wearing safety harnesses in real time from images or videos.

Developed during a Machine Learning Internship at Larsen & Toubro Energy Hydrocarbon,
this model classifies images into three categories:
	•	🟥 No Harness
	•	🟩 Harness with Hook
	•	🟨 Harness without Hook

⸻

🎯 Objectives
	•	Detect and classify safety harness categories in real-world conditions.
	•	Enable accurate localization using bounding boxes or segmentation.
	•	Improve detection accuracy using transfer learning.
	•	Support real-time video inference for industrial safety systems.
	•	Promote automation and compliance monitoring in high-risk environments.

🧰 Tools & Technologies
Category - Tools,
Language - Python,
Libraries - Ultralytics YOLOv8, PyTorch, OpenCV, NumPy, Matplotlib, Albumentations;
Annotation - LabelMe,
Environment - Anaconda, Jupyter Notebook, VS Code ;
Documentation - MS Word, GitHub

  📊 Dataset & Annotation

🖼️ Data Collection

Images and videos were collected from L&T project sites and extracted into frames using Python scripts.

🏷️ Data Annotation

Use LabelMe to label each image with one of the following classes:
	•	harness_with_hook
	•	harness_without_hook
	•	noharness

Command: #labelme --labels harness_with_hook,harness_without_hook,noharness

🧠 Model Training

🧾 Dataset YAML Configuration

#train: /path/to/train/images
#val: /path/to/val/images

#nc: 3
#names: ['harness_with_hook', 'harness_without_hook', 'noharness']

# Train the YOLOv8 segmentation model
yolo segment train data=dataset.yaml model=yolov8m-seg.pt epochs=100 imgsz=640

📈 Results
	•	Improved accuracy by 6.7% using transfer learning, reaching 63.7%.
	•	Successfully detected harness types in challenging industrial conditions.
	•	Supported real-time inference on live video streams.

⸻

🧩 Workflow Summary
	1.	Data Collection & Frame Extraction
	2.	Annotation using LabelMe
	3.	Convert Annotations (LabelMe → YOLO)
	4.	Data Preprocessing & Augmentation
	5.	Model Training with YOLOv8
	6.	Evaluation & Visualization (Precision, Recall, mAP)
	7.	Deployment for Real-Time Detection

⸻

📘 References
	•	Ultralytics YOLOv8 Documentation￼
	•	LabelMe Annotation Tool￼
	•	PyTorch Framework￼
	•	OpenCV Library￼
	•	NumPy Documentation￼

