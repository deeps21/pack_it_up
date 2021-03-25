import cv2 as cv

img = cv.imread('secondary.jfif')
img = cv.resize(img,(800,850))
cv.imwrite('secondary1.jpg',img)
#cv.imshow('img',img)
#cv.waitKey(0)