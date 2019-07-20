import cv2.cv2 as cv
#导包使使用cv2.cv2才会有代码提示

def color_space_demo(image):
    gray = cvtColor()

src = cv.imread("F:/photo/tx.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
print("Hi,python")