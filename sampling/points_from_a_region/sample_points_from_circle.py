# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:38:14 2021

@author: lankuohsing
"""
"""https://www.cnblogs.com/TenosDoIt/p/4025221.html"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#right
def GeneratePointInCycle1(point_num, radius):
    for i in range(1, point_num+1):
        while True:
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            if (x**2) + (y**2) < (radius**2):
                break
        plt.plot(x, y, '*', color = "black")

#wrong
def GeneratePointInCycle2(point_num, radius):
    for i in range(1, point_num+1):
        x = random.uniform(-radius, radius)
        y_max = math.sqrt(radius**2 - x**2)
        y = random.uniform(-y_max, y_max)
        plt.plot(x, y, '*', color = "black")

#wrong
def GeneratePointInCycle3(point_num, radius):
    for i in range(1, point_num+1):
        theta = random.random()*2*pi;
        r = random.uniform(0, radius)
        x = r*math.sin(theta)
        y = r*math.cos(theta)
        plt.plot(x, y, '*', color = "black")

#right
def GeneratePointInCycle4(point_num, radius,center_x=0.0,center_y=0.0,R=1.0):
    for i in range(1, point_num+1):
        theta = random.random()*2*pi;
        r = random.uniform(0, radius)*R
        x = math.sin(theta)* (r**0.5) + center_x
        y = math.cos(theta)* (r**0.5) + center_y
        plt.plot(x, y, '*', color = "black")

# In[]
if __name__=="__main__":
    pi = np.pi
    theta = np.linspace(0, pi*2, 1000)
    R = 1
    x = np.sin(theta)*R
    y = np.cos(theta)*R

    plt.figure(figsize=(6,6))
    plt.plot(x,y,label = "cycle",color="red",linewidth=2)
    plt.title("cycyle")
    GeneratePointInCycle4(1000, R) #修改此处来显示不同算法的效果
    plt.legend()
    plt.show()