import cv2
import numpy as np
import main_functionlib
import os


def fuction2_display(Loc):
    playerx = int(Loc['player_x'])
    playerz = int(Loc['player_y'])

    #draw image
    img = np.zeros((700, 1100, 3), np.uint8)
    img[:, :] = (150, 150, 150)
    cv2.rectangle(img, pt1=(50, 50), pt2=(650, 650), color=(0, 0, 0), thickness=2)

    
    endcity_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'purpur block img.png'))
    #endcity_img from https://minecraft.fandom.com/wiki/Purpur_Block 2023/04/05
    endstone_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'end stone img.png'))
    #endstone_img from https://minecraft.fandom.com/wiki/End_Stone 2023/04/05
    player_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'player img.png'))
    #player_img from https://minecraft.fandom.com/wiki/Player 2023/04/05
    right_arrow_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'right arrow img.png'))
    down_arrow_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'down arrow img.png'))
    bottom_right_arrow_img = cv2.imread(os.path.join(os.getcwd(), 'resource', 'bottom right arrow img.png'))

    endcity_img = cv2.resize(endcity_img, (28, 28), cv2.INTER_AREA)
    endstone_img = cv2.resize(endstone_img, (28, 28), cv2.INTER_AREA)
    player_img = cv2.resize(player_img, (24, 24), cv2.INTER_AREA)
    right_arrow_img = cv2.resize(right_arrow_img, (28, 28), cv2.INTER_AREA)
    down_arrow_img = cv2.resize(down_arrow_img, (28, 28), cv2.INTER_AREA)
    bottom_right_arrow_img = cv2.resize(bottom_right_arrow_img, (28, 28), cv2.INTER_AREA)

    for i in range(20):
        for j in range(20):
            if i > 7 or j > 7:
                img[52 + 30 * i:80 + 30 * i, 52 + 30 * j:80 + 30 * j] = endstone_img
            else:
                img[52 + 30 * i:80 + 30 * i, 52 + 30 * j:80 + 30 * j] = endcity_img

    for i in range(8):
        img[52 + 30 * i:80 + 30 * i, 52 + 30 * 19:80 + 30 * 19] = right_arrow_img
        img[52 + 30 * 19:80 + 30 * 19, 52 + 30 * i:80 + 30 * i] = down_arrow_img

    img[52 + 30 * 19:80 + 30 * 19, 52 + 30 * 19:80 + 30 * 19] = bottom_right_arrow_img
    #locate player position
    relative_position = main_functionlib.player_relative_position(playerx, playerz)
    img[54 + 30 * relative_position[0]:78 + 30 * relative_position[0], 54 + 30 * relative_position[1]:78 + 30 * relative_position[1]] = player_img

    #draw info
    x_calculate = playerx // 16 - 1
    z_calculate = playerz // 16 - 1
    if round(abs(x_calculate) % 20) <= 8 and round(abs(z_calculate) % 20) <= 8:
        text1 = "In spawnable range,35% chance it's here "
        text2 = "if the biome is highland or midland"
        cv2.putText(img, text1, (675, 75), cv2.FONT_HERSHEY_SIMPLEX,
                        0.55, (255, 0, 0), 1, cv2.LINE_8)
        cv2.putText(img, text2, (675, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    0.55, (255, 0, 0), 1, cv2.LINE_8)
    else:
        text = "Out of range"
        cv2.putText(img, text, (675, 75), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 1, cv2.LINE_8)
    if playerx % 320 == 0:
        border_x = playerx
    else:
        border_x = (x_calculate - (x_calculate % 20)) * 16
    if playerz % 320 == 0:
        border_z = playerz
    else:
        border_z = (z_calculate - (z_calculate % 20)) * 16
    #draw topic
    text_topic = "Map of the nearby 20X20 chunk area"
    cv2.putText(img, text_topic, (130, 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (150, 0, 100), 2, cv2.LINE_8)
    #draw top border coordinate
    top_x = str(border_x)
    top_z1 = str(border_z)
    top_z2 = str(border_z + 320)
    top_left_text = "(" + top_x + "," + top_z1 + ")"
    top_right_text = "(" + top_x + "," + top_z2 + ")"
    cv2.putText(img, top_left_text, (0, 40), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1, cv2.LINE_8)
    cv2.putText(img, top_right_text, (600, 40), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1, cv2.LINE_8)

    #draw bottom border coordinate
    bottom_x = str(border_x + 320)
    bottom_z1 = str(border_z)
    bottom_z2 = str(border_z + 320)
    bottom_left_text = "(" + bottom_x + "," + bottom_z1 + ")"
    bottom_right_text = "(" + bottom_x + "," + bottom_z2 + ")"
    cv2.putText(img, bottom_left_text, (0, 675), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1, cv2.LINE_8)
    cv2.putText(img, bottom_right_text, (600, 675), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1, cv2.LINE_8)

    #draw illustration
    img[110:138, 675:703] = endcity_img
    text_pupur_block = ":End city chunk"
    cv2.putText(img, text_pupur_block, (705, 130), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (200, 70, 90), 2, cv2.LINE_8)
    img[110:138, 870:898] = endstone_img
    text_end_stone = ":Normal chunk"
    cv2.putText(img, text_end_stone, (900, 130), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (100, 70, 0), 2, cv2.LINE_8)
    img[145:169, 677:701] = player_img
    text_player_pos = ":Your location"
    cv2.putText(img, text_player_pos, (703, 162), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (0,40,180), 2, cv2.LINE_8)
    text_playerx = str(playerx)
    text_playerz = str(playerz)
    text_bottom_player_xy = "(" + text_playerx + "," + text_playerz + ")"
    cv2.putText(img, text_bottom_player_xy, (833, 162), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (0,40,180), 1, cv2.LINE_8)
    img[176:204, 675:703] = right_arrow_img
    text_arrow = ":It shows the end city chunk"
    cv2.putText(img, text_arrow, (703, 194), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (140,0,170), 1, cv2.LINE_8)
    text_arrow2 = " spawned beside this area."
    cv2.putText(img, text_arrow2, (703, 226), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (140,0,170), 1, cv2.LINE_8)



    #draw introduction
    text_intro1 = "Intoduction"
    cv2.putText(img, text_intro1, (675, 258), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro2 = "The end city have a 35% chance to be"
    cv2.putText(img, text_intro2, (675, 290), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro3 = "spawned in the highlands or midlands biome"
    cv2.putText(img, text_intro3, (675, 322), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro4 = "in the purple areas."
    cv2.putText(img, text_intro4, (675, 354), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro5 = "The purple area has a unique rectangle shape"
    cv2.putText(img, text_intro5, (675, 386), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro6 = "and the pattern will repeat in the entire map."
    cv2.putText(img, text_intro6, (675, 418), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro7 = "The areas that end city might spawn showed"
    cv2.putText(img, text_intro7, (675, 450), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro8 = "here are not the only one you will find,"
    cv2.putText(img, text_intro8, (675, 482), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro9 = "look at the arrows for the direction of others."
    cv2.putText(img, text_intro9, (675, 514), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro10 = "If uncertain about where they are exactly,"
    cv2.putText(img, text_intro10, (675, 546), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro11 = "key in the coordinates into this system,"
    cv2.putText(img, text_intro11, (675, 578), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)
    text_intro12 = "and it will show you the way."
    cv2.putText(img, text_intro12, (675, 610), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (205, 0, 0), 1, cv2.LINE_8)



    #display
    cv2.namedWindow("End City Locator", cv2.WINDOW_AUTOSIZE)
    cv2.imshow('End City Locator', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


#draw line
#i = 1
#while i <=19 :
    #cv2.line(img, (50 + 30 * i, 50), (50 + 30 * i, 650), (0, 0, 0) , 1)
    #cv2.line(img, (50, 50 + 30 * i), (650, 50 + 30 * i), (0, 0, 0) , 1)
    #i += 1
