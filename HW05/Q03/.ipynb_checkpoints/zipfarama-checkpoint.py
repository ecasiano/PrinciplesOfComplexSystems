#Determine the scaling exponent of the "Zipfarama" distribution

import numpy as np
import colors
from math import inf
'''---Define Functions---'''

def zipfarama(a,alpha,n):
        #a = shift, alpha = scaling exponenet, n = sum upper limit
        j = np.arange(1,n+1)
        return (j + a)**(-alpha)

'''---Main---'''
#Parameters
n = 1E+06
a = 1
alpha = np.random.random() #Randomly generate an alpha in [0,1)

#Absolute error between 1 and summation with the current alpha
error = np.abs(np.sum(zipfarama(a,alpha,n)) - 1)

#Desired tolerance between 1 and summation
tol = 1E-03

#Estimating loop
while(error > tol):
    if(np.sum(zipfarama(a,alpha,n)) < 1): #Decrease alpha if the sum is smaller than 1
        alpha = 0.99*alpha
    else:                                 #Increase alpha if the sum is larger than 1
        alpha = 1.01*alpha
    error = np.abs(np.sum(zipfarama(a,alpha,n)) - 1)
    print("alpha: %.2f error: %.4f"%(alpha,error))    