import cv2
import numpy as np
import main_functionlib
import time
CIR = main_functionlib.CIR
ratio = main_functionlib.ratio
inner_circle_rad = main_functionlib.inner_circle_rad
outer_circle_rad = main_functionlib.outer_circle_rad

flag = 0
#PPX/PPZ:predicted point x/z
def input_again(event, x, y, flags, param):
    global flag
    if event == 1:
        flag = 1
        #if (x > 1700 and x < 1915 and y > 700 and y < 790):
            #flag = 1

def reset():
    global flag
    flag = 0

def st_menu_display(circle):  
    #700*700 rectangle
    #3000/6000/9000/12100/15200/18200/21300/24400
    img = np.zeros((800, 2500, 3), np.uint8)
    img[:, :] = (255, 255, 255)

    cv2.rectangle(img, pt1=(50, 50), pt2=(750, 750), color=(0, 0, 0), thickness=3)

    inner_display_rad = int(inner_circle_rad[circle] * ratio[circle])
    outer_display_rad = int(outer_circle_rad[circle] * ratio[circle])

    cv2.circle(img, (400, 400), outer_display_rad, (150, 255, 200), -1)
    cv2.circle(img, (400, 400), inner_display_rad, (255, 255, 255), -1)
    cv2.putText(img, 'Click X on top right to close program', (50,30), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 0), 1, cv2.LINE_AA)
    
    #for i in range(36):
    #    CIR[circle].append([i+1,i])
    
    cr = ratio[circle]

    if circle == 6:
        d = 20
        fs = 0.5
    elif circle == 4 or circle == 5:
        d = 25
        fs = 0.75
    elif circle == 0 or circle == 1 or circle == 2 or circle == 3 or circle == 7:
        d = 50
        fs = 1
    for i in range(len(CIR[circle])):
        #print(CIR[circle][i][0], CIR[circle][i][1])
        x = CIR[circle][i][0] * (-1)
        y = CIR[circle][i][1]
        xcr = int(x * cr)
        ycr = int(y * cr)
        cv2.putText(img, 'Circle %d stronghold %d : (%d,%d)' %(circle + 1,i + 1,x,y), (800,50 + d * i), cv2.FONT_HERSHEY_SIMPLEX , fs, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.circle(img, (400 + xcr, 400 + ycr), 10, (0, 0, 255), -1)

    cv2.rectangle(img, pt1=(1700, 700), pt2=(1915, 790), color=(0, 255, 255), thickness=-1)#create a bottom
    cv2.rectangle(img, pt1=(1701, 699), pt2=(1916, 791), color=(0, 100, 255), thickness=2)
    cv2.putText(img, "input again", (1750, 750), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (200, 70, 90), 1, cv2.LINE_8)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,50), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,69), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,50), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 0), 1, cv2.LINE_AA)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,750), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 0), 1, cv2.LINE_AA)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,50), cv2.FONT_HERSHEY_SIMPLEX , 0.75, (0, 0, 0), 1, cv2.LINE_AA)
    #cv2.putText(img, 'Circle '+str(circle)+' stronghold', (800,750), cv2.FONT_HERSHEY_SIMPLEX , 0.75, (0, 0, 0), 1, cv2.LINE_AA)
        
    #write circle number inside white circle
    #dynamic font size and location adjustment using for loop
    #change font
    #import list from main
    #a1=50,d=19,an=750,word_size=0.5,displayed_data=36,maximum craming setting for circle 7
    #a1=50,d=50,an=750,word_size=1,displayed_data=15,maximum craming setting for circle 1,2,3,4,8
    #a1=50,d=25,an=750,word_size=0.75,displayed_data=29,maximum craming setting for circle 5,6

    cv2.namedWindow("Stronghold Locator", cv2.WINDOW_AUTOSIZE)

    cv2.setMouseCallback('Stronghold Locator', input_again)
    cv2.imshow('Stronghold Locator', img)

    while True:
        time.sleep(0.00001)
        #cv2.waitKey(0)
        if flag != 0:
            cv2.destroyAllWindows()
            break
        cv2.waitKey(1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#st_menu_display()