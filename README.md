# Surface Detection for Safe Drone Landing (ISRO IROC-25)
This project simulates a vision-based iṣntelligent landing system for lunar exploration missions, inspired by ISRO's Chandrayaan series. Using YOLOv8 object detection and OpenCV, the system identifies unsafe regions (craters) and highlights safe landing zones for drones on the Moon’s rugged surface.


## OBJECTIVE:
The goal is to help autonomous drones safely land on unfamiliar lunar terrain by:

Detecting craters (unsafe zones)

Identifying flat and obstacle-free areas (safe zones)

Visualizing this in real-time or from satellite/drone images

## FEATURES:
YOLOv8 trained on custom lunar crater dataset

Real-time or static image-based surface analysis

Green boxes represent detected craters (unsafe for landing)

Blue boxes indicate grid areas evaluated to be safe for landing

Overlap checking ensures craters do not interfere with landing zones

Designed to support lunar rover or drone landing simulations

## TECH STACK:
TOOL	    PURPOSE
YOLOv8	    Object detection of craters
OpenCV	    Image processing and visualization
Python	    Core programming language
Roboflow	Dataset annotation and augmentation
LabelImg	Manual annotation for custom classes

## DATASET:
The dataset was collected and annotated using Roboflow and LabelImg
Class used: Crater
Format: YOLO format (compatible with Ultralytics)


## SAMPLE OUTPUT:

Craters are marked using green bounding boxes

Safe landing zones are highlighted with blue grid boxes

The system avoids grid regions overlapping with craters

## HOW IT WORKS:
Load the trained YOLOv8 model

Run object detection on a given image

Extract crater positions from the detection output

Divide the image into fixed-size grids

For each grid:

Check if it overlaps with any detected crater

If not, label it as a safe landing zone
