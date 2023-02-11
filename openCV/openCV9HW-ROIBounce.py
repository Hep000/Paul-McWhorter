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

x=300
y=50
w=100
h=80
dx=2
dy=2

while True:
    ret, frame=cam.read()
    roi=frame[y:(y+h),x:(x+w)].copy()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameGray=cv2.cvtColor(frameGray,cv2.COLOR_GRAY2BGR)
    frameGray[y:(y+h),x:(x+w)]=roi
    cv2.rectangle(frameGray,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('ROI',roi)
    cv2.imshow('nanoCam',frameGray)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('nanoCam',0,0)
    if x<=0 or x+w>=dispW:
        dx=-dx
    if y<=0 or y+h>=dispH:
        dy=-dy
    x=x+dx
    y=y+dy
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
