import cv2.cv2 as cv
import  numpy as np
#导包使使用cv2.cv2才会有代码提示

def blur_demo(image):    #均值模糊
    dst = cv.blur(image,(15,1 ))
    cv.imshow("blur_demo",dst)

def media_blur_demo(image):    #中值模糊
    dst = cv.medianBlur(image,5)
    cv.imshow("blur_demo",dst)

def custom_blur_demo(image):    #自定义模糊
    kernel = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("blur_demo",dst)

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")