import cv2 
import numpy as np 


image = cv2.imread('cards.png') 

window_name = 'Image'

kernel = np.ones((5, 5), np.uint8) 

image = cv2.erode(image, kernel) 

cv2.imshow(window_name, image) 