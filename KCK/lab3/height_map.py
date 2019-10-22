import matplotlib.pyplot as plt
import numpy as np

def plot(data):
  img = plt.imshow(data)
  plt.savefig('height_map.png')

def read_data(file_path):
  width = 0
  height = 0
  distance = 0
  data = np.array([])

  with open(file_path, 'r') as f:
    idx = 0
    for line in f.readlines():
      if idx == 0:
        line = line.split(' ')
        width = int(line[0])
        height = int(line[1])
        distance = int(line[2][:-1])
      else:
        line = line.split(' ')
        line[-1] = line[-1][:-1]
        # data.append(line)
        line = np.array(line)
        data = np.append(data, line, axis=0)

      idx += 1

  return (width, height, distance, data)


def main():
  width, height, distance, data = read_data('big.dem')
  print(data)
  plot(data)

if __name__ == '__main__':
  main()
