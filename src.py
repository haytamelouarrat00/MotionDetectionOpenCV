import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Constants
WAIT_KEY_INTERVAL = 50
THRESHOLD_VALUE = 20
MAX_THRESHOLD_VALUE = 255
THRESHOLD_TYPE = cv.THRESH_BINARY
DILATION_ITERATIONS = 3
MIN_CONTOUR_AREA = 900
ASCII_VALUE_OF_Q = ord('q')


def process_frame(frame1, frame2):
    diff = cv.absdiff(frame1, frame2)
    diff_gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(diff_gray, (5, 5), 0)
    _, thresh = cv.threshold(blur, THRESHOLD_VALUE, MAX_THRESHOLD_VALUE, THRESHOLD_TYPE)
    dilated = cv.dilate(thresh, None, iterations=DILATION_ITERATIONS)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours, frame2


def draw_contours(frame, contours):
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < MIN_CONTOUR_AREA:
            continue
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, "Status: {}".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv.drawContours(frame, contours, -1, (0, 255, 0), 2)


def motionDetection():
    cap = cv.VideoCapture("./samples/sample3.mp4")
    if not cap.isOpened():
        print("Error opening video file")
        return

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while ret:
        contours, frame2 = process_frame(frame1, frame2)
        draw_contours(frame1, contours)
        cv.imshow("Video", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv.waitKey(WAIT_KEY_INTERVAL) & 0xFF == ASCII_VALUE_OF_Q:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    motionDetection()
