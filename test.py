import cv2.cv2 as cv
#导包使使用cv2.cv2才会有代码提示

src = cv.imread("F:/photo/tx.jpg")
'''
关于imread
1、斜杠方向与Windows中地址栏复制的斜杠相反
2、路径中不能有中文，图片名亦不能使中文
'''
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")