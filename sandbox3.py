import math
from ctb import place

radius = 10
segments = 30

for position in range(segments):
    radians = 2 * math.pi * position / segments
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    place(x, y, 0)
