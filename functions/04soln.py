import math

def function(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference

radius=5
print(function(radius))
