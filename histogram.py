import cv2 
from matplotlib import pyplot as plt 

path = r'C:\Users\Divyanshi Bhardwaj\Downloads\lena.jpg'
image = cv2.imread(path) 

histr = cv2.calcHist([image],[0],None,[256],[0,256])

plt.plot(histr) 
plt.show() 


