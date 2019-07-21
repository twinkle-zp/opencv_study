import cv2.cv2 as cv
import numpy as np
#导包使使用cv2.cv2才会有代码提示

def extrace_object_demo():     #追踪颜色
    capture = cv.VideoCapture("")    #填写视频路径
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c=cv.waitKey(40)
        if c == 27:
            break;

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
extrace_object_demo()
b,g,r = cv.split(src)   #通道分离
cv.imshow("blue",b)
cv.imshow("gree",g)
cv.imshow("red",r)
src[:,:,2]=0
src = cv.merge([b,g,r])   #通道合并
cv.imshow("change",src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")