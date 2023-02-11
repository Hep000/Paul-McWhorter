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

def nothing(x):
    pass

cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal','nanoCam',25,dispW,nothing)
cv2.createTrackbar('yVal','nanoCam',25,dispH,nothing)
cv2.createTrackbar('width','nanoCam',25,dispH,nothing)
cv2.createTrackbar('height','nanoCam',25,dispH,nothing)

while True:
    ret, frame=cam.read()
    
    xVal=cv2.getTrackbarPos('xVal','nanoCam')
    yVal=cv2.getTrackbarPos('yVal','nanoCam')
    width=cv2.getTrackbarPos('width','nanoCam')
    height=cv2.getTrackbarPos('height','nanoCam')
    cv2.rectangle(frame,(xVal,yVal),(xVal+width,yVal+height),(255,0,0),3)
    #cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1)


    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
