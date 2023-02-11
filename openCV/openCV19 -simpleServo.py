from adafruit_servokit import ServoKit
myKit=ServoKit(channels=16)
myKit.servo[0].angle=0
myKit.servo[1].angle=0
#myKit.servo[2].angle=120
#myKit.servo[3].angle=65
#myKit.servo[4].angle=160
#myKit.servo[5].angle=90
import time
while True:
    for i in range(0,1800,1):
        myKit.servo[0].angle=i/10
        myKit.servo[1].angle=i/10
        time.sleep(.0001)
    for i in range(1800,0,-1):
        myKit.servo[0].angle=i/10
        myKit.servo[1].angle=i/10
        time.sleep(.0001)

