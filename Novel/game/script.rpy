﻿#персонажи
define mc = Character('Вы', color="#c8ffc8")

#спрайты гг
image mc_neutral = "mc/mc_neutral.png"

#фоны
image house = "bg/house.jpg"
image room = "bg/room.jpg"
image lake = "bg/lake.jpg"


#старотовая позиция
label start:
    scene house
    "Вы прибываете в домик, который стал вашим новым жилищем. Все вокруг кажется каким-то давно забытым, как будто время здесь остановилось."

    show mc_neutral
    with dissolve
    mc "Давно я тут не был..."

    scene room
    show mc_neutral
    with dissolve
  
    "Старые фотографии, запах сырости, и телевизор, который кажется отображает лишь кусочек прошлого. Но вам нужно привыкнуть к этому новому месту."
    mc "Чем бы сперва заняться: убраться дома или проведать окресности?"

    menu:
        "Навести порядок.":
            jump clean
        "Прогуляться.":
            jump lake
    return


label clean:
    "Вы решаете разобраться с вещами в доме, чтобы сделать его более уютным. Начнем с того, чтобы найти место для своих вещей и, возможно, немного привести в порядок кухню."

    "В разработке."
    return


label lake:
    scene house
    show mc_neutral
    mc "Лучше схожу на прогулку, интересно, как многое тут успело измениться."
    "Вы решаете покинуть домик и прогуляться по окрестностям. Ведь, может быть, что-то интересное или полезное окажется неподалеку."
    "Вы выходите на улицу и направляетесь к парку с озером, который находится неподалеку от вашего нового дома"
    scene lake
    show mc_neutral

    "В разработке."
    return