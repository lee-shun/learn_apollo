import sys
sys.path.append("../mathlib")

from Matrix import *


'''
Implement the KF below
'''

measurements = [1, 2, 3]


def kalman_filter(x, p):
    for n in range(len(measurements)):
        #update---->measurement
        

x = Matrix([[0.], [0.]])  # initial state (location and velocity)
P = Matrix([[1000., 0.], [0., 1000.]])  # initial uncertainty
u = Matrix([[0.], [0.]])  # external motion
F = Matrix([[1., 1.], [0, 1.]])  # next state function
H = Matrix([[1., 0.]])  # measurement function
R = Matrix([[1.]])  # measurement uncertainty
I = Matrix([[1., 0.], [0., 1.]])  # identity matrix

print(kalman_filter(x, P))
