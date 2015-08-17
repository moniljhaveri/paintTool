import cv2 
import cv
import time 
import numpy as np

time1 = time.strftime("%H:%M:%S") 
print time1 
drawing = False 
ix,iy = -1, -1
paintBrush = 1

def nothing(x): 
    pass 

def paint_Brush(event, x, y, flags, param): 
    global ix, iy, drawing, paintBrush, r, g, b 
    paintBrush = cv2.getTrackbarPos('Paint Brush', name)     
    r = cv2.getTrackbarPos('Red', name)     
    g = cv2.getTrackbarPos('Green', name)     
    b = cv2.getTrackbarPos('Blue', name)

    if event == cv2.EVENT_LBUTTONDOWN: 
        drawing = True 
        ix,iy = x,y 
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing == True:  
            cv2.line(img,(ix,iy), (x,y), (b,g,r), paintBrush) 
            ix,iy = x,y                                 #This will set the paintbrush to the new point 
    elif event == cv2.EVENT_LBUTTONUP: 
            drawing = False


img = np.zeros((512,512,3), np.uint8) 
name = "image2" 
cv2.namedWindow(name) 
cv2.setMouseCallback(name, paint_Brush) 

cv2.createTrackbar('Paint Brush', name, 0, 5, nothing) 
cv2.createTrackbar('Green', name, 0, 255, nothing) 
cv2.createTrackbar('Red', name, 0, 255, nothing) 
cv2.createTrackbar('Blue', name, 0, 255, nothing) 

while(1): 
    cv2.imshow(name, img) 
    k = cv2.waitKey(1) & 0xFF 
    if k == 27: 
        break 
    elif k == ord('s'): 
        saveName = 'paint' + time1 + '.jpg'
        cv2.imwrite(saveName, img)
        break
cv2.destroyAllWindows()

