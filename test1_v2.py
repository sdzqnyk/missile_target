#!/usr/bin/env python
# coding=utf-8
'''
Author: niuyukai
email: 0906150215@csu.edu.cn
Date: 2020-08-17 12:38:17
LastEditTime: 2020-08-30 22:22:28
Description: 面向对象missile_v2
FilePath: \hw1\test1_v2.py
'''

import numpy as np
import matplotlib.pyplot as plt

tolerance = 1e-1
dt = 0.01
# plane initial 
p_p = np.array([0,2])
p_p = p_p.astype(np.float64)
v_p = np.array([5,0])
v_p = v_p.astype(np.float64) 

# missile initial
p_m = np.array([0,0])
p_m = p_m.astype(np.float64)
v_m = 10.

#draw picture
plt.figure(figsize=(10, 10), dpi=80)
plt.title(" missile flight simulator ", fontsize=40)
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.xticks([])
plt.yticks([])

class Entity(object):
    def __init__(self,pos):
        self.pos = pos
        
    def step(self):
        pass

class Plane(Entity):
    def __init__(self, pos):
        super(Plane, self).__init__(pos)
    
    def access(self, v, dt):
        self.pos = self.pos + v * dt 
        return self.pos
    
    
class Missile(Entity):
    def __init__(self, pos):
        super(Missile, self).__init__(pos)

    def access(self, v, target, dt):        
        self.pos = self.pos + (target - self.pos)/np.linalg.norm(target - self.pos, axis=0) * v * dt        
        return self.pos

    def distance(self, target):
        return np.linalg.norm(target - self.pos, axis=0)       
        

m1 = Missile(p_m)
p1 = Plane(p_p)

while True:
    
    x_m, y_m = m1.access(v_m, p1.pos, dt)
    x_p, y_p = p1.access(v_p, dt)
    
    if m1.distance(p1.pos) <= tolerance :
    
        print("collision")
        plt.plot(x_p, y_p, 'o')
        plt.annotate('crash point', xy=(x_m, y_m),  xycoords='data',
                     xytext=(+15, +15), textcoords='offset points', fontsize=12,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
        plt.pause(0.1)
        plt.show()
        break

    #print alpha, beta
    plt.plot(x_m, y_m, 'bx', alpha=.5)
    plt.plot(x_p, y_p, 'k*', alpha=.5)
    plt.legend(("missile", "plane"), loc="upper left", prop={'size': 12})
    plt.pause(0.1)
