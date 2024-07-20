
import cv2 

image = cv2.imread('blox.jpg') 

window_name = 'Image'
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0) 
cv2.imshow(window_name, image) 
