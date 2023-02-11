import cv2
import numpy as np
#import time as t
#seconds=t.time()
from datetime import datetime as dt

cam=cv2.VideoCapture(0)
nativeW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
nativeH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('/native width =',nativeW,'native height =',nativeH)
#cam.release()
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

dispW=int(nativeW/2)
dispH=480 #960

def nothing(x):
    pass
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1550,0)
cv2.createTrackbar('x','Trackbars',680,nativeW,nothing)
cv2.createTrackbar('y','Trackbars',120,nativeH,nothing)
cv2.createTrackbar('w','Trackbars',500,nativeW,nothing)
cv2.createTrackbar('h','Trackbars',500,nativeH,nothing)

lastX=0
lastY=0
lastW=2
lastH=2
lastROI=np.zeros((lastH,lastW,3),np.uint8)
lastROI=cv2.bitwise_not(lastROI)
imageNo=0
while True:
    ret, frame=cam.read()
    
    sameROI=frame[lastY:(lastY+lastH),lastX:(lastX+lastW)].copy()

    lastROIGray=cv2.cvtColor(lastROI,cv2.COLOR_BGR2GRAY)
    sameROIGray=cv2.cvtColor(sameROI,cv2.COLOR_BGR2GRAY)
    meanBrightnessLast=cv2.mean(lastROIGray)[0]
    _,sameROIMask=cv2.threshold(sameROIGray,meanBrightnessLast,255,cv2.THRESH_BINARY)
    _,lastROIMask=cv2.threshold(lastROIGray,meanBrightnessLast,255,cv2.THRESH_BINARY)
    diffROIMask=cv2.bitwise_xor(sameROIMask,lastROIMask)

    diff=cv2.mean(diffROIMask)[0]
    meanBrightnessSame=cv2.mean(sameROIGray)[0]
    if diff>=20 and meanBrightnessLast>=20 and meanBrightnessSame>=20:
        fileName='catImages/image' + str(imageNo) + '.jpg'
        now=dt.now()
        print(now.strftime("%Y%m%d %H:%M:%S"),"{:.3}".format(diff),"{:.4}".format(meanBrightnessLast),"{:.4}".format(meanBrightnessSame),fileName)
        cv2.imwrite(fileName,sameROI)
        imageNo=imageNo+1
    
    x=cv2.getTrackbarPos('x','Trackbars')
    y=cv2.getTrackbarPos('y','Trackbars')
    w=cv2.getTrackbarPos('w','Trackbars')
    h=cv2.getTrackbarPos('h','Trackbars')
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)

    lastROI=frame[y:(y+h),x:(x+w)].copy()
    lastX=x
    lastY=y
    lastW=w
    lastH=h

    cv2.imshow('nanoCam'    ,cv2.resize(frame,(dispW,dispH)))
#    cv2.imshow('lastROI'    ,lastROI    )
    cv2.imshow('sameROI'    ,sameROI    )
#    cv2.imshow('lastROIMask',lastROIMask)
#    cv2.imshow('sameROIMask',sameROIMask)
#    cv2.imshow('diffROIMask',diffROIMask)

    cv2.moveWindow('nanoCam'    ,  0,  0)
#    cv2.moveWindow('lastROI'    ,  0,530)
    cv2.moveWindow('sameROI'    ,  0,800)
#    cv2.moveWindow('lastROIMask',300,530)
#    cv2.moveWindow('sameROIMask',300,800)
#    cv2.moveWindow('diffROIMask',500,530)

    if imageNo>=10000:
        break
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
