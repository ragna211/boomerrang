import cv2
from moviepy.editor import *
from moviepy.Clip import *
from moviepy.video.VideoClip import *
import os
cap = cv2.VideoCapture(0)
list=[]
e=4
# Check if the webcam is opened correctly if not cap.isOpened():     raise IOError("Cannot open webcam")
while True:
    ret, frame = cap.read()
    #ret is boolean, to check if frame is coming or not 
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_AREA)
    e=e+1
    list.append(frame)
    cv2.imwrite(("C:/Users/HP/Desktop/spcl/play/%d.jpg"%e),frame)     
    cv2.imshow('Input', frame)
    c = cv2.waitKey(1)
    #video.write_videofile('test.avi', fps=30, codec='mpeg4')
    if c == 27:
    #27 is ASCII value of esc
         break
cap.release()
cv2.destroyAllWindows()
def convert_frames_to_video(pathIn,pathOut,fps):
    
    height, width, layers = list[1].shape
    size = (width,height)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(list)):
        # writing to a image array
        out.write(list[i])
    out.release()
    pathOut = 'C:/Users/HP/Desktop/rev_video.avi'
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in reversed(list):
        # writing to a image array
        
        out.write(i)
    out.release()
    pathOut = 'C:/Users/HP/Desktop/boom_video.avi'
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    k=0
    while k<1000:
     for i in range(len(list)):
        # writing to a image array
        out.write(list[i])
     k=k+len(list)
     for i in reversed(list):
        # writing to a image array
        
        out.write(i)
     k=k+len(list)
    out.release()    
 
pathIn= 'C:/Users/HP/Desktop/spcl/play/'
pathOut = 'C:/Users/HP/Desktop/video.avi'
fps = 25.0
convert_frames_to_video(pathIn, pathOut, fps)
