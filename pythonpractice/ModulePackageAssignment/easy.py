#1 Square Root
import math

n=int(input("Enter number: "))
print(math.sqrt(n))

#2 Calculator
import calculator

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print(calculator.add(a,b))
print(calculator.subtract(a,b))

#3. geometry
from geometry.shapes import circle_area,rectangle_area

r=int(input("Enter radius: "))
l=int(input("Enter length: "))
b=int(input("Enter breadth: "))

print(circle_area(r))
print(rectangle_area(l,b))

#4 Import only sin and cos
from math import sin,cos,radians

n=int(input("Enter angle: "))
print("sin(90) =",sin(radians(n)))
print("cos(90) =",round(cos(radians(n)),1))