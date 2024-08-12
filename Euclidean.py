# Euclidean distance is a measure of the "straight line" distance 
# between two points in Euclidean space. It is one of the most commonly used distance measures in mathematics

import math

point1 = (2,3)
point2 = (10,8)

distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

print(distance)