import matplotlib.pyplot as plt
import numpy as np

def hsv2rgb(row):
    h, s, v = row
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    r = 0
    g = 0
    b = 0

    if h >= 0 and h < 60:
        r = c
        g = x
        b = 0
    if h >= 60 and h < 120:
        r = x
        g = c
        b = 0
    if h >= 120 and h < 180:
        r = 0
        g = c
        b = x
    if h >= 180 and h < 240:
        r = 0
        g = x
        b = c
    if h >= 240 and h < 300:
        r = x
        g = 0
        b = c
    if h >= 300 and h < 360:
        r = c
        g = 0
        b = x     

    r, g, b = (r + m, g + m, b + m)

    return (r, g, b)

def read_data(file_path):
  width = 0
  height = 0
  distance = 0

  with open(file_path, 'r') as f:
    width, height, distance = [int(x) for x in f.readline().split()]
    
  data = np.loadtxt(fname='big.dem', dtype=float, skiprows=1)

  return (width, height, distance, data)


def main():
  width, height, distance, data = read_data('big.dem')

  data_min = np.amin(data)
  data_max = np.amax(data)

  hue_norm = data - data_min
  hue_norm = hue_norm * 120 / data_max
  hue_norm = 120 - hue_norm

  hmap = np.zeros((width, height, 3), dtype=float)

  s = 0.7
  v = 0.7

  for i in range(len(hue_norm)):
    for j in range(len(hue_norm[i])):
      hmap[i][j] = hsv2rgb([hue_norm[i][j], s, v])
  
  plt.imshow(hmap)
  plt.show()

if __name__ == '__main__':
  main()
