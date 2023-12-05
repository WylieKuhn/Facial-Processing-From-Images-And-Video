import cv2
import os

def extract_frames(input_video_path, output_folder, n_frames):
    # Create the output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)

    # Set the frame number to 0 initially
    frame_number = 0
    frame_count = 0

    while True:
        # Set the next frame to be decoded
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        # Read the frame
        are_more_frames, frame = video_capture.read()

        # Check if there are no more frames
        if not are_more_frames:
            break

        filename = os.path.join(output_folder, f"frame_{frame_number}.jpg")
        cv2.imwrite(filename, frame)

        # Increment the frame number by the number of frames you want to skip
        frame_number += n_frames  # Adjust the value as needed
        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print(f"VIDEO PROCESSING FINISHED, {frame_count} IMAGES CREATED")
    

# Example usage:
input_video_path = "images/test_footage.mp4"
output_folder = "output_frames"


#extract_frames(input_video_path, output_folder)
