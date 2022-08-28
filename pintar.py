import numpy as np
import matplotlib.pyplot as plt
import sys
import math

from csv import reader

rng = np.random.RandomState()

def aptitud(c1):
  cr, cg, cb = c1
  gr, gc, gb = goal

  apt = math.sqrt( math.pow(cr - gr, 2) + (math.pow(cg - gc, 2)) + math.pow(cb - gb, 2) )
  return apt

def aptitud_rel(pop: np.array):
  ps = pop.apply_along_axis(aptitud, 1, pop)
  prels = ps / np.sum(ps)



class Population:
  def __init__(self, palette: np.ndarray, size: int) -> None:
    self.n = size
    self.k = len(palette)

def get_colors() -> np.ndarray:
  file = open("./colores.csv")
  csvreader = reader(file)

  colores = []
  for row in csvreader:
    r, g, b = (int(x) for x in row)
    colores.append( (r, g, b) )
  return np.array(colores, dtype=np.uint8)
  
def show_color(color: np.ndarray):
  im = color.reshape(1, 1, 3)
  fig = plt.figure(figsize=(3,3))
  ax = fig.add_subplot(111)
  ax.axis("off")
  ax.imshow(im)
  plt.show()


def main():
  global palette, goal
  palette = get_colors()
  print(palette)
  goal = np.array([int(x) for x in sys.argv[1].split(',')], dtype=np.uint8)

  a = rng.randint(0, 256, size=(10))

  show_color(goal)


if __name__ == "__main__":
  main()
