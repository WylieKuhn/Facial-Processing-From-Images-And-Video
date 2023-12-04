import cv2
import os

video_capture = cv2.VideoCapture(r"C:\Users\Wylie\Documents\GitHub\Facial Processing From Images And Video\Images\test_footage.mp4")
output_dir = "Video Frames"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

frame_number = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    filename = os.path.join(output_dir, "frame_" + str(frame_number) + ".jpg")
    cv2.imwrite(filename, frame)

    frame_number += 1
