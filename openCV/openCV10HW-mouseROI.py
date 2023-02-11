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

x1=0
y1=0
x2=0
y2=0
def click(event,x,y,flags,params):
    global x1
    global y1
    global x2
    global y2
    evt=event
    if evt==cv2.EVENT_LBUTTONDOWN:
        x1=x
        y1=y
    if evt==cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y

cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)

while True:
    ret, frame=cam.read()
    cv2.imshow('nanoCam',frame)
    if x1<x2 and y1<y2:
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('ROI',roi)
    cv2.moveWindow('nanoCam',0,0)
    cv2.moveWindow('ROI',0,dispH+60)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
