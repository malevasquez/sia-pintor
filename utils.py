from queue import Queue
import numpy as np
from csv import reader
import genetic
import colors

def get_colors(path) -> np.ndarray:
  file = open(path)
  csvreader = reader(file)

  colores = []
  for row in csvreader:
    r, g, b = (int(x) for x in row)
    colores.append( (r, g, b) )
  return np.array(colores, dtype=np.uint8)

last_fitness = []

def check_finished(iter, pop, mixes, delta, goal):

  if (iter >= 100):
    return True

  aps = np.apply_along_axis(genetic.aptitud, 1, mixes, (goal))
  best_aps = np.max(aps)

  if (len(last_fitness) < 5):
    last_fitness.append(best_aps)
  else:
    last_fitness.pop(0)
    last_fitness.append(best_aps)

  if(np.std(last_fitness) < 0.1):
    end = True

  order = np.argsort(aps)
  best = np.flip(mixes[order], axis=0)
  best = best[0]

  print(best_aps)
  
  print("best mix con aptitud = {}".format(best_aps))
  print(best)
  print("props:")
  pop = np.flip(pop[order], axis=0)
  print(pop[0])


  return False

  if (iter >=  max_iter):
    return True

  cond =  (1 - best_aps) < delta

  return cond, best, best_ap, 


def get_mixes(rgbp):
  mixes = []
  for i in range(len(rgbp)):
    mix = colors.mix_colors(rgbp[i])
    mixes.append(mix)
  return np.array(mixes)

def get_rgbp(rgbs, p):
  rgbps = []
  s = len(p[0])
  for i in range(len(p)):
    rgbp = np.concatenate((rgbs, p[i].reshape(1, s).T), axis=1)
    rgbps.append(rgbp)
  return np.array(rgbps)