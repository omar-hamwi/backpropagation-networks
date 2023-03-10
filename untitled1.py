# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iyOu6iebc6EFHk2Vg-RcnVKHEGpboL6i
"""

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

#sigmond function 
def nlinear(x,deriv=False):
  if(deriv==True):
    return x*(1-x)
  return 1/(1+np.exp(-x))

#input dataset
X=np.array([   [0,0,1],
               [0,1,1],
               [1,0,1],
               [1,1,1],
            ])
#output dataset 
y=np.array([[0,0,1,1]]).T
#seed random number for random distribution 
#deterministic
np.random.seed(1)
#initialize weighs randomly with mean 0 
synapse0=2*np.random.random((3,1))-1

for i in range(1000):
  #forward propagation 
  layer0=X
  layer1=nlinear(np.dot(layer0,synapse0))
  #calculate error 
  layer1_error=y-layer1
  #multiply how much error backpropogated 
  #slop of the sigmoid at the values in layer1 
  layer1_delta=layer1_error*nlinear(layer1,True)

#update weights as per the errors backpropgats 
synapse0 +=np.dot(layer0.T,layer1_delta)

print("Output After Training:")
print(layer1)
print("Actual Output: ")
print(y)

df=[y,layer1]

df

plt.plot(y,layer1)

