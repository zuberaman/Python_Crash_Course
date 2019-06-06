import cv2

img = cv2.imread('img.png')
h_img = cv2.flip(img, 0)
v_img = cv2.flip(img, 1)
b_img = cv2.flip(img, -1)

cv2.imshow('image', img)
cv2.imshow('horizontal', h_img)
cv2.imshow('vertical', v_img)
cv2.imshow('both', b_img)

cv2.waitKey(0)