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

    # 瞳のトリミング処理
    # 右目：[36,,37,39, 40]　左目：[42, 43, 45, 46]
    # Right eye
    r_x1,r_y1 = landmarks.part(36).x,landmarks.part(36).y
    r_x2,r_y2 = landmarks.part(37).x,landmarks.part(37).y
    r_x3,r_y3 = landmarks.part(39).x,landmarks.part(39).y
    r_x4,r_y4 = landmarks.part(40).x,landmarks.part(40).y
    # Left eye
    l_x1,l_y1 = landmarks.part(42).x,landmarks.part(42).y
    l_x2,l_y2 = landmarks.part(43).x,landmarks.part(43).y
    l_x3,l_y3 = landmarks.part(45).x,landmarks.part(45).y
    l_x4,l_y4 = landmarks.part(46).x,landmarks.part(46).y

    r_frame_trim = frame[r_y2-3:r_y4+3, r_x1:r_x3]
    l_frame_trim = frame[l_y2-3:l_y4+3, l_x1:l_x3]

    # 拡大処理（5倍）
    r_height,r_width = r_frame_trim.shape[0],r_frame_trim.shape[1]
    l_height,l_width = l_frame_trim.shape[0],l_frame_trim.shape[1]
    r_frame_trim_resize = cv2.resize(r_frame_trim , (int(r_width*5.0), int(r_height*5.0)))
    l_frame_trim_resize = cv2.resize(l_frame_trim , (int(l_width*5.0), int(l_height*5.0)))

    # グレースケール処理
    r_frame_gray = cv2.cvtColor(r_frame_trim_resize, cv2.COLOR_BGR2GRAY)
    l_frame_gray = cv2.cvtColor(l_frame_trim_resize, cv2.COLOR_BGR2GRAY)

    # 2値化処理
    thresh = 200
    maxval = 255
    e_th,r_frame_black_white = cv2.threshold(r_frame_gray,thresh,maxval,cv2.THRESH_OTSU)
    l_th,l_frame_black_white = cv2.threshold(l_frame_gray,thresh,maxval,cv2.THRESH_OTSU)

    cv2.imshow("right eye",r_frame_black_white)
    cv2.imshow("left eye",l_frame_black_white)

    cv2.moveWindow('right eye', 100,20)
    cv2.moveWindow('left eye', 240,20)

    key = cv2.waitKey(1)
    if key ==27:
        break