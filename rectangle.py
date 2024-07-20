import cv2

# Read the image from file
image = cv2.imread('blox.jpg')

# Define the window name
window_name = 'Image'

# Define the start and end points of the rectangle
start_point = (5, 5)
end_point = (220, 220)

# Define the color of the rectangle (BGR - Blue, Green, Red)
color = (255, 0, 0)

# Define the thickness of the rectangle border
thickness = 2

# Draw the rectangle on the image
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Display the image in a window
cv2.imshow(window_name, image)

# Wait for a key event indefinitely or for a specified amount of time
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
