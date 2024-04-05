import tkinter as tk
import st_menu_display
import main_functionlib
#import sys

CIR = main_functionlib.CIR
typecheck = 0

def create():
    global root
    root = tk.Tk()
    root.title('Eye of ender locator')
    global XI, XII, YI, YII, DI, DII
    XI, XII, YI, YII, DI, DII = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

def newpoint():
    global output
    #TYPE': 1,
    output = {'XI': XI.get(), 'ZI': YI.get(), 'DEGI': DI.get(), 'XII': XII.get(), 'ZII': YII.get(), 'DEGII': DII.get()}
    root.destroy()
def oldpoint():
    global output
    #TYPE': 2,
    output = {'XI': XI.get(), 'ZI': YI.get(), 'DEGI': DI.get()}
    root.destroy()

def twopoint(btna, btnb):
    btna.destroy()
    btnb.destroy()
    global typecheck, output
    XIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='X2:')
    XIIlabel.grid(row=1, column=0)
    XIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=XII)
    XIIentry.grid(row=1, column=1)
    YIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='Z2:')
    YIIlabel.grid(row=1, column=2)
    YIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=YII)
    YIIentry.grid(row=1, column=3)
    DIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='DEG2:')
    DIIlabel.grid(row=1, column=4)
    DIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=DII)
    DIIentry.grid(row=1, column=5)
    calcbutton = tk.Button(root, text='Calculate', font=('Arial',18,'bold'), command=newpoint)
    calcbutton.grid(row=0, column=6)
    calcbutton.config(height = 1, width = 10)
    typecheck = 1

def onepoint(btna, btnb):
    btna.destroy()
    btnb.destroy()
    global typecheck, output
    #loc = main_functionlib.matchmaking(x, y, deg, main_functionlib.LIN[lockcircle])
    #output = {'XI': loc[0], 'ZI': loc[1], 'DEGI': deg}
    #calcbutton = tk.Button(root, text='Calculate', font=('Arial',20,'bold'), command=oldpoint)
    #calcbutton.grid(row=1, column=6)
    #calcbutton.config(height = 1, width = 10)
    oldpoint()
    typecheck = 2
    root.destroy()


def conf(btn):
    
    global typecheck, function1_Loc, output, lockcircle, x, y, deg
    slabel = tk.Label(root, font=('Arial',18,'bold'), text='                      ')
    slabel.grid(row=0, column=6)
    btn.destroy()

    function1_Loc = {'XI': float(XI.get()), 'ZI': float(YI.get()), 'DEGI': float(DI.get())}
    #root.destroy()
    x = function1_Loc['XI']
    y = function1_Loc['ZI']
    deg = function1_Loc['DEGI']
    circle = main_functionlib.loccircle(x, y)
    lockcircle = 0
    #-1 special case handle
    #lockcircle(鎖定要塞所在圈數) = [circle(判定位置圈數)] + 1
    if circle == -1: lockcircle = 0
    elif circle < -1:
        rad = st_menu_display.outer_circle_rad[abs(circle) - 2] #inner circle
        bool = main_functionlib.facing(x, y, deg, rad)
        if bool == 1:
            lockcircle = abs(circle) - 2
        else:
            lockcircle = abs(circle) - 1
    else: lockcircle = circle
    #print(lockcircle)
    if CIR[lockcircle]==[]:
        temp = tk.Button(root, text=' ', font=('Arial',10,'bold'))
        twopoint(temp, temp)
    else:
        twop = tk.Button(root, text='locate with 2 points', font=('Arial',18,'bold'), command=lambda: twopoint(onep, twop))
        onep = tk.Button(root, text='locate with 1 point', font=('Arial',18,'bold'), command=lambda: onepoint(onep, twop))
        twop.grid(row=1, column=7)
        twop.config(height = 1, width = 15)
        onep.grid(row=1, column=6)
        onep.config(height = 1, width = 15)
    '''
    if calctype == 1:
        XIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='X2:')
        XIIlabel.grid(row=1, column=0)
        XIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=XII)
        XIIentry.grid(row=1, column=1)
        YIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='Y2:')
        YIIlabel.grid(row=1, column=2)
        YIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=YII)
        YIIentry.grid(row=1, column=3)
        DIIlabel = tk.Label(root, font=('Arial',18,'bold'), text='DEG2:')
        DIIlabel.grid(row=1, column=4)
        DIIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=DII)
        DIIentry.grid(row=1, column=5)
        calcbutton = tk.Button(root, text='Calculate', font=('Arial',18,'bold'), command=newpoint)
        calcbutton.grid(row=0, column=6)
        calcbutton.config(height = 1, width = 10)
        typecheck = 1
        #main_functionlib.LIN[lockcircle] = main_functionlib.division(m, lockcircle)
    elif calctype == 2:
        #m = (CIR[lockcircle][0][1]-y)/(CIR[lockcircle][0][0]-x)
        loc = main_functionlib.matchmaking(x, y, deg, main_functionlib.LIN[lockcircle])
        output = {'XI': loc[0], 'ZI': loc[1], 'DEGI': deg}
        calcbutton = tk.Button(root, text='Calculate', font=('Arial',20,'bold'), command=oldpoint)
        calcbutton.grid(row=1, column=6)
        calcbutton.config(height = 1, width = 10)
        typecheck = 2
    #button.destroy()
    '''



def st_menu_input():
    global output
    root.geometry("1350x500")

    XIlabel = tk.Label(root, font=('Arial',18,'bold'), text='X1:')
    XIlabel.grid(row=0, column=0)
    XIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=XI)
    XIentry.grid(row=0, column=1)
    YIlabel = tk.Label(root, font=('Arial',18,'bold'), text='Z1:')
    YIlabel.grid(row=0, column=2)
    YIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=YI)
    YIentry.grid(row=0, column=3)
    DIlabel = tk.Label(root, font=('Arial',18,'bold'), text='DEG1:')
    DIlabel.grid(row=0, column=4)
    DIentry = tk.Entry(root, font=('Arial',18,'bold'), textvariable=DI)
    DIentry.grid(row=0, column=5)
    confbutton = tk.Button(root, text='Confirm', font=('Arial',18,'bold'))
    
    confbutton.grid(row=0, column=6)
    confbutton.config(height = 1, width = 10, command=lambda: conf(confbutton))
    #confbutton.bind('', conf(confbutton))

    closebutton = tk.Button(root, text='Close program', font=('Arial',18,'bold'), command=exit)
    closebutton.grid(row=0, column=7)
    closebutton.config(height = 1, width = 15)
    

    root.mainloop()

    return output
