import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

path = r'C:\Users\Divyanshi Bhardwaj\Downloads\lena.jpg'
image = cv2.imread(path)

dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15) 

plt.subplot(121), plt.imshow(image) 
plt.subplot(122), plt.imshow(dst) 

plt.show() 
