import cv2
import numpy as np
import time
import os

rec = 0


def menu(event, x, y, flags, param):
    global rec
    if event == 1:
        if (x > 30 and x < 620 and y > 30 and y < 240):
            rec = 1
        if (x > 30 and x < 620 and y > 260 and y < 470):
            rec = 2

def main_menu():
    global rec
    img = np.zeros((500, 650, 3), np.uint8)
    img[:, :] = (250, 250, 250)
    black_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'black.png'))
    stronghold_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'stronghold.png'))
    end_city_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'end_city.png'))
    stronghold_img = cv2.resize(stronghold_img, None,0,fx = 0.3, fy = 0.3, interpolation=cv2.INTER_AREA)
    end_city_img = cv2.resize(end_city_img, None,0,fx = 0.3, fy = 0.253, interpolation=cv2.INTER_AREA)
    black_img = cv2.resize(black_img, (650, 500), cv2.INTER_CUBIC)
    stronghold_size = stronghold_img.shape
    end_city_size = end_city_img.shape

    img[0:500, 0:650] = black_img
    img[50:221, 40:261] = stronghold_img
    img[270:441, 40:261] = end_city_img

    text1 = "Stronghold locator"
    text2 = "End City locator"
    cv2.putText(img, text1, (291, 135), cv2.FONT_HERSHEY_TRIPLEX,
                0.8, (50, 200, 50), 1, cv2.LINE_8)
    cv2.putText(img, text2, (291, 365), cv2.FONT_HERSHEY_TRIPLEX,
                0.8, (200, 0, 200), 1, cv2.LINE_8)

    cv2.namedWindow("Main_Menu", cv2.WINDOW_AUTOSIZE)

    cv2.setMouseCallback('Main_Menu', menu)
    cv2.imshow('Main_Menu', img)
    while True:
        time.sleep(0.00001)
        #cv2.waitKey(0)
        if rec != 0:
            cv2.destroyAllWindows()
            return rec
        cv2.waitKey(1)


main_menu()