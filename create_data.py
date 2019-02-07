#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:15:48 2019

@author: antonin.gallot
"""
import random
import matplotlib.pyplot as plt

def generate_coords_convex(N, a, b, alpha):
    res = list()
    for i in range(N):
        x = random.uniform(a, b)
        y = 1/(x**alpha)
        res.append((x, y))
    res.sort()
    return res

def create_file_convex(N, a, b, alpha, points, number):
    filename = "dataConvex_" + str(a) + "_" + str(b) + "_" + str(alpha) + "_" + str(N) + "_ex" + str(number) +".txt"
    f = open(filename, "w")
    f.write(str(N) + " " + "2" + " \n")
    for x, y in points:
        f.write(str(x) + " " + str(y) + "\n")
    f.close()
    
def generate_coords_concav(N, a, b, alpha):
    res = list()
    for i in range(N):
        x = random.uniform(a, b)
        y = 1-(x**alpha)
        res.append((x, y))
    res.sort()
    return res

def create_file_concav(N, a, b, alpha, points, number):
    filename = "dataConcav_" + str(a) + "_" + str(b) + "_" + str(alpha) + "_" + str(N) + "_ex" + str(number) + ".txt"
    f = open(filename, "w")
    f.write(str(N) + " " + "2" + " \n")
    for x, y in points:
        f.write(str(x) + " " + str(y) + "\n")
    f.close()
    
def generate_coords_alea(N, A, B):
    res = list()
    x = 0
    y = 1000
    res.append((x, y))
    for i in range(N):
        a = random.uniform(0, A)
        b = random.uniform(0, B)
        x = x + a
        y = y - b
        res.append((x, y))
    return res
    
def create_file_alea(N, A, B, points, number):
    filename = "dataAlea_" + str(A) + "_" + str(B) + "_" + str(N) + "_ex" + str(number) + ".txt"
    f = open(filename, "w")
    f.write(str(N) + " " + "2" + " \n")
    for x, y in points:
        f.write(str(x) + " " + str(y) + "\n")
    f.close()

def generate_coords_alea_box(N, A, B):
    res = list()
    box = list()
    x = 0
    y = 1000
    n = 0
    #Boite xmin,xmax * ymin,ymax
    box.append( ((x, y),(x, y)) )
    while (n < N):
        indice = random.randint(0, len(box)-1)
        currentbox = box.pop(indice)
        xpoint = random.uniform(currentbox[0][0], currentbox[0][1])
        ypoint = random.uniform(currentbox[1][0], currentbox[1][1])
        res.append((xpoint, ypoint))
        n = n + 1
        newbox1 = ( (currentbox[0][0], xpoint), (ypoint, currentbox[1][1]) )
        box.append(newbox1)
        newbox2 = ( (xpoint, currentbox[0][1]), (currentbox[1][0], ypoint) )
        box.append(newbox2)
    res.sort()
    return res
    
def create_file_alea_box(N, A, B, points, number):
    filename = "dataAleaBox_" + str(A) + "_" + str(B) + "_" + str(N) + "_ex" + str(number) + ".txt"
    f = open(filename, "w")
    f.write(str(N) + " " + "2" + "\n")
    for x, y in points:
        f.write(str(x) + " " + str(y) + " \n")
    f.close()

def display(l):
    xlist= list()
    ylist= list()
    for p in l:
        xlist.append(p[0])
        ylist.append(p[1])
    plt.plot(xlist, ylist, 'k.')
    plt.show()

def mult_instances_convex(N, a, b, alpha, p):
    for i in range(p):
        data = generate_coords_convex(N, a, b, alpha)
        create_file_convex(N, a, b, alpha, data, i)
    display(data)
    
def mult_instances_concav(N, a, b, alpha, p):
    for i in range(p):
        data = generate_coords_concav(N, a, b, alpha)
        create_file_concav(N, a, b, alpha, data, i)
    display(data)

def mult_instances_alea(N, A, B, p):
    for i in range(p):
        data = generate_coords_alea(N, A, B)
        create_file_alea(N, A, B, data, i)
    display(data)

def mult_instances_alea_box(N, A, B, p):
    for i in range(p):
        data = generate_coords_alea_box(N, A, B)
        create_file_alea_box(N, A, B, data, i)
    display(data)

def create_data(N, a, b, alpha, A, B, p):
    mult_instances_convex(N, a, b, alpha, p)
    mult_instances_concav(N, a, b, alpha, p)
    mult_instances_alea(N, A, B, p)
    mult_instances_alea_box(N, A, B, p)