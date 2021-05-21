import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#blank[:] = 0,0,255
#cv.imshow('Rectangle', blank)

##Draw rectangle, thickness=-1 fill the rectangle, thickness > 0 will fill only the edge
cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness=-1)
#cv.imshow('Rectangle', blank)

##Draw circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
#cv.imshow('circle', blank)

###Draw line
cv.line(blank, (0,0), (250,250), (0,0,255), thickness=1)
#cv.imshow('line', blank)

### place text
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)



cv.waitKey(0)
cv.destroyAllWindows()