# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:32:33 2021

@author: jonvw
"""
'''
Code to demonstrate rosette creation of stellar orbit with epicycle
'''
import vpython as vp
import numpy as np
import time

SCENE = vp.canvas(width=1200, height=1200)

CURVE = vp.sphere(make_trail=True, radius=1)

# Initiate angles for circular and epicycle orbits, as well as angular increase per step
Theta = 0
Phi = 0
DTheta = (np.pi*.01)
DPhi = (np.pi*.011)
x = np.cos(Theta)*100 + np.cos(Phi)*10
y = np.sin(Theta)*100 + np.sin(Phi)*10

CURVE.pos = vp.vector(x,y,0)

time.sleep(3)

for step in range(3000):
    time.sleep(.01)
    Theta += DTheta
    Phi -= DPhi
    x = np.cos(Theta)*100 + np.cos(Phi)*10
    y = np.sin(Theta)*100 + np.sin(Phi)*10
    CURVE.pos = vp.vector(x,y,0)
    
