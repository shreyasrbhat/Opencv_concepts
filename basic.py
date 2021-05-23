#### essentual functions in opencv
import cv2 as cv

image = cv.imread('Photos/park.jpg')
#cv.imshow('cat', image)

### to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#cv.imshow('cat', gray_image)

### blur
blur_image = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)

### edge detection
edge_image = cv.Canny(blur_image, 125,175)

### dialation
dialated_image = cv.dilate(edge_image, (7,7), iterations=2)

### Erode
erode_image = cv.erode(dialated_image, (7,7), iterations=2)

### Resize 
resized_image = cv.resize(image, (500,500), interpolation=cv.INTER_CUBIC)

cv.imshow('cat', resized_image)
cv.waitKey(0)