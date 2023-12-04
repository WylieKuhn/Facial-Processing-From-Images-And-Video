import cv2
import os

video_capture = cv2.VideoCapture(r"images\video_source.mp4")
output_folder = "Video Frames"

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)

# Extract every 30th frame assuming 30fps footage, this can be altered to extract any n-frames for performance and time
n_frames = 29  

frame_number = 0
while True:
    are_more_frames, frame = video_capture.read()
    if not are_more_frames:
        break

    if frame_number % (n_frames + 1) == 0:
        filename = os.path.join(output_folder, "frame_" + str(frame_number) + ".jpg")
        cv2.imwrite(filename, frame)

    frame_number += 1

video_capture.release()
cv2.destroyAllWindows()