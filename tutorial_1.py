import cv2.cv2 as cv
import numpy as np
#读取摄像头
def video_demo():
    capture = cv.VideoCapture(0) #括号中可以是视频路径 
    while(True):
        ret, frame=capture.read()
        frame = cv.flip(frame,1)   #摄像头镜像
        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c==27:
            break

#获取图片信息
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)    #大小等于形状的三个参数相乘
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")