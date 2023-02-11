import cv2
dispW=640
dispH=480

def nothing(x):
    pass
cv2.namedWindow('img')
cv2.createTrackbar('Blend','img',50,100,nothing)

logo=cv2.imread('pl.jpg')
logo=cv2.resize(logo,(100,100))
cv2.imshow('logo',logo)
cv2.moveWindow('logo',700,0)

logoGray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
cv2.imshow('logoGray',logoGray)
cv2.moveWindow('logoGray',800,0)

_,BGMask=cv2.threshold(logoGray,230,255,cv2.THRESH_BINARY)
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',900,9)

FGMask=cv2.bitwise_not(BGMask)
FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',1000,0)

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

x=200
y=100
l=100
dx=2
dy=2

while True:
    ret, frame=cam.read()

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)

    img=frame

    roi=img[y:(y+l),x:(x+l),]
    cv2.imshow('roi',roi)
    cv2.moveWindow('roi',700,150)

    roiBG=cv2.bitwise_and(roi,roi,mask=BGMask)
    cv2.imshow('roiBG',roiBG)
    cv2.moveWindow('roiBG',800,150)

    roiFG=cv2.bitwise_and(logo,logo,mask=FGMask)
    cv2.imshow('roiFG',roiFG)
    cv2.moveWindow('roiFG',900,150)

    roiComb=cv2.add(roiBG,roiFG)
    cv2.imshow('roiComb',roiComb)
    cv2.moveWindow('roiComb',1000,150)

    w1=cv2.getTrackbarPos('Blend','img')/100
    w2=1-w1
    roiBlend=cv2.addWeighted(roiComb,w1,roi,w2,0)
    cv2.imshow('roiBlend',roiBlend)
    cv2.moveWindow('roiBlend',1100,150)

    img[y:(y+l),x:(x+l),]=roiBlend
    cv2.imshow('img',img)
    cv2.moveWindow('img',0,560)

    if x<=0 or x+l>=dispW:
        dx=-dx
    if y<=0 or y+l>=dispH:
        dy=-dy
    x=x+dx
    y=y+dy

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
