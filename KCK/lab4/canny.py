import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime

def main():
  picks = [random.randint(0, 21) for i in range(6)]
  filenames = list()
  for pick in picks:
    filename = ''
    if pick < 10:
      filename = f'photos/samolot0{pick}.jpg'
    else:
      filename = f'photos/samolot{pick}.jpg'
    filenames.append(filename)

  for idx, image in enumerate(filenames):
    ax = plt.subplot(3, 2, idx + 1)
    img = cv.imread(image)
    img = cv.resize(img, (300,200))
    edges = cv.Canny(img, 85, 100)
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    ax.set_aspect('equal')
  
  plt.subplots_adjust(wspace=0, hspace=0)
  
  plt.show()

if __name__ == '__main__':
  random.seed(datetime.now())
  main()
