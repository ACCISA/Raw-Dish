import cv2 as cv
import numpy as np
  
  
# 0 for webcam feed ; add "path to file"
# for detection in video file
capture = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")
Last_printed = "Straight" # this will be sued later on to not repeat tilting
while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    x, y, w, h = 0, 0, 0, 0
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame, (x + int(w * 0.5), y +
                          int(h * 0.5)), 4, (0, 255, 0), -1)
    eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)
    index = 0
    y_eye_list=[]#keeps the y values of the different eyes found to be sorted later
    eye_list=[] #list of eyes found
    eye_1 = [0, 0, 0, 0]
    eye_2 = [0, 0, 0, 0]
    eye_3 = [0, 0, 0, 0]
    eye_4 = [0, 0, 0, 0]
    for (ex, ey, ew, eh) in eyes:
        
        if index == 0:
            eye_1 = [ex, ey, ew, eh]
            y_eye_list.append(eye_1[1])
            eye_list.append(eye_1)
        elif index == 1:
            eye_2 = [ex, ey, ew, eh]
            y_eye_list.append(eye_2[1])
            eye_list.append(eye_2)
        elif index == 2:
            eye_3 = [ex, ey, ew, eh]
            y_eye_list.append(eye_3[1])
            eye_list.append(eye_3)
        elif index == 3:
            eye_4 = [ex, ey, ew, eh]
            y_eye_list.append(eye_4[1])
            eye_list.append(eye_4)
        
        cv.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey),
                     (ex + ew, ey + eh), (0, 0, 255), 2)
        index = index + 1
    y_eye_list.sort(reverse=False)
    

    real_eyes=[]
    
    r_eye_number=0
    for eye in eye_list:#the 2 highest eyes are considered real eyes. This is because fake eyes are often found lower in the face region.
            #it would be better to make the eyes closest to the eyebrows, for example, the real eyes
        
        if eye[1]==y_eye_list[r_eye_number]:
            real_eyes.append(eye)
            r_eye_number+=1
        if r_eye_number==2:
            break
    
    if len(real_eyes)==2:
        real_eye1=real_eyes[0]
        real_eye2=real_eyes[1]

    elif len(real_eyes)==1:
        real_eye1=real_eyes[0]
        real_eye2=[None, None, None, None]

    elif len(real_eyes)==0:
        real_eye1=[None, None, None, None]
        real_eye2=[None, None, None, None]
    
    
    if (real_eye1[0] is not None) and (real_eye2[0] is not None):
        if real_eye1[0] < real_eye2[0]:
            left_eye = real_eye1
            right_eye = real_eye2
        else:
            left_eye = real_eye2
            right_eye = real_eye1
        left_eye_center = (
            int(left_eye[0] + (left_eye[2] / 2)), 
          int(left_eye[1] + (left_eye[3] / 2)))
          
        right_eye_center = (
            int(right_eye[0] + (right_eye[2] / 2)),
          int(right_eye[1] + (right_eye[3] / 2)))
          
        left_eye_x = left_eye_center[0]
        left_eye_y = left_eye_center[1]
        right_eye_x = right_eye_center[0]
        right_eye_y = right_eye_center[1]
  
        delta_x = right_eye_x - left_eye_x
        delta_y = right_eye_y - left_eye_y
          
        # Slope of line formula
        if delta_x==0:
            angle=360
        else:
            angle = np.arctan(delta_y / delta_x)  
          
        # Converting radians to degrees
        angle = (angle * 180) / np.pi  
  
        # Provided a margin of error of 10 degrees
        # (i.e, if the face tilts more than 10 degrees
        # on either side the program will classify as right or left tilt)
        
        if angle==360:
            cv.putText(frame, 'N/A',
                       (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 0), 2, cv.LINE_4)
        elif angle > 10:
            cv.putText(frame, 'Left TILT :' + str(int(angle))+' degrees',
                       (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 0), 2, cv.LINE_4)
            if Last_printed == "Straight":
                print("Left")
                Last_printed="Left"
        elif angle < -10:
            cv.putText(frame, 'RIGHT TILT :' + str(int(angle))+' degrees',
                       (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, 
                       (0, 0, 0), 2, cv.LINE_4)
            if Last_printed == "Straight":
                print("Right")
                Last_printed="Right"
        else:
            cv.putText(frame, 'STRAIGHT :', (20, 30),
                       cv.FONT_HERSHEY_SIMPLEX, 1, 
                       (0, 0, 0), 2, cv.LINE_4)
            Last_printed="Straight"
            
  
    cv.imshow('Frame', frame)
  
    if cv.waitKey(1) & 0xFF == 27:
        break
capture.release()
cv.destroyAllWindows()