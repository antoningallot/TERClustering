#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:27:51 2019

@author: antonin.gallot
"""
import matplotlib.pyplot as plt

def get_points(filename):
    f = open(filename, "r")
    res = list()
    cpt = 0
    for line in f:
        if cpt == 0: 
            cpt = cpt + 1
        else:
            newline = line.split()
            res.append( (float(newline[0]), float(newline[1])) )
    return res

def display(l):
    xlist= list()
    ylist= list()
    for p in l:
        xlist.append(p[0])
        ylist.append(p[1])
    plt.plot(xlist, ylist, 'k.')
    plt.show()
    
filename = "dataAlea_10_50_100_ex1.txt"
points_list = get_points(filename)
display(points_list)