import cv2 as cv
import matplotlib.pyplot as plt
from os.path import dirname, abspath

if __name__ == '__main__':
    # 读图片
    image = cv.imread('img/image.jpg', cv.IMREAD_COLOR)  # Load the image
    # Or just: image=cv.LoadImage('img/image.png')

    # 输出文字
    cv.putText(image, 'lenka', (100, 100), cv.FONT_HERSHEY_TRIPLEX, 2, (127, 127, 127), 12)

    # lenka
    cv.namedWindow('lenka', cv.WINDOW_NORMAL)
    # Show the image
    cv.imshow('lenka', image)

    # 写图片
    path = dirname(dirname(abspath(__file__)))
    cv.imwrite(path+'/img/thumb.jpg', image)
    k = cv.waitKey(0)  # Wait for user input and quit
    if k == 27:  # 如果输入ESC退出
        cv.destroyAllWindows()

    plt.imshow(image, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
