from adafruit_servokit import ServoKit
myKit=ServoKit(channels=16)
import time
while True:
    for i in range(0,181,90):
        print(i)
        myKit.servo[7].angle=i
        time.sleep(10)
