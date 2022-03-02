import cv2
from base64 import b64decode, b64encode
import numpy as np


def img_encode(img):
    success,img_data =  cv2.imencode(".png",img)
    if success:
        joinImg = ",".join(["data:image/png;base64",b64encode(img_data).decode("ascii")])
        return joinImg

def img_decode(enData):
    _,b64_data = enData.split(",")
    img = cv2.imdecode(
        np.frombuffer(
            b64decode(b64_data),
            dtype=np.uint8
        ),
        cv2.IMREAD_ANYCOLOR
    )
    return img

def imgToGray(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img_gray




