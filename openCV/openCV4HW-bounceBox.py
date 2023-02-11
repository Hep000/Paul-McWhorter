import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

xTL=340
yTL=100
xBR=450
yBR=190
count=0
xD=1
yD=1
while True:
    ret, frame=cam.read()
    if xD>0 and xBR<dispW:
        xTL=xTL+xD
        xBR=xBR+xD
    if xD>0 and xBR==dispW:
        xD=-xD
    if xD<0 and xTL>0:
        xTL=xTL+xD
        xBR=xBR+xD
    if xD<0 and xTL==0:
        xD=-xD
    if yD>0 and yBR<dispH:
        yTL=yTL+yD
        yBR=yBR+yD
    if yD>0 and yBR==dispH:
        yD=-yD
    if yD<0 and yTL>0:
        yTL=yTL+yD
        yBR=yBR+yD
    if yD<0 and yTL==0:
        yD=-yD
    
    frame=cv2.rectangle(frame,(xTL,yTL),(xBR,yBR),(0,255,0),-1)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
