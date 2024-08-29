''' import math

pi = 3.14
r = 30
area_of_circle = pi * r * r

print(area_of_circle)


pi = 3.14
r = 30

circumference = 2 * pi * r
print(circumference)


import math
radius = int(input("Enter the radius of the circle: "))
pi = 3.14

area = pi * radius * radius
print(area)
'''

def circle ():
    try:
        radius = int(input("Enter the radius of the circle: "))
        pi = 3.14
        area = pi * radius * radius
        return f'The area of the circle is {area}'
    except ValueError:
        return ("Radius can only be a number!")
    
area = circle()
print(area)
