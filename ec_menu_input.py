import tkinter as tk
import math

def create():
    global root2
    root2 = tk.Tk()
    root2.title('player coordinate')
    global PlayerX, PlayerY
    PlayerX, PlayerY= tk.StringVar(), tk.StringVar()

def create_error_reporter():
    global root3
    root3 = tk.Tk()
    root3.title('Error')
    global error
    error = tk.StringVar()

def conf_reporter():
    root3.destroy()

def conf():
    global function2_Loc
    function2_Loc = {'player_x': PlayerX.get(), 'player_y': PlayerY.get()}
    if math.sqrt(pow(abs(int(function2_Loc['player_x'])), 2) + pow(abs(int(function2_Loc['player_y'])), 2)) < 1000:
        create_error_reporter()
        errorlabel = tk.Label(root3, text='Too close to the main island')
        errorlabel.grid(row=1, column=0)
        confbutton = tk.Button(root3, text='Confirm', command=conf_reporter)
        confbutton.grid(row=2, column=3)
    else:
        root2.destroy()


def st_menu_function2_input():
    PlayerXlabel = tk.Label(root2, text='Player x coordinate:')
    PlayerXlabel.grid(row=0, column=0)
    PlayerXentry = tk.Entry(root2, textvariable=PlayerX)
    PlayerXentry.grid(row=0, column=1)
    PlayerYlabel = tk.Label(root2, text='Player z coordinate:')
    PlayerYlabel.grid(row=1, column=0)
    PlayerYentry = tk.Entry(root2, textvariable=PlayerY)
    PlayerYentry.grid(row=1, column=1)

    confbutton = tk.Button(root2, text='Confirm', command=conf)
    confbutton.grid(row=2, column=3)

    root2.mainloop()
    return function2_Loc
