import numpy as np
from csv import reader

import colors

goal = (50,50,50)

def get_colors(path) -> np.ndarray:
  file = open(path)
  csvreader = reader(file)

  colores = []
  for row in csvreader:
    r, g, b = (int(x) for x in row)
    colores.append( (r, g, b) )
  return np.array(colores, dtype=np.uint8)

def check_finished(iter, pop, mixes, delta):
  if (iter >= 10000):
    return True

  aps = np.apply_along_axis(colors.fitness, 1, mixes)
  best_aps = np.max(aps)

  order = np.argsort(aps)
  best = np.flip(mixes[order], axis=0)
  best = best[0]
  
  print("best mix con aptitud = {}".format(best_aps))
  print(best)
  print("props:")
  pop = np.flip(pop[order], axis=0)
  print(pop[0])

  return (1 - best_aps) < delta

def get_rgba(rgbs, alphas):
  rgbas = []
  size = len(rgbs)
  for i in range(len(alphas)):
    rgba = np.concatenate((rgbs, alphas[i].reshape(1,size).T), axis=1)
    rgbas.append(rgba)
  return np.array(rgbas)

def mix_all(rgbas):
  mixes = []
  for i in range(len(rgbas)):
    mixes.append(colors.mix_n(rgbas[i]))
  return np.array(mixes)

def mix_all_prueba(rgbp):
  mixes = []
  for i in range(len(rgbp)):
    mix = colors.mix_prueba2(rgbp[i])
    mixes.append(mix)
  return np.array(mixes)

def get_rgbp(rgbs, p):
  rgbps = []
  s = len(p[0])
  for i in range(len(p)):
    rgbp = np.concatenate((rgbs, p[i].reshape(1, s).T), axis=1)
    rgbps.append(rgbp)
  return np.array(rgbps)