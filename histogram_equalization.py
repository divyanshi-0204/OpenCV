import cv2 
from matplotlib import pyplot as plt 

path = r'C:\Users\Divyanshi Bhardwaj\Downloads\lena.jpg'
image = cv2.imread(path) 

equ = cv2.equalizeHist(image)
res = np.hstack((image, equ))

cv2.imshow(res) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 