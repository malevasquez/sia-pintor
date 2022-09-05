
import numpy as np
import colors 
import utils
import genetic
  
palette = utils.get_colors("./colores.csv")
rng = np.random.default_rng()

def main():
  print("palette")
  print(palette.shape)
  print(palette)
  goal = np.array([int(x) for x in input("objective color: ").split(',')], dtype=np.uint8)
  selector = genetic.SelectOption.ROULETTE
  N = 200

  # goal = np.array([int(x) for x in sys.argv[1].split(',')], dtype=np.uint8)

  # poblacion inicial
  pop = rng.uniform(0., 1., size=(N, len(palette)))

  # mix inicial
  rgbp = utils.get_rgbp(palette, pop)
  mixes = utils.mix_all_prueba(rgbp)

  end = False
  i = 0
  delta = 0.01

  while (not end):
    print("iteracion: " + str(i)) 

    rgbp = utils.get_rgbp(palette, pop)
    mixes = utils.mix_all_prueba(rgbp)

    # check criteria
    end = utils.check_finished(i, pop, mixes, delta)

    # cruza
    parents = pop
    children = genetic.cross_n(parents)

    parentswithchildren = np.concatenate((parents, children), axis=0)
    # print("all")
    # print(parentswithchildren)


    # calculo de mezclas resultantes
    rgbp = utils.get_rgbp(palette, parentswithchildren)
    mixes = utils.mix_all_prueba(rgbp)

    # MUTACION
    parentswithchildren = genetic.mutate_n(parentswithchildren)


    # SELECCION 
    pop = selector(parentswithchildren, mixes, colors.fitness, N)
    # print("pop selected")
    # print(pop)

    i += 1



if __name__ == '__main__':
  # cs = rng.integers(0, 256, size=(5, 3), dtype=np.uint8)
  # print("cs")
  # print(cs)

  # alphas = rng.uniform(0., 1., size=(3, len(cs)))
  # print("alphas")
  # print(alphas)

  # rgbas = utils.get_rgba(cs, alphas)
  # print("rgba")
  # print(rgbas)

  # mixes = []
  # for i in range(len(rgbas)):
  #   mixes.append(colors.mix_n(rgbas[i]))
  # mixes = np.array(mixes)
  # print(mixes)

  main()