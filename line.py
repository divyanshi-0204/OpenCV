import cv2 

image = cv2.imread('cards.png')

window_name = 'Image'

start_point = (0, 0)

end_point = (250, 250)

color = (0, 255, 0)

thickness = 9

image = cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow(window_name, image) 
