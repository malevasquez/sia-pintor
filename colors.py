from colorutils import Color
import math

colors = []

size = int(input("Enter palette size: "))
exp_r, exp_g, exp_b = map(int, input("Enter comma-separated rgb values of expected color: ").split(','))
expected = Color((exp_r, exp_g, exp_b))

count = 0

while count < size:
    r, g, b = map(int, input("Enter comma-separated rgb values: ").split(','))
    colors.append(Color((r,g,b)))
    count += 1

##c1 = Color((153,102,255))
##c2 = Color((255,255,102))

red = 0
green = 0
blue = 0

for c in colors:
    red += math.pow(255-c.red,2)
    green += math.pow(255-c.green,2)
    blue += math.pow(255-c.blue,2)
    
red = round(255-math.sqrt(red)/2)
green = round(255-math.sqrt(green)/2)
blue = round(255-math.sqrt(blue)/2)

result = Color((red,green,blue))

#FITNESS
#difference -> euclidean distance :: select mix with lowest distance
distance = math.sqrt((math.pow(result.red-expected.red,2) + math.pow(result.green-expected.green,2) + math.pow(result.blue-expected.blue,2)))

#manual distance
##diffRed = abs(result.red - expected.red)
##diffGreen = abs(result.green - expected.green)
##diffBlue = abs(result.blue - expected.blue)
##pctDiffRed = float(diffRed)/255
##pctDiffGreen = float(diffGreen)/255
##pctDiffBlue = float(diffBlue)/255
##diff = ((pctDiffRed + pctDiffGreen + pctDiffBlue) / 3) * 100


##Gene: color
##Chromosome: color mix
##Population: all mixes possible
