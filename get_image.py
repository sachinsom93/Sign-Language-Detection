"""
    Module for capturing data of all signs.
"""

# Import Dependencies
import numpy as np
import cv2 as cv
from pathlib import Path


def get_image():
    """
    Function to get image from webcam and create
    DATASET images for all signs.
    """
    Class = '3' # Change this to respective sign

    # Define dataset path and create directory
    Path('DATASET/'+Class).mkdir(parents=True, exist_ok=True)

    # Capture video frame
    cap = cv.VideoCapture(0)

    # Check if webcam is on or not
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Iterator
    i = 0
    while True:

        # read image from web cam
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        i+= 1
        if i % 5==0:
            cv.imwrite('DATASET/'+Class+'/'+str(i)+'.png',frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q') or i > 500:
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
   get_image()