import math
q1 = float(input("Enter Q1: "))   # degree
r1 = float(input("Enter r1: "))
q2 = float(input("Enter Q1: "))
r2 = float(input("Enter r2: "))

a1 = (math.pi/180)*q1
a2 = (math.pi/180)*q2  # rad

sin1 = math.sin(a1)
cos1 = math.cos(a1)
sin2 = math.sin(a2)
cos2 = math.cos(a2)

x1 = r1*cos1
y1 = r1*sin1
x2 = r2*cos2
y2 = r2*sin2

x = x1 + x2
y = y1 + y2

s = x**2 + y**2
r = s**0.5

p = math.atan(y/x)
m = math.pi
n = 180/m
q = n*p




print(f'We get: ({x}, {y})')
print(f'We have r = {r}')
print(f'we get Q= {q}')
