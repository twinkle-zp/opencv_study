import cv2.cv2 as cv
import numpy as np


src = cv.imread("F:/photo/tx.jpg")

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
face = src[100:300, 150:350]   #查找脸的范围
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[100:300, 150:350] = backface   #将灰度图像塞回去
cv.imshow("face",src)
cv.waitKey(0)
cv.destroyAllWindows()
