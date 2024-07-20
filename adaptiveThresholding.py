import cv2  
import numpy as np  

path = r'C:\Users\Divyanshi Bhardwaj\Downloads\lena.jpg'
image = cv2.imread(path) 
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5) 
  
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5) 

cv2.imshow('Adaptive Mean', thresh1) 
cv2.imshow('Adaptive Gaussian', thresh2) 

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()