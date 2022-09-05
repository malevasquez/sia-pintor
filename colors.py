# from colorutils import Color
import numpy as np
import math
from main import palette
from genetic import aptitud, distance2

goal = (50, 50, 50)

#calculates the euclidean distance between the rgb spaces of two colors
def distance(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return math.sqrt((math.pow(r2-r1,2) + math.pow(g2-g1,2) + math.pow(b2-b1,2)))


# def mix(c1, c2, p):
#     r1, g1, b1 = c1
#     r2, g2, b2 = c2

#     aux_red = p*math.pow(255-r1,2) + (1-p)*math.pow(255-r2,2)
#     aux_green = p*math.pow(255-g1,2) + (1-p)*math.pow(255-(1-p)*g2,2)
#     aux_blue = p*math.pow(255-p*b1,2) + (1-p)*math.pow(255-(1-p)*b2,2)

#     red = round(255-math.sqrt(aux_red)/2)
#     green = round(255-math.sqrt(aux_green)/2)
#     blue = round(255-math.sqrt(aux_blue)/2)

#     return Color((red,green,blue))

def mix_prueba2(colors):
    alphas = colors[:, -1]
    rgbs = colors[:, :-1]

    rn = min(255, np.sum(rgbs[:, 0] * alphas))
    gn = min(255, np.sum(rgbs[:, 1] * alphas))
    bn = min(255, np.sum(rgbs[:, 2] * alphas))

def mix_prueba(colors):
    alphas = colors[:, -1]
    total_weight = np.sum(alphas)

    rgbs = colors[:, :-1]

    rn = np.sum(rgbs[:, 0] * alphas) / total_weight
    gn = np.sum(rgbs[:, 1] * alphas) / total_weight
    bn = np.sum(rgbs[:, 2] * alphas) / total_weight

    return rn, gn, bn

def mix_n(colors):
    new_color = colors[0]

    for i in range(1, len(colors)):
        new_color = mix_rgba(new_color, colors[i])

    return new_color

def mix_rgba(c1, c2):
    r1, g1, b1, a1 = c1
    r2, g2, b2, a2 = c2

    r3 = 255-math.sqrt(((255-r1)**2 + (255-r2)**2)/2)
    g3 = 255-math.sqrt(((255-g1)**2 + (255-g2)**2)/2)
    b3 = 255-math.sqrt(((255-b1)**2 + (255-b2)**2)/2)
    a3 = 255-math.sqrt(((255-a1)**2 + (255-a2)**2)/2)

    return r3, g3, b3, a3
    # a3 = 1 - (1 - a1) * (1 - a2)
    
    # # if (a3 < 1.0e-6):
    # #     return 0, 0, 0, a3
    
    # r3 = (r1 * a1 / a3 + r2 * a2 * (1 - a1) / a3)
    # g3 = (g1 * a1 / a3 + g2 * a2 * (1 - a1) / a3)
    # b3 = (b1 * a1 / a3 + b2 * a2 * (1 - a1) / a3)

    # return r3, g3, b3, a3


def fitness(c1):
    return aptitud(c1)



# ##Gene: color
# ##Chromosome: color mix
# ##Population: all mixes possible
