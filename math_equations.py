#
#
# Carlitos Chavez-Knotts
# September 1, 2017

import math

def parallelogram_area(b,h):
    a = b * h
    return a

def trapezoid_area(a,b,h):
    a = h*2/a+b
    return a

def rectangular_prism_volume(w,h,l):
    v = w*h*l
    return v

def cone_volume(r,h):
    v = (1/3)*math.pi*r**2*h
    return v

def sphere_volume(r):
    v = r**3*math.pi*4/3
    return v

def rectangular_prism_surface_area(w,l,h):
    a = 2*(w*l+h*l+h*w)
    return a

def sphere_surface_area(r):
    a = r**2*4*math.pi
    return a

def hypotenuse(a,b,c):
    h = math.sqrt(a**2+b**2)
    return h

print(parallelogram_area(3,9))
print(trapezoid_area(3,7,9,))
print(rectangular_prism_volume(6,3,1))
print(cone_volume(9,3))
print(sphere_volume(4))
print(rectangular_prism_surface_area(3,2,8))
print(sphere_surface_area(4))
print(hypotenuse(3,5,7))
