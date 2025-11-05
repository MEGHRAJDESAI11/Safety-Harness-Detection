from ultralytics import YOLO

# Load a model
model = YOLO(r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote/YOLODataset/yolov8m.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data=r"/Users/meghrajdesai11/Desktop/SafetyHarnessModel/Annote/YOLODataset/dataset.yaml", epochs=100, imgsz=640, device="mps" , batch=8)