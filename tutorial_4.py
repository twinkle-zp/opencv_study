import cv2.cv2 as cv
import numpy as np
#导包使使用cv2.cv2才会有代码提示

def add_demo(m1,m2):   #两张图片需要同样大
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):   #两张图片需要同样大
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

def divide_demo(m1, m2):  # 两张图片需要同样大
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):  # 两张图片需要同样大
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow("logic_demo", dst)

def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con-bri-demo",dst)

src1 = cv.imread("")
src2 = cv.imread("")
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
add_demo(src1,src2)

cv.waitKey(0)
cv.destroyAllWindows()


