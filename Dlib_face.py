import cv2
import dlib
from imutils import face_utils
import time

cap = cv2.VideoCapture(0)
ptime = 0
while True:
    isTrue, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_detect = dlib.get_frontal_face_detector()

    rects = face_detect(gray, 1)

    for (i, rect) in enumerate(rects):
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        ctime = time.time()
        fps = 1/ (ctime-ptime)
        ptime = ctime
        cv2.putText(frame, f'FPS:{int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

