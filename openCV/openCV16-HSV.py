import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueLow' ,'Trackbars', 50,179,nothing)
cv2.createTrackbar('hueHigh','Trackbars',100,179,nothing)
cv2.createTrackbar('hue2Low' ,'Trackbars', 50,179,nothing)
cv2.createTrackbar('hue2High','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow' ,'Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow' ,'Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)


dispW=640 #1280
dispH=480 #960
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret, frame=cam.read()
    #frame=cv2.imread('smarties.png')
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

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
    cv2.moveWindow('FGMaskComp',0,430)

    FG=cv2.bitwise_and(frame,frame,mask=FGMaskComp)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',480,0)

    BGMask=cv2.bitwise_not(FGMaskComp)
    cv2.imshow('BGMask',BGMask)
    cv2.moveWindow('BGMask',480,430)

    BG=cv2.cvtColor(BGMask,cv2.COLOR_GRAY2BGR)

    final=cv2.add(FG,BG)
    cv2.imshow('final',final)
    cv2.moveWindow('final',900,0)


    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
