from deepface import DeepFace

# Set the path to the image of the face you want to search for
image = r"images/joel.jpg"

# Set the folder with the extracted video frames you want to search
search_folder = "Video Frames 2"

dfs = DeepFace.find(img_path = image, db_path = search_folder, enforce_detection=False, detector_backend = "retinaface")

print(dfs)