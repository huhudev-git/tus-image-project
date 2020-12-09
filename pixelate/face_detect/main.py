from typing import List

import cv2
import numpy as np
from pixelate.models.image import Image
from pixelate.models.position import Position

face_cascade = cv2.CascadeClassifier('pixelate/face_detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('pixelate/face_detect/haarcascade_eye.xml')


def face_detect(image: Image) -> List[Position]:
    image_stream = image.get_from_io()
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)

    result = []
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        p = Position(x, y, x+w, y+h)
        result.append(p)
    return result


def eye_detect(image: Image) -> List[Position]:
    image_stream = image.get_from_io()
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)

    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)

    result = []

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            p = Position(ex, ey, ex+ew, ey+eh)
            result.append(p)
    return result
