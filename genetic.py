from turtle import shape
import numpy as np
import math
import colors
from enum import Enum

goal = (50, 50, 50)
rng = np.random.default_rng()

def distance2(c1, c2):
  r1, g1, b1 = c1
  r2, g2, b2 = c2

  d_r = r1 - r2
  d_g = g1 - g2
  d_b = b1 - b2
  
  d = math.sqrt( (d_r**2) + (d_g**2) + (d_b**2) )


  # r_ = 0.5 * (r1 + r2)

  # d = math.sqrt(
  #   (2 + (r_ / 256)) * (d_r**2)
  # + (4 * (d_g**2))
  # + (2 + (255 - r_) / 256) * (d_b**2) )

  return d


MAX_DISTANCIA = distance2((0,0,0), (255,255,255))

def distance_w(c1, c2):
  r1, g1, b1 = c1
  r2, g2, b2 = c2

  d_r = r1 - r2
  d_g = g1 - g2
  d_b = b1 - b2

  return math.sqrt((0.3 * (d_r**2)) + (0.59 * (d_g**2)) + (0.11 * (d_b)**2))

def distance(r1, g1, b1, r2, g2, b2):
    return math.sqrt((math.pow(r2-r1,2) + math.pow(g2-g1,2) + math.pow(b2-b1,2)))

def aptitud(color):
  return 1 - (distance2(color, goal) / MAX_DISTANCIA)

def distancia(color, goal):
  r1, g1, b1, a1 = color
  r2, g2, b2, a2 = goal
  return math.sqrt()

# SELECCION

def select_elite(pop, mixes, f, k):
  fitness = np.apply_along_axis(f, 1, mixes)
  order = np.argsort(fitness)
  best = np.flip(pop[order], axis=0)

  return best[:k]

def select_roulette(pop, mixes, f, k):
  selection = []
  fitness = np.apply_along_axis(f, 1, mixes)
  # print(fitness)
  ps = fitness / np.sum(fitness)
  # print(ps)
  qs = np.cumsum(ps)
  # print(qs)

  rs = rng.uniform(0., 1., size=(k,))
  # print("rs:")
  # print(rs)
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
    idxs = rng.integers(0, len(pop), m)
    pool, aps = pop[idxs], fitness[idxs]
    # print("pool:")
    # print(pool)
    # print("aps:")
    # print(aps)
    winner = pool[np.where(aps == np.max(aps))]
    # print("winner:")
    # print(winner)
    selection.append(winner)
  
  return np.array(selection)

class SelectOption(Enum):
  ELITE = select_elite
  ROULETTE = select_roulette
  TOURNEY = select_tourney

# CRUZA

def cross_simple(x, y):
  s = len(x)
  p = rng.integers(1, s)

  ch1 = np.concatenate([x[:p], y[p:]])
  ch2 = np.concatenate([y[:p], x[p:]])

  return ch1, ch2

def cross_double(x, y):
  s = len(x)
  p1, p2 = np.sort(rng.integers(0, s, size=2))

  ch1 = np.concatenate([x[:p1], y[p1:p2], x[p2:]])
  ch2 = np.concatenate([y[:p1], x[p1:p2], y[p2:]])

  return ch1, ch2

def cross_uniform(x, y):
  ps = rng.uniform(0., 1., size=len(x))
  
  ch1 = np.where(ps > 0.5, x, y)
  ch2 = np.where(ps < 0.5, x, y)

  return ch1, ch2

# MUTACION

def mutate(pi):
  deltas = rng.uniform(-0.05, 0.05, len(pi))

  pf = pi + deltas
  pf = np.abs(pf)

  return pf
  
def cross_n(parents):
  children = []
  for i in range(0, len(parents) // 2 + 1, 2):
    # print("parents")
    # print(parents[0], parents[1])
    # print("children")
    # print(children)

    ch1, ch2 = cross_simple(parents[i], parents[i+1])
    
    children.append(ch1)
    children.append(ch2)


  return np.array(children)

def mutate_n(pop):
  probs = rng.random(size=pop.shape)
  mutated = np.where(probs > 0.5, pop + 0.05, pop - 0.05)
  mutated = np.abs(mutated)
  return mutated

def fill(parents, children, n, k):
  pass