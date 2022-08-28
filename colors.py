from colorutils import Color
from numpy import random
import math

#calculates the euclidean distance between the rgb spaces of two colors
def distance(r1, g1, b1, r2, g2, b2):
    return math.sqrt((math.pow(r2-r1,2) + math.pow(g2-g1,2) + math.pow(b2-b1,2)))


def mix(r1, g1, b1, r2, g2, b2, p):
    aux_red = p*math.pow(255-r1,2) + (1-p)*math.pow(255-r2,2)
    aux_green = p*math.pow(255-g1,2) + (1-p)*math.pow(255-(1-p)*g2,2)
    aux_blue = p*math.pow(255-p*b1,2) + (1-p)*math.pow(255-(1-p)*b2,2)

    red = round(255-math.sqrt(aux_red)/2)
    green = round(255-math.sqrt(aux_green)/2)
    blue = round(255-math.sqrt(aux_blue)/2)

    return Color((red,green,blue))

def fitness(r1, g1, b1, r2, g2, b2):
    return 1/distance

c1 = Color((153,102,255))
c2 = Color((255,255,102))

colors = [c1, c2]
exp = Color((204,179,179))

#first select the two colors closest to the expected
distances = []

for c in colors:
    distances.append(distance(c.red,c.green,c.blue,exp.red,exp.green,exp.blue))

#calculate all the different proportions for mixing the selected colors
#store them in a dictionary "results"
results = {}
k = 10
count = 0
while count < k:
    p = random.rand()
    c = mix(c1.red, c1.green, c1.blue, c2.red, c2.green, c2.blue, p)
    print(c)
    results[p] = distance(exp.red,exp.green,exp.blue,c.red,c.green,c.blue)
    count += 1

c = mix(c1.red, c1.green, c1.blue, c2.red, c2.green, c2.blue, 0.5)
print(c)
print (distance(exp.red,exp.green,exp.blue,c.red,c.green,c.blue))
print(results)

#use max with fitness, min with distance
max_p = max(results, key=results.get)
print(max_p)

#sort dictionary by values descending order
sorted(results.items(), key=lambda x: x[1], reverse=True)



##Gene: color
##Chromosome: color mix
##Population: all mixes possible
