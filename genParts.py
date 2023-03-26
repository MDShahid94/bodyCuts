# Import the required modules
import cv2
import numpy as np

# Read the image from the given image link
img = cv2.imread("https://img2.cgtrader.com/items/2353155/c038b14108/no306-male-t-pose-3d-model-obj.jpg")

# Get the body parts locations from the OpenPose algorithm
body_parts = {"nose": (248, 189), "left eye": (237, 184), "right eye": (259, 184), "left ear": (224, 191), "right ear": (272, 191), "left shoulder": (194, 241), "right shoulder": (302, 241), "left elbow": (151, 321), "right elbow": (345, 321), "left wrist": (108, 401), "right wrist": (388, 401), "left hip": (206, 401), "right hip": (290, 401), "left knee": (206, 561), "right knee": (290, 561), "left ankle": (206, 721), "right ankle": (290, 721)}

# Define a margin for cropping around each body part
margin = 10

# Loop through each body part and crop it into a separate image
for part in body_parts:
    # Get the x and y coordinates of the body part
    x = body_parts[part][0]
    y = body_parts[part][1]

    # Define the cropping region with the margin
    x1 = max(0, x - margin)
    y1 = max(0, y - margin)
    x2 = min(img.shape[1], x + margin)
    y2 = min(img.shape[0], y + margin)

    # Crop the image using numpy slicing
    cropped_img = img[y1:y2, x1:x2]

    # Save the cropped image as a new layer with the part name
    cv2.imwrite(part + ".png", cropped_img)