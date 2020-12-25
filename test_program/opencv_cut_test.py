import cv2
import numpy as numpy
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(gray, face)
        # [36,,37,39, 40],[42, 43, 45, 46]
        # Right eye
        r_x1 = landmarks.part(36).x
        # r_y1 = landmarks.part(36).y
        # r_x2 = landmarks.part(37).x
        r_y2 = landmarks.part(37).y
        r_x3 = landmarks.part(39).x
        # r_y3 = landmarks.part(39).y
        # r_x4 = landmarks.part(40).x
        r_y4 = landmarks.part(40).y

        frame_trim = frame[r_y2:r_y4, r_x1:r_x3]
        # cv2.circle(frame_trim, (r_x1, r_y2), 2, (255, 0, 0), -1)
        # cv2.circle(frame_trim, (r_x3, r_y4), 2, (255, 0, 0), -1)



    cv2.imshow("Frame",frame_trim)
    
    key = cv2.waitKey(1)
    if key ==27:
        break