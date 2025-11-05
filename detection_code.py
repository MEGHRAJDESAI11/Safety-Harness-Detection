import torch
import time
from ultralytics import YOLO
 
device = torch.device('cuda')
model=YOLO(r'C:\Users\ASUS\Downloads\harness\24-4.pt').to(device)
 
results=model.track(source=r"C:\Users\ASUS\Downloads\D10_S20240425112955_E20240425113106.mp4",show=True,iou=0.3,conf=0.2,save=True,save_txt=False,tracker="bytetrack.yaml")

# for result in results:
#     boxes = result.boxes.cpu().numpy()
#     b_id = result.boxes.id.cpu().numpy()

# print(boxes)
# print(b_id)