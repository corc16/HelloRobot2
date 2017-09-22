from gopigo import *
import time

class Piggy(object):

    def __init__(self):
        print("I AM ALIVE")

    def cha_cha(self):
        for x in range(8):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()
    def onward(self):
        time.sleep(2)
        fwd(2)
        stop()

    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15)  # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(selfs):
        """drive fwd, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)
    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)
p = Piggy()

def menu():
    while True:
        input = raw_input("Press 1 for Pulse \n Press 2 for Cruise \n Press 3 for Sweep")
        if "1" in input:
            p.pulse()
        elif "2" in input:
            p.cruise()
        elif "3" in input:
            p.servo_sweep()
try:
    menu()
except Exception as ee:
    from gopigo import *
    stop()

# p.cha_cha()
# p.onward()