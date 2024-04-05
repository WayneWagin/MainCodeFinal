import math
import tkinter as tk

# ======================================================================================================== #
CIR = [[] for _ in range(8)]
LIN = [[] for _ in range(8)]
#[[[x1,y1]],[],[],[],[],[],[],[]]
ratio = [0.10653, 0.05095, 0.03348, 0.02493, 0.01986, 0.01651, 0.01412, 0.01234]
inner_circle_rad = [1280, 4352, 7424, 10496 ,13568, 16640, 19712, 22784]
outer_circle_rad = [2816, 5888, 8960, 12032, 15104, 18176, 21248, 24320]
nlist = [3,6,10,15,21,28,36,9]


def change_degree(a):
    a = float(a) * (-1) + 90
    return a


def keyin():
    output = []
    #print("Please input the first location")
    output.append(float(input("X:")))
    output.append(float(input("Z:")))
    output.append(float(input("degree:")))
    #print("Please input the second location")
    output.append(float(input("X:")))
    output.append(float(input("Z:")))
    output.append(float(input("degree:")))
    return output



def locate_first(x1, z1, d1, x2, z2, d2):
    output = []
    k = 0.01745329
    x1 = float(x1 * (-1))
    x2 = float(x2 * (-1))
    d1 = float(math.tan(change_degree(d1) * k))
    d2 = float(math.tan(change_degree(d2) * k))

    deltax = (d1 * x1 - z1) * (-1) - (-1) * (d2 * x2 - z2)
    deltaz = (d1 * (d2 * x2 - z2)) - ((d1 * x1 - z1) * d2)
    delta = (d1 * (-1)) - ((-1) * d2)
    output.append(round(deltax / delta))
    output.append(round(deltaz / delta))
    return output


def loc_range():
    x = float(input("Location(X):"))
    z = float(input("Location(Z):"))
    return x, z


def draw_square():
    display = [["-" for i in range(20)] for i in range(20)]
    for i in range(0, 8):
        for j in range(0, 8):
            display[i][j] = "+"
    return display

def player_relative_position(x, z) :
    x = (x // 16 + 1) % 20 - 1
    z = (z // 16 + 1) % 20 - 1
    if x < 0:
        x += 20
    if z < 0:
        z += 20
    return (x, z)


def quadratic(x, a, b):
    return (a * x) + b


# circumcenter_function_source:https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcircle_equations


def circumcenter(ax, ay, bx, by, cx, cy):
    ax, ay, bx, by, cx, cy = int(ax), int(ay), int(bx), int(by), int(cx), int(cy)
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    pax, pbx, pcx = ax * ax, bx * bx, cx * cx
    pay, pby, pcy = ay * ay, by * by, cy * cy
    # ^pow(ax), and so on
    ux = ((pax + pay) * (by - cy) + (pbx + pby) * (cy - ay) + (pcx + pcy) * (ay - by)) / d
    uy = ((pax + pay) * (cx - bx) + (pbx + pby) * (ax - cx) + (pcx + pcy) * (bx - ax)) / d
    dist = math.sqrt((ax - ux) * (ax - ux) + (ay - uy) * (ay - uy))
    return ux, uy, dist

def refactor(Loc, XF, YF):
    #XI, XII, YI, YII, DI, DII = int(Loc['XI']), int(Loc['XII']), int(Loc['YI']), int(Loc['YII']), int(Loc['DEGI']), int(Loc['DEGII'])
    XI, XII, YI, YII, DI, DII = Loc['XI'], Loc['XII'], Loc['ZI'], Loc['ZII'], Loc['DEGI'], Loc['DEGII']
    CCCx, CCCy, CCCd = circumcenter(XI, YI, XII, YII, XF, YF)
    # ^CCC == CirCumCenter, CCCd == distance to circumcenter

    r = float()
    r = CCCd / 250
    Render = {'ptax': XI, 'ptay': YI, 'ptbx': XII, 'ptby': YII, 'ptcx': XF, 'ptcy': YF, 'CCCx': CCCx, 'CCCy': CCCy, 'ratio': r}
    # ^ptax == point a x location, and so on
    return Render

def tan_angle_sum(tanA, tanB):
    tan_A_B = (tanA + tanB) / (1 - (tanA * tanB))
    return tan_A_B

def vector_dist(x, y):
    x, y = float(x), float(y)
    return math.sqrt(x * x + y * y)

def division(m, circle):
    n = nlist[circle]
    lines = []
    deg = (2 * math.pi) / n
    for i in range(0, n):
        lines.append(tan_angle_sum(math.tan(deg * i), m))
        #print(tan_angle_sum(math.tan(deg * i), m))
    return lines

def differencial(m, lines):
    for i in range(0, len(lines)):
        if (math.degrees(math.atan(m) - math.atan(lines[i]))) < 2.5: #0.3% error margin @circle 7
            return i + 1
    #print("Mathmetical error occurred while locating stronghold, closing the program")
    quit()

def matchmaking(x, y, deg, lines):

    loc = []
    min_dist = 100000
    min_m = 0

    for m in lines:
        dist = (abs(m * x - y) / math.sqrt(m ** 2 + 1))
        if dist < min_dist:
            min_dist = dist
            min_m = m
    '''
    vax = math.cos(math.radians(deg))
    vay = math.sin(math.radians(deg))
    valen = vector_dist(vax, vay)
    vbx = math.cos(math.atan(min_m))
    vby = math.cos(math.atan(min_m))
    vblen = vector_dist(vbx, vby)
    dot = vax * vbx + vay * vby
    cosAB = dot / (valen * vblen)
    sinAB = math.sqrt(1 - cosAB ** 2)
    true_dist = min_dist / sinAB
    r = true_dist / valen
    vcx = vax * r
    vcy = vay * r
    loc.append(x + vcx)
    loc.append(y + vcy)
    '''
    deltax = (math.tan(math.radians(deg)) * x - y) * (-1)
    deltaz = 0 - ((math.tan(math.radians(deg)) * x - y) * min_m)
    delta = (math.tan(math.radians(deg)) * (-1)) - ((-1) * min_m)
    loc.append(round(deltax / delta))
    loc.append(round(deltaz / delta))
    return loc

def loccircle(PPX,PPZ):
    circle = -1
    dist = vector_dist(PPX, PPZ)

    if dist > 1280 and dist < 2816: circle = 0
    elif dist > 4352 and dist < 5888: circle = 1 
    elif dist > 7424 and dist < 8960: circle = 2
    elif dist > 10496 and dist < 12032: circle = 3
    elif dist > 13568 and dist < 15104: circle = 4
    elif dist > 16640 and dist < 18176: circle = 5
    elif dist > 19712 and dist < 21248: circle = 6
    elif dist > 22784 and dist < 24320: circle = 7
    elif dist <= 1280: circle = -1
    elif dist >= 2816 and dist <= 4352: circle = -2
    elif dist >= 5888 and dist <= 7424: circle = -3
    elif dist >= 8960 and dist <= 10496: circle = -4
    elif dist >= 12032 and dist <= 13568: circle = -5
    elif dist >= 15104 and dist <= 16640: circle = -6
    elif dist >= 18176 and dist <= 19712: circle = -7
    elif dist >= 21248 and dist <= 22784: circle = -8
    elif dist >= 24320: circle = -9
    return circle
    
def locate_any(x, y, m):
    circle = loccircle(x, y)
    return circle

def facing(x, y, deg, inner_circle_radius):
    d = vector_dist(x, y)
    r = inner_circle_radius
    theta = math.degrees(math.asin(r / d))
    phi = math.degrees(math.asin(y / d))
    if deg >= (phi - theta) and deg <= (phi + theta):
        return 1
    else:
        return 0

def leave():
    root.destroy()
    status = False

def explosive_extraction(x, y, circle):
    global status, root
    list = [x,y]
    status = True
    for i in CIR[circle]:
        distance = vector_dist(i[0] - x, i[1] - y)
        #2217 is an approx. value of  minimum distance between stronghold in circle #0
        #all are 1280 blocks from center and forms a 60-60-60 triangle
        #strongholds in the same circle shouldn't be closer than this value in theory
        if distance < 2217 or len(CIR[circle]) >= nlist[circle]:
            if len(CIR[circle]) >= nlist[circle]:
                txt = "The stronghold in this circle has been fully discovered."
            #elif distance > 300:
            #    txt = "Locator malfunction occured. Please re-enter your data."
            else:
                txt = "Stronghold (%d,%d) has already been located." %(i[0],i[1]*(-1))
            root = tk.Tk()
            root.geometry("450x65")
            msg = tk.Label(root, font=('Arial',12,'bold'), text=txt)
            #msg.configure(anchor="center")
            #msg.grid(row=0, column=1)
            closebutton = tk.Button(root, text='OK', font=('Arial',12,'bold'), command=leave)
            #closebutton.grid(row=1, column=1)

            msg.pack()
            closebutton.pack()
            root.mainloop()
            status = False
            return status
    CIR[circle].append(list)
    return status

def sort(circle):
    degs = []
    NCIR = [[[] for x in range(36)] for y in range(8)]
    counter = 0
    for i in CIR[circle]:
        degree = math.degree(math.atan(i[1] / i[0]))
        if i[1] < 0:
            degree += 180
        degs.append([degree, counter, i[0], i[1]])
        counter += 1
    degs.sort(key = lambda d:d[0])
    for j in degs:
        NCIR[circle].insert(j[1], [j[2], j[3]])
    CIR = NCIR
    return CIR

# ======================================================================================================== #


'''
hold = keyin()
hold = locate_first(hold[0], hold[1], hold[2], hold[3], hold[4], hold[5])
#print(hold[0], hold[1])
'''

'''
x, z = loc_range()
draw_final(x, z)
'''


