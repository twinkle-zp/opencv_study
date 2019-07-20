import cv2.cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape);
    height=image.shape[0]
    width=image.shape[1]
    channels=image.shape[2]
    print("width:%s,height:%s,channels:%s"%(width,height,channels))
    for row in range(height):       #循环每个像素并改变其值
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c]=255-pv
    cv.imshow("pixels_demo",image)

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)

def create_image():
    '''   三通道
    img = np.zeros([400,400,3],np.uint8)   #创建一个三通道图像
    #img[: ,: , 0] = np.ones([400,400])*255  #修改第一个通道的值
    img[:, :, 2] = np.ones([400, 400]) * 255  # 三通道分别为blue，green，red
    cv.imshow("new image", img)
    '''
    img = np.zeros([400,400,1],np.uint8)  #创建一个单通道图像,初值为0,可将zeros改为ones,则初值为1
    img[:,:,0] = np.ones([400,400])*127
    #img = img*127
    cv.imshow("new image",img)

    '''
    n1 = np.ones([3,3],np.uint8)
    n1.fill(12222.388)
    print(n1)
    
    n2 = n1.reshape([1,9])
    print(n2)
    
    n3 = np.array([[2,3,4],[4,5,6],[7,8,9]],np.int32)
    n3.fill(9)
    print(n3)
    '''

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
#access_pixels(src)
inverse(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency();   #计算时间
print("time:%s ms"%(time*1000))
create_image()
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")