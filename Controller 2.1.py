from grovepi import *
from grove_rgb_lcd import *

setRGB(240,248,250)

drejeting = 2
i = 0

def location()
    buildings = 

while True:
    try:
        i = analogRead(drejeting)

        setText_norefresh(str(i))
    except KeyboardInterrupt:
        break