import numpy as np
import cv2

video = cv2.VideoCapture("v1.mp4")

img = cv2.imread("back.jpg")


# ret , frame = video.read()



image = cv2.resize(img,(640,480))


u_green = np.array([104,153,70])
l_green = np.array([30,30,0])
# #highlighted green to white


# #and operation between mask and frame
# #syntax (dest,src,mask)




while(True):
    ret, frame = video.read()
    frame = cv2.resize(frame,(640,480))
    mask = cv2.inRange(frame,l_green,u_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.destroyAllWindows()
        break
