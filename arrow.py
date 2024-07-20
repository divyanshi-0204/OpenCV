import cv2 

path = r'C:\Users\Divyanshi Bhardwaj\Downloads\lena.jpg'
image = cv2.imread(path) 

window_name = 'Image'

start_point = (0, 0)
end_point = (200, 200)

color = (0, 255, 0)
thickness = 9

image = cv2.arrowedLine(image, start_point, end_point, color, thickness)

cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows() 