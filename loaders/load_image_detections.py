import os
import psycopg2
from ultralytics import YOLO
from PIL import Image

# === Configuration ===
IMAGE_DIR = "data/raw/telegram_messages/2025-07-09/media/"
YOLO_MODEL = "yolov8n.pt"  # Or yolov8s.pt, yolov8m.pt, etc.
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "telegram_medical",
    "user": "postgres",
    "password": "2328"  
}

# === Initialize YOLO model ===
model = YOLO(YOLO_MODEL)

# === Connect to PostgreSQL ===
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# === Process Images ===
for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(IMAGE_DIR, file)

    # Extract message_id from filename, e.g., "12345_image.jpg" → 12345
    message_id = os.path.splitext(file)[0].split("_")[0]

    # Run YOLO detection
    results = model(image_path)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            # Insert into DB
            cursor.execute("""
                INSERT INTO raw.image_detections (message_id, detected_object_class, confidence_score)
                VALUES (%s, %s, %s)
            """, (message_id, class_name, confidence))

    print(f"✅ Processed and inserted: {file}")

# === Finalize ===
conn.commit()
cursor.close()
conn.close()
print("✅ All image detections loaded into raw.image_detections.")
