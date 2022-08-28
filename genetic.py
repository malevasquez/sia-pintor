import numpy as np

rng = np.random.default_rng()

def aptitud(color):
  pass

# SELECCION

def select_elite(pop, f, k):
  fitness = pop.apply_along_axis(f, 1, pop)
  order = np.argsort(fitness)
  best = np.flip(pop[order], axis=0)

  return best[:k]

def select_roulette(pop, f, k):
  selection = []
  fitness = pop.apply_along_axis(f, 1, pop)
  ps = fitness / np.sum(fitness)
  qs = np.cumsum(ps)

  rs = rng.uniform(0., 1., size=(k,))

  for ri in rs:
    for i in range(len(qs)):
      if (qs[i-1] < ri <= qs[i]):
        selection.append(qs[i])

  return np.array(selection)

def select_tourney(pop, f, k, m=2):
  fitness = pop.apply_along_axis(f, 1, pop)
  order = np.argsort(fitness)
  selection = []

  for i in range(k):
    idxs = rng.randint(0, pop.shape[0], m)
    pool, aps = pop[idxs], fitness[idxs]
    winner = pool[np.where(aps == np.max(aps))]
    selection.append(winner)
  
  return np.array(selection)

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