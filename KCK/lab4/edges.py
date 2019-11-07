import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
import random


def main():
    plt.ion()

    picks = [2, 17, 19, 7, 1, 5, 4, 10, 12, 11, 18, 0, 3, 6, 9, 8, 14, 16]
    filenames = list()
    for pick in picks:
        filename = ''
        if pick < 10:
            filename = f'photos/samolot0{pick}.jpg'
        else:
            filename = f'photos/samolot{pick}.jpg'
        filenames.append(filename)

    for image in filenames:
        img = cv2.imread(image)
        img = imutils.resize(img, height=400)
        og_img = img.copy()
        gray = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_WRAP)
        img = cv2.Canny(gray, 75, 100)
        threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 3)
        threshold = cv2.dilate(threshold, None, iterations=8)
        contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        for x in contours:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            cv2.drawContours(og_img, [x], -1, color, 2)
            
        plt.imshow(og_img)
        plt.show()
        _ = input('Press enter')
        plt.close()


if __name__ == '__main__':
    main()
