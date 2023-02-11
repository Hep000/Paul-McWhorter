from adafruit_servokit import ServoKit
myKit=ServoKit(channels=16)
panAngle=90
tiltAngle=90
myKit.servo[0].angle=panAngle
myKit.servo[1].angle=tiltAngle

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1550,0)

cv2.createTrackbar('hueLow' ,'Trackbars', 80,179,nothing)
cv2.createTrackbar('hueHigh','Trackbars',158,179,nothing)
cv2.createTrackbar('hue2Low' ,'Trackbars', 50,179,nothing)
cv2.createTrackbar('hue2High','Trackbars',10,179,nothing)
cv2.createTrackbar('satLow' ,'Trackbars',77,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',222,255,nothing)
cv2.createTrackbar('valLow' ,'Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)


dispW=640 #1280
dispH=480 #960
dispCentreX = dispW/2
dispCentreY = dispH/2
angleOfViewH = 78 # degrees
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret, frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow =cv2.getTrackbarPos('hueLow' ,'Trackbars')
    hueHigh=cv2.getTrackbarPos('hueHigh','Trackbars')
    hue2Low =cv2.getTrackbarPos('hue2Low' ,'Trackbars')
    hue2High=cv2.getTrackbarPos('hue2High','Trackbars')
    satLow =cv2.getTrackbarPos('satLow' ,'Trackbars')
    satHigh=cv2.getTrackbarPos('satHigh','Trackbars')
    valLow =cv2.getTrackbarPos('valLow' ,'Trackbars')
    valHigh=cv2.getTrackbarPos('valHigh','Trackbars')
    l_b=np.array([hueLow ,satLow ,valLow ])
    u_b=np.array([hueHigh,satHigh,valHigh])
    l_b2=np.array([hue2Low ,satLow ,valLow ])
    u_b2=np.array([hue2High,satHigh,valHigh])

    FGMask=cv2.inRange(hsv,l_b,u_b)
    FGMask2=cv2.inRange(hsv,l_b2,u_b2)
    FGMaskComp=cv2.add(FGMask,FGMask2)
    cv2.imshow('FGMaskComp',FGMaskComp)
    cv2.moveWindow('FGMaskComp',0,530)

    contours,heirachy=cv2.findContours(FGMaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contoursSorted = sorted(contours, key=lambda x: cv2.contourArea(x),reverse=True)
    count=0
    for cnt in contoursSorted:
        count=count+1
    if count>=1:
        cnt=contoursSorted[0]
        area=cv2.contourArea(cnt)
        if area>=50:
            (x,y,w,h)=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            centreX = x+w/2
            centreY = y+h/2
            moveX = dispCentreX - centreX
            moveY = dispCentreY - centreY
            panAngle =panAngle  + moveX/50
            tiltAngle=tiltAngle - moveY/50
            panAngle =min(180,max(0,panAngle))
            tiltAngle=min(180,max(0,tiltAngle))
            myKit.servo[0].angle=panAngle
            myKit.servo[1].angle=tiltAngle


    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


