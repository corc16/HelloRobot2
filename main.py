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

p = Piggy()
p.cha_cha()
p.onward()