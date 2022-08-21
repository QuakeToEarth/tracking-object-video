
import cv2
import time
import math
goalX = 530
goalY = 300
video = cv2.VideoCapture('bb3.mp4')
tracker = cv2.TrackerCSRT_create()
ret,image = video.read()
bBox = cv2.selectROI('tracking...',image,False)
tracker.init(image,bBox)
def drawBox(image,bBox):
    x,y,w,h = int(bBox[0]),int(bBox[1]),int(bBox[2]),int(bBox[3])
    cv2.rectangle(image,(x,y),(x+w, y+h),(156,233,252),3,1)

def goTracking(image,bBox):
     x,y,w,h = int(bBox[0]),int(bBox[1]),int(bBox[2]),int(bBox[3])
     c1 = x+ int(w/2)
     c2 = y+ int(h/2)
     cv2.circle(image,(c1,c2),2,(156,233,252),3)
     cv2.circle(image,(goalX,goalY),2,(156,233,252),3)
     distance = math.sqrt(((c1-goalX)**2) + (c2-goalY)**2)
     if (distance < 40):
         cv2.putText(image,'🎉GOAL ACHIEVED!🎉',(350,90),cv2.FONT_HERSHEY_COMPLEX,0.7,(156,233,252))
while True:
    ret,image = video.read()
    SUCCESS,bBox = tracker.update(image)
    if (SUCCESS == True):
        drawBox(image, bBox)
    goTracking(image,bBox)
    cv2.imshow('result',image)
    if cv2.waitKey(1) == 32:
        break

video.release()
cv2.destroyAllWindows()