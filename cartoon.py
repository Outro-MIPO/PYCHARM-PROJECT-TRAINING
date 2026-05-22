import cv2
import numpy as np

image = cv2.imread("mike.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, mask=edges)

cv2.imshow("Image", image)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitkey(0)
cv2.destroyAllwindows()