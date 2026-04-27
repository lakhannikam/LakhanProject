import cv2
import os
import time

while True:
    print("Checking for green leaf...")

    os.system("rpicam-still -o temp.jpg")

    img = cv2.imread("temp.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

    lower_green = (35, 50, 50)
    upper_green = (85, 255, 255)

    mask = cv2.inRange(hsv, lower_green, upper_green)

    green = cv2.countNonZero(mask)
    total = img.size / 3
    percent = (green / total) * 100

    print("Green %:", percent)

    if percent > 30:
        print("Leaf detected! Capturing final image...")
        os.system("rpicam-still -o plant.jpg")
        break

    time.sleep(2)