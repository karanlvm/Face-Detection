import cv2
import dlib
from imutils import face_utils
import matplotlib.pyplot as plt

frame = cv2.imread('')
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Calling the function
face_detect = dlib.get_frontal_face_detector()
rectangle = face_detect(gray, 1)
# For the bounding box
for (i, rect) in enumerate(rectangle):
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
plt.imshow(frame)
plt.show()