import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
import random
from datetime import datetime

def main():
  # picks = [random.randint(0, 21) for i in range(6)]
  picks = [0, 1, 2, 3, 4, 5]
  filenames = list()
  for pick in picks:
    filename = ''
    if pick < 10:
      filename = f'photos/samolot0{pick}.jpg'
    else:
      filename = f'photos/samolot{pick}.jpg'
    filenames.append(filename)

  for idx, image in enumerate(filenames):
    img = cv2.imread(image)
    img = imutils.resize(img, height=400)
    ax = plt.subplot(3, 2, idx + 1)
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_WRAP)
    img = cv2.Canny(gray, 75, 100)

    # img = cv.resize(img, (300,200))
    # edges = cv.Canny(img, 85, 100)
    plt.imshow(img, cmap='gray')
    # plt.axis('off')
    # ax.set_aspect('equal')
  
  plt.subplots_adjust(wspace=0, hspace=0)
  
  plt.show()

if __name__ == '__main__':
  random.seed(datetime.now())
  main()
