import numpy as np
import colors
import utils
import genetic


rng = np.random.default_rng()

def main():
  palette = utils.get_colors("./colores.csv")
  goal = np.array([int(x) for x in input("objective color: ").split(',')], dtype=np.uint8)
  selector = genetic.SelectOption.ELITE
  pop_size = 10

  # goal = np.array([int(x) for x in sys.argv[1].split(',')], dtype=np.uint8)

  # poblacion inicial
  pop = rng.uniform(0., 1, size=(pop_size, len(palette)))

  end = False

  while (not end):
    mixes = np.apply_along_axis(colors.mix_n, 1, pop)

    # check criteria
    end = utils.check_finished()

    # seleccion
    parents = selector(pop, colors.fitness, pop_size // 2)

    # cruza
    children = genetic.cross_n(parents)

    # mutacion
    parents = genetic.mutate_n(parents)
    children = genetic.mutate_n(children)



if __name__ == '__main__':
  main()