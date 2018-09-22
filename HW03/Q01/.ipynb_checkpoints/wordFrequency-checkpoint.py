#Emanuel Casiano-Diaz - September 12, 2018.
#INSERT PROGRAM DESCRIPTION

import numpy as np
import matplotlib.pyplot as plt
from math import log
from scipy.stats import linregress
import colors
import pandas as pd

#with plt.style.context('../../IOP_large.mplstyle'):

#Some nice pastel colors
red = ["#e85c47"]
blue = ["#4173b3"]
orange = ["#ff8c00"]
green = ["#7dcca4"]
violet = ["#b19cd9"]

alpha = [0.8,0.5,0.1]

for i,c in enumerate(alpha):
        red.append(colors.get_alpha_hex(red[0],alpha[i]))
        orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
        green.append(colors.get_alpha_hex(green[0],alpha[i]))
        blue.append(colors.get_alpha_hex(blue[0],alpha[i]))
        violet.append(colors.get_alpha_hex(violet[0],alpha[i]))

"--------------------------------------------------------------------"
#Define functions
def findPowerLaw(x,y,rSquared=False):
    '''Input: x and y data (arrays of real numbers)'''
    '''Output: Prefactor and exponent of power law scaling''' 

    #Perform linear regression of x,y data
    #p , logA = np.polyfit(np.log10(x),np.log10(y),deg=1)
    gamma, logA, r_value, p_value, std_err = linregress(np.log10(x),np.log10(y))
    A = 10**(logA)
    #p: exponent, A: prefactor
    if(rSquared == False):
        return A,gamma
    else: return A,gamma,r_value**2

def findNearest(array, val, above=None, below=None):
    #array = np.sort(array)
    indicesUpToVal = np.where(array <= val)
    valIdx = np.max(indicesUpToVal)
    return valIdx        
"--------------------------------------------------------------------"

#Load data
data = np.loadtxt("vocab_cs_mod.txt")
data2 = np.loadtxt("vocab_cs_modSliced2.txt")

k = data[:,0]
Nk = data[:,1]

k2 = data2[:,0]
Nk2 = data2[:,1]

"--------------------------------------------------------------------"

#Determine CCDF exponent
#A,p,r2 = findPowerLaw(k2,Nk2,rSquared=True)

kMean = np.mean(k)
kStDev = np.std(k)

kSize = np.size(k)
conf95Low = kMean - 2*kStDev/np.sqrt(kSize)
conf95High = kMean + 2*kStDev/np.sqrt(kSize)


print("---Nk---")
#print("Power Law Exponent: %.8f with r^2 = %.8f" % (p,r2))
print("Mean: %.5e"%(kMean))
print("St Dev: %.5e"%(kStDev))
print("Confidence Interval: [%.5e,%.5e]"%(conf95Low,conf95High))
print("")

"--------------------------------------------------------------------"

gamma = 1.6951
fig, ax2 = plt.subplots()
ax2.plot(np.log10(k),np.log10(k**-(gamma-1)),'.',color=violet[0])
ax2.set_xlabel(r"$\log_{10}{k}$")
ax2.set_ylabel(r"$\log_{10}{N_{\geq k}}$")
plt.savefig("wordFrequencyCCDFLog.pdf",rasterized=True)





