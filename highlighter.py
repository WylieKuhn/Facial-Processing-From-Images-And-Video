import cv2

# Load the image
image_path = r"output_frames\frame_2550.jpg"  # Replace with your image path
image = cv2.imread(image_path)

# Assuming you have the coordinates (x, y, w, h)
x, y, w, h = 513, 532, 156, 194  # Replace with your actual coordinates

# Draw a rectangle around the specified region
color = (0, 255, 0)  # BGR color (green in this case)
thickness = 2  # Line thickness
cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)

# Display the image with the highlighted region
cv2.imshow("Highlighted Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()