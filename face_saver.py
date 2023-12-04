import cv2
import matplotlib.pyplot as plt
import os

# Specify the input image path
imagePath = r"C:\Users\Wylie\Documents\GitHub\Facial Processing From Images And Video\Images\test.jpg"

# Create a directory to save detected faces
save_dir = "detected_faces"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Read the input image
img = cv2.imread(imagePath)

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the face classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces in the grayscale image
faces = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

# Initialize a counter for unique identifier
face_count = 1

# Iterate over detected faces
for (x, y, w, h) in faces:
    # Create a cropped face image
    face_image = img[y:y+h, x:x+w]

    # Save the cropped face image with a unique identifier
    face_path = os.path.join(save_dir, "face_" + str(face_count) + ".jpg")
    cv2.imwrite(face_path, face_image)

    # Draw a rectangle around the detected face
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    face_count += 1

# Convert the image back to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image with detected faces
"""plt.figure(figsize=(20, 10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()"""
