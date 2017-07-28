__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CS 600
    HW: #2, Pr 2.18, 'Numerical methods for engineers, 7th edition'
    Brief: Piecewise function for describing velocity in terms of time
'''


from math import exp
import numpy as np
import pylab as pl

def rocketVelocity(t):

    v = 0.0
    if (t>= 0 and t <= 10):
        v = 11 * t**2 - 5*t
    elif (t>= 10 and t <= 20):
        v = 1100 - 5*t
    elif (t >= 20 and t <= 30):
        v = 50*t + 2 * (t-20)**2
    elif (t > 30):
        v = 1520 * exp(-0.2 * (t-30))
    else:
        v = 0.0
    return v

def analyseRocketVelocity():

    print("t | v")
    times = [t * 0.1 for t in range(-5*10, 50*10, 5)] # range() works only with integers
    velocities = [rocketVelocity(t) for t in times]

    #Plot velocity vs time graph
    pl.plot(times,velocities)
    pl.xlabel('Time')
    pl.ylabel('Rocket velocity')
    pl.grid(True)
    pl.show()

    #Print the values
    for i in range(len(times)):
        print(times[i],"|",velocities[i])

analyseRocketVelocity()