#!/usr/bin/env python
# coding=utf-8
'''
Author: niuyukai
email: 0906150215@csu.edu.cn
Date: 2020-08-17 08:36:08
LastEditTime: 2020-08-30 22:23:42
Description: Modify here please
FilePath: \hw1\test1.py
'''

import matplotlib.pyplot as plt
import math

tolerance = 2e-2

#object initial
v_o = 5
x_o, y_o = 0, 3

#missle initial 
x_m, y_m = 0, 0
v_m = 10

#draw figure 
plt.figure(figsize=(10, 10), dpi=80)
plt.title(" missile flight simulator ", fontsize=40)
plt.xlim(0, 4)
plt.ylim(0, 4)
#plt.xticks([])
#plt.yticks([])
  
while True:    
    if math.sqrt((x_o - x_m) ** 2 + (y_o - y_m) ** 2) <= tolerance:
        print("collision")
        plt.plot(x_m, y_m, 'o')
        
        plt.pause(0)
        break
    elif x_o < x_m:
        alpha = math.pi + math.atan((y_o - y_m) / (x_o - x_m))
    elif x_o == x_m:
        alpha = math.pi / 2
    else:
        alpha = math.atan((y_o - y_m) / (x_o - x_m))
    #set step time is 0.01
    #object x  
    x_o = x_o + v_o * 0.01
    #missle x and y
    x_m = x_m + v_m * 0.01 * math.cos(alpha)
    y_m = y_m + v_m * 0.01 * math.sin(alpha)
    #print alpha, beta
    plt.plot(x_o, y_o, 'r.', alpha=.5)
    plt.plot(x_m, y_m, 'bx', alpha=.5)
    plt.legend(("target", "missile"), loc="upper left", prop={'size': 12})
    plt.pause(0.1)