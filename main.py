import main_functionlib
import st_menu_input
import st_menu_display
import main_menu_display
import ec_menu_input
import ec_menu_display
import st_introduction_display

main_Loc = {}
function = (main_menu_display.main_menu())
resloc = []
circle = 0


#exit()

if function == 1:
    st_introduction_display.st_introduction_display()
    while True:
        locx, locy = 0,0
        st_menu_input.create()
        main_Loc = st_menu_input.st_menu_input()

        if st_menu_input.typecheck == 1:
            resloc = main_functionlib.locate_first(float(main_Loc['XI']), float(main_Loc['ZI']), float(main_Loc['DEGI']), float(main_Loc['XII']), float(main_Loc['ZII']), float(main_Loc['DEGII']))
            locx = resloc[0]
            locy = resloc[1]
            m = locy / locx
            circle = st_menu_input.lockcircle
            main_functionlib.LIN.insert(circle, main_functionlib.division(m, circle))

        elif st_menu_input.typecheck == 2:
            tempx = float(main_Loc['XI']) * -1
            tempy = float(main_Loc['ZI'])
            deg = main_functionlib.change_degree(float(main_Loc['DEGI']))
            m = tempy / tempx
            circle = st_menu_input.lockcircle
            finloc = main_functionlib.matchmaking(tempx, tempy, deg, main_functionlib.LIN[circle])
            locx = finloc[0]
            locy = finloc[1]
        status = main_functionlib.explosive_extraction(locx, locy, circle)
        if status:
            st_menu_display.st_menu_display(circle)
            st_menu_display.reset()

if function == 2:
    ec_menu_input.create()
    main_Loc = ec_menu_input.st_menu_function2_input()
    ec_menu_display.fuction2_display(main_Loc)





    
    