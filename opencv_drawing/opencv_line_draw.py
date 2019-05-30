import numpy as np
import cv2
from os.path import dirname, abspath
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Create a black image
    img = np.zeros((512, 512, 3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    font = cv2.FONT_HERSHEY_SIMPLEX

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 255))
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

    # title
    cv2.namedWindow('opencv', cv2.WINDOW_NORMAL)
    cv2.imshow('opencv',img)
    # 写图片
    path = dirname(dirname(abspath(__file__)))
    cv2.imwrite(path+'/img'+'/draw.jpg', img)
    k = cv2.waitKey(0)  # Wait for user input and quit
    if k == 27:  # 如果输入ESC退出
        cv2.destroyAllWindows()

    # plot show
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
