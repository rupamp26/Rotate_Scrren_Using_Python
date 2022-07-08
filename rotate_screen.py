import rotatescreen
import time
screen = rotatescreen.get_primary_display()
screen.rotate_to(0) #enter the angle you want to rotate, only wroks on 0, 90, 180, or 270 degrees.


for i in  range(9):
        time.sleep(1)
        screen.rotate_to(i*90 % 360)