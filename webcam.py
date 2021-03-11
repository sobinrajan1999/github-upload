# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:24:46 2020

@author: rajan
"""

import cv2
import numpy as np
url='http://192.168.43.1:8080/video'
cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
