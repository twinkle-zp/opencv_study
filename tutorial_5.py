import cv2.cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyImg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyImg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)

def fill_binary(image):
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:]=255
    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301]=0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill_binary",image)
'''
FLOODFILL_FIXED_RANGE  改变图像，泛洪填充
FLOODFILL_MASK_ONLY  不改变图像、只填充遮罩层本身、忽略新的颜色值参数
'''

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)     
#fill_color_demo(src)
fill_binary(src)
'''
face = src[100:300, 150:350]   #查找脸的范围
gray = cv.cvtColor(face, cv.C  OLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[100:300, 150:350] = backface   #将灰度图像塞回去
cv.imshow("face",src)
'''

cv.waitKey(0)
cv.destroyAllWindows()
