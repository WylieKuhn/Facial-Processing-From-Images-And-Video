import cv2
import os

# Specify the input folder containing images
input_folder = "Video Frames"

# Specify the output folder for saving detected faces
output_folder = "detected_faces"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Iterate over each image in the input folder
for filename in os.listdir(input_folder):
    # Read the image
    image_path = os.path.join(input_folder, filename)
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        # Crop the face region
        face_image = image[y:y + h, x:x + w]

        # Save the cropped face image
        face_filename = os.path.join(output_folder, filename + "_face.jpg")
        cv2.imwrite(face_filename, face_image)

        # Draw a rectangle around the detected face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)

