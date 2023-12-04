"""

This program takes every 30th frame of a video, extracts it, saves any detected faces to one folder and the full frame to another

"""


from deepface import DeepFace
import cv2
import os

# Set the path to your video 
video_capture = cv2.VideoCapture(r"images\video_source.mp4")
video_frames_directory = "Video Frames"
detected_faces_directory = "Detected Faces"

os.makedirs(video_frames_directory, exist_ok=True)
os.makedirs(detected_faces_directory, exist_ok=True)

frame_number = 0
n_frames = 29  # Extract every 30th frame, this can be changed to improve performance/time or video coverage
detector_backend = "retinaface"  # Choose from ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe', 'yolov8', 'yunet', 'fastmtcnn']

while True:
    are_more_frames, frame = video_capture.read()
    if not are_more_frames:
        break

    # Check if the current frame number is a multiple of 30
    if frame_number % (n_frames + 1) == 0:
        # Detect faces using DeepFace
        

        faces = DeepFace.extract_faces(frame, enforce_detection=False, detector_backend=detector_backend)

        # Save all frames
        filename_all_frames = os.path.join(video_frames_directory, f"frame_{frame_number}.jpg")
        cv2.imwrite(filename_all_frames, frame)

        # Process each detected face
        for i, face in enumerate(faces):

            # Extract face coordinates
            w = int(face["facial_area"]["w"])
            h = int(face["facial_area"]["h"])
            x = int(face["facial_area"]["x"])
            y = int(face["facial_area"]["y"])

            # Extract and save the face
            face_image = frame[y:y + h, x:x + w]
            filename_detected_faces = os.path.join(detected_faces_directory, f"face_{frame_number}_{i + 1}.jpg")
            cv2.imwrite(filename_detected_faces, face_image)

    frame_number += 1

video_capture.release()
cv2.destroyAllWindows()
