import cv2
import numpy as np
import os
import time

flag2 = 0

def close_intro(event,x,y,u,q):
    global flag2 
    if event == 1:
        flag2 = 1

def st_introduction_display():
    img = np.zeros((600, 1100, 3), np.uint8)
    img[:, :] = (255, 255, 255)

    circle_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'circle.png'))
    circle_img = cv2.resize(circle_img, (540, 540), cv2.INTER_AREA)
    img[30:570, 560:1100] = circle_img

    topic = "Stronghold Locator Introduction"
    cv2.putText(img, topic, (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (205, 0, 0), 2, cv2.LINE_8)
    text2 = "  By constructing two vectors that points to the"
    cv2.putText(img, text2, (30, 75), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text3 = "stronghold,This method is called \"two point location\" "
    cv2.putText(img, text3, (30, 110), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    

    text4 = "  The 128 strongholds in a minecraft world is arranged "
    cv2.putText(img, text4, (30, 145), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text5 = "in a specific way.Every stronghold belongs to a"
    cv2.putText(img, text5, (30, 180), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text6 = "\"concentric circles\" shaped area. only 8 such"
    cv2.putText(img, text6, (30, 215), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text7 = "circles exist in a game map, and all of them"
    cv2.putText(img, text7, (30, 250), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text8 = "host different numbers of strongholds."
    cv2.putText(img, text8, (30, 285), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    

    text9 = "  The strongholds inside a concentric circles is  "
    cv2.putText(img, text9, (30, 320), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text10 = "roughly on the lines that perfectly divides the circle "
    cv2.putText(img, text10, (30, 355), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text11 = "which, means if you obtain the slope rate of one "
    cv2.putText(img, text11, (30, 390), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text12 = "stronghold, you only need an additional vector"
    cv2.putText(img, text12, (30, 425), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text13 = "to locate the rest of the strongholds in that"
    cv2.putText(img, text13, (30, 460), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text14 = "circle using mathematical means.This method"
    cv2.putText(img, text14, (30, 495), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text15 = "of locating strongholds with prior data is called "
    cv2.putText(img, text15, (30, 530), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    text16 = "\"one point location\"."
    cv2.putText(img, text16, (30, 565), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (205, 0, 0), 1, cv2.LINE_8)
    cv2.namedWindow("st_introduction", cv2.WINDOW_AUTOSIZE)

    cv2.setMouseCallback('st_introduction', close_intro)
    cv2.imshow('st_introduction', img)

    while True:
        time.sleep(0.00001)
        #cv2.waitKey(0)
        if flag2 != 0:
            cv2.destroyAllWindows()
            return flag2
        cv2.waitKey(1)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

