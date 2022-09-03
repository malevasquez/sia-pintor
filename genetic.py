import numpy as np
import math
from enum import Enum

rng = np.random.RandomState()

def distance(r1, g1, b1, r2, g2, b2):
    return math.sqrt((math.pow(r2-r1,2) + math.pow(g2-g1,2) + math.pow(b2-b1,2)))

def aptitud(color):
  return 1 / distance

# SELECCION

def select_elite(pop, f, k):
  fitness = np.apply_along_axis(f, 1, pop)
  order = np.argsort(fitness)
  best = np.flip(pop[order], axis=0)

  return best[:k]

def select_roulette(pop, f, k):
  selection = []
  fitness = np.apply_along_axis(f, 1, pop)
  print(fitness)
  ps = fitness / np.sum(fitness)
  print(ps)
  qs = np.cumsum(ps)
  print(qs)

  rs = rng.uniform(0., 1., size=(k,))
  print("rs:")
  print(rs)
  for ri in rs:
    for i in range(len(qs)):
      if (qs[i-1] < ri <= qs[i]):
        selection.append(pop[i])

  return np.array(selection)

def select_tourney(pop, f, k, m=2):
  fitness = np.apply_along_axis(f, 1, pop)
  order = np.argsort(fitness)
  selection = []

  for i in range(k):
    idxs = rng.randint(0, len(pop), size=m)
    pool, aps = pop[idxs], fitness[idxs]
    print("pool:")
    print(pool)
    print("aps:")
    print(aps)
    winner = pool[np.where(aps == np.max(aps))]
    print("winner:")
    print(winner)
    selection.append(winner)
  
  return np.array(selection)
class SelectOption(Enum):
  ELITE = select_elite
  ROULETTE = select_roulette
  TOURNEY = select_tourney

# CRUZA

def cross_simple(x, y):
  s = len(x)
  p = rng.randint(0, s)

  ch1 = np.concatenate([x[:p], y[p:]])
  ch2 = np.concatenate([y[:p], x[p:]])

  return ch1, ch2

def cross_double(x, y):
  s = len(x)
  p1, p2 = np.sort(rng.randint(0, s, size=2))

  ch1 = np.concatenate([x[:p1], y[p1:p2], x[p2:]])
  ch2 = np.concatenate([y[:p1], x[p1:p2], y[p2:]])

  return ch1, ch2

def cross_uniform(x, y):
  ps = rng.uniform(0., 1., size=len(x))
  
  ch1 = np.where(ps > 0.5, x, y)
  ch2 = np.where(ps < 0.5, x, y)

  return ch1, ch2

