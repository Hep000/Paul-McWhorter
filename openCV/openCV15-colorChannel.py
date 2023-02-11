import cv2
import numpy as np
dispW=640 #1280
dispH=480 #960
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

blank=np.zeros([dispH,dispW,1],np.uint8)
#blank[0:240,0:320]=125
while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(frame[50,45,1])
    #print(frame.shape)
    #print(frame.size)
    b,g,r=cv2.split(frame)

    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))
    r[:]=0.9*r[:]
    merge=cv2.merge((b,g,r))

    cv2.imshow('b',blue)
    cv2.moveWindow('b',700,0)
    cv2.imshow('g',green)
    cv2.moveWindow('g',0,500)
    cv2.imshow('r',red)
    cv2.moveWindow('r',700,500)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    cv2.imshow('merge',merge)
    cv2.moveWindow('merge',1400,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
