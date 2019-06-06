import cv2
import numpy as np

img = cv2.imread('img.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([80,120,120])
upper_blue = np.array([130,255,255])

blueMask = cv2.inRange(imgHSV,lower_blue,upper_blue)

res = cv2.bitwise_and(img, img, blueMask)



cv2.imshow('img', img)
cv2.imshow('gray', grayImg)
cv2.imshow('mask', blueMask)
cv2.imshow('blue', res)

cv2.waitKey(0)

pagina 31 el pdf cicolani chapter 9