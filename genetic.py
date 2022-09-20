from select import select
import numpy as np
from colors import distance, MAX_DISTANCIA
from enum import Enum

rng = np.random.default_rng()

def aptitud(color, goal):
  return 1 - (distance(color, goal) / MAX_DISTANCIA)

# SELECCION

def select_elite(pop, mixes, f, k, goal):
  fitness = np.apply_along_axis(f, 1, mixes, (goal))
  order = np.argsort(fitness)
  best = np.flip(pop[order], axis=0)

  return best[:k]

def select_roulette(pop, mixes, f, k, goal):
  fitness = np.apply_along_axis(f, 1, mixes, (goal))
  sum_fitness = np.sum(fitness)

  ps = fitness / sum_fitness
  qs = np.cumsum(ps)
  rs = rng.uniform(0., 1., size=(k,))

  selection = []
  for ri in rs:
    for i in range(len(qs)):
      if (qs[i-1] < ri <= qs[i]):
        selection.append(pop[i])

  return np.array(selection)

def select_tourney(pop, mixes, f, k, goal, m=2):
  fitness = np.apply_along_axis(f, 1, mixes, (goal))
  order = np.argsort(fitness)
  pop = pop[order]

  selection = []
  for i in range(k):
    idxs = rng.choice(len(pop), size=k, replace=False)
    winner = pop[np.max(idxs)]
    selection.append(winner)

  return np.array(selection)


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

def cross_n(parents, method):
  children = []
  for i in range(0, len(parents) // 2 + 1, 2):
    ch1, ch2 = method(parents[i], parents[i+1])
    
    children.append(ch1)
    children.append(ch2)

  return np.array(children)

# MUTACION
def mutate_gen(gen):
  u = gen * 0.5
  delta = rng.uniform(-u, u)
  return gen + delta

def mutate(pi):
  probs = rng.uniform(0., 1., len(pi))
  pi = np.where(probs > 0.5, mutate_gen(pi), pi)
  return pi
  
def mutate_n(pop):
  mutated = np.apply_along_axis(mutate, 1, pop)
  return mutated

class SelectOption(Enum):
  ELITE = select_elite
  ROULETTE = select_roulette
  TOURNEY = select_tourney

class CrossOption(Enum):
  SIMPLE = cross_simple
  DOUBLE = cross_double
  UNIFORM = cross_uniform  