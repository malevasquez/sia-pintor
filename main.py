from audioop import cross
import numpy as np

global goal

import utils
import genetic

rng = np.random.default_rng()


def main():
  palette = utils.get_colors("./colores.csv")
  print("palette")
  print(palette.shape)
  print(palette)
  # goal = np.array([int(x) for x in input("objective color: ").split(',')], dtype=np.uint8)
  goal = (255,125,0)

  selector = genetic.SelectOption.ELITE
  cross_method = genetic.CrossOption.SIMPLE

  # goal = np.array([int(x) for x in sys.argv[1].split(',')], dtype=np.uint8)

  # POBLACION INICIAL
  N = 100
  pop = rng.uniform(0., 1., size=(N, len(palette)))

  end = False
  delta = 0.01
  i = 0

  while (not end):
    print("iteracion: " + str(i))

    rgbp = utils.get_rgbp(palette, pop)
    mixes = utils.get_mixes(rgbp)

    # check criteria
    end = utils.check_finished(i, pop, mixes, delta, goal)

    # CRUZA
    parents = pop
    children = genetic.cross_n(parents, cross_method)

    parentswithchildren = np.concatenate((parents, children), axis=0)

    # calculo de mezclas resultantes
    rgbp = utils.get_rgbp(palette, parentswithchildren)
    mixes = utils.get_mixes(rgbp)

    # MUTACION
    parentswithchildren = genetic.mutate_n(parentswithchildren)

    # SELECCION 
    pop = selector(parentswithchildren, mixes, genetic.aptitud, N, goal)

    i += 1



if __name__ == '__main__':
  main()