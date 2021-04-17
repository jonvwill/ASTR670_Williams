#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code to create 'winding problem' demo. Saves frames for later
translation into movie (e.g. with FFMpeg)

Jonathan Williams
March 31, 2021
"""

import matplotlib.pyplot as plt
import numpy as np


# By scale, this code will create a "winding effect" for a 1kpc radius
# set of particles over about 10 Myr, assuming 240 km/s azimuthal velocity.
vel = 240
r = np.append(np.arange(1000,0,-1),np.arange(1,1001,1))
theta = np.append(np.pi * np.ones(1000), np.zeros(1000))
Dtheta = 0.01 * vel / r
x = np.arange(-1000,1000,1)
y = np.zeros(2000)



for step in range(1000):
    theta += Dtheta
    x = np.cos(theta) * r
    y = np.sin(theta) * r
    plt.scatter(x,y, s=0.1)
    plt.xlim([-1500,1500])
    plt.ylim([-1500,1500])
    name = ".\\ani\\out%04d.png" %step
    plt.savefig(name, dpi=300)
    plt.clf()
