screen idleScreen:
    imagebutton:
        idle "walking_feet.png"
        xpos 50
        ypos 800
        action Jump("chooseLocMove")

label chooseLocMove:
    if location == 'home':
        call screen homeLoc
    if location == 'lake':
        call screen lakeLoc
    if location == 'home':
        call screen homeLoc

screen homeLoc:
    if lakeVisited == True:
        imagebutton:
            idle "Arrows/left.png"
            xpos 50
            ypos 300
            action Jump("lakeSecond")
    else:
        imagebutton:
            idle "Arrows/left.png"
            xpos 50
            ypos 300
            action Jump("lake")

screen lakeLoc:
    imagebutton:
        idle "Arrows/right.png"
        xpos 1350
        ypos 300
        action Jump("homeSecond")