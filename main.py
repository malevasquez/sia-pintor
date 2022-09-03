import numpy as np
import sys
import utils
import genetic


rng = np.random.RandomState()

def main():
  palette = utils.get_colors("./colores.csv")
  goal = np.array([int(x) for x in input("objective color: ").split(',')], dtype=np.uint8)
  method = genetic.SelectOption.ELITE
  pop_size = 10
  # goal = np.array([int(x) for x in sys.argv[1].split(',')], dtype=np.uint8)

  pop = rng.uniform(0., 1, size=(pop_size, len(palette)))
  corte = 0  

if __name__ == '__main__':
  main()