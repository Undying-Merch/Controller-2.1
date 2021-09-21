from grovepi import *
from grove_rgb_lcd import *

setRGB(240,248,250)

btn = 4
drejeting = 2
i = 0

def location()
    x = 0
    rooms = ["MU8-15", "MU8-R22", "MU8-R24", "MU8-R25", "MU8-R27", "MU8-R30", "MU8-R31", "MU8-R32", "MU8-R33", "MU8-R44" ]
    i = analogRead(drejeting)
    btn_status = digitalRead(btn)
    if i > 100:
        setText_noreresh(rooms[0])
    else:
        setText_norefres(rooms[int(i/100)])

    if btn_status:
        if i <= 100:
            x = 0
        elif i >100 or i <=200:
            x = 1
        elif i >200 or i <=300:
            x = 2

        return rooms[x]

while True:
    try:
        room = location()
        break

    except KeyboardInterrupt:
        break