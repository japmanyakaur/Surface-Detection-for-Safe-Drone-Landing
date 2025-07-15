


import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 trained model
model = YOLO("runs/detect/train4/weights/best.pt") 

# Defining the class name
class_names = {0: "Crator"}  

# Loading the image
image_path = "sample.png"  
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Resizing image 
image = cv2.resize(image, (640, 480))


processed_image = image.copy()

# Runing YOLOv8 
results = model(processed_image)

# Storing detected objects for further processing
rock_boxes = []


for result in results:
    for box, conf, cls_id in zip(result.boxes.xyxy, result.boxes.conf, result.boxes.cls):
        x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
        class_id = int(cls_id)  # Convert class index to integer

        # Get the class name from dictionary
        class_name = class_names.get(class_id, "Unknown") 

    
        cv2.rectangle(processed_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        
        label = f"{class_name} ({conf:.2f})"
        cv2.putText(processed_image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        
        rock_boxes.append((x1, y1, x2, y2))

# safe landing zones
safe_spots = []

grid_size = 80  
for i in range(0, 640, grid_size):
    for j in range(0, 480, grid_size):
        # Define a candidate safe landing box
        safe_x1, safe_y1 = i, j
        safe_x2, safe_y2 = i + grid_size, j + grid_size

        # Checking the box overlap case
        is_safe = True
        for rx1, ry1, rx2, ry2 in rock_boxes:
            if not (safe_x2 < rx1 or safe_x1 > rx2 or safe_y2 < ry1 or safe_y1 > ry2):
                is_safe = False
                break

        
        if is_safe:
            safe_spots.append((safe_x1, safe_y1, safe_x2, safe_y2))
            cv2.rectangle(processed_image, (safe_x1, safe_y1), (safe_x2, safe_y2), (255, 0, 0), 2)  # Blue box


cv2.imshow("Detection", processed_image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()
