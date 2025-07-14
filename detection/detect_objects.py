from ultralytics import YOLO
import pandas as pd
from pathlib import Path
import os

# Define path to the image directory (from Task 1)
image_dir = Path(r"C:\Users\Admin\Desktop\KAIM\Week 7\telegram_medical_pipeline\data\raw\telegram_messages\2025-07-09\media")
output_csv = "data/yolo_detections.csv"

# Create processed directory if it doesn't exist
output_path.parent.mkdir(parents=True, exist_ok=True)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  

# Initialize result container
results_list = []

# Detect objects in each image
for img_file in image_dir.glob("*.[jJ][pP][gG]"):  # Case-insensitive JPG matching
    image_id = img_file.stem  # Use file name without extension as message_id
    results = model(str(img_file))[0]

    for box in results.boxes:
        cls_name = results.names[int(box.cls)]
        conf = float(box.conf)
        results_list.append({
            "message_id": image_id,
            "detected_object_class": cls_name,
            "confidence_score": round(conf, 4)
        })

# Convert to DataFrame and save
df = pd.DataFrame(results_list)
df.to_csv(output_path, index=False)

print(f"✅ YOLO detections saved to {output_path}")
