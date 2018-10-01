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
    p, logA, r_value, p_value, std_err = linregress(np.log10(x),np.log10(y))
    A = 10**(logA)
    #p: exponent, A: prefactor
    if(rSquared == False):
        return A,p
    else: return A,p,r_value**2
    
def findNearest(array, val, above=None, below=None):
    #array = np.sort(array)
    indicesUpToVal = np.where(array <= val)
    valIdx = np.max(indicesUpToVal)
    return valIdx        
"--------------------------------------------------------------------"

#Load data
df = pd.read_csv('google_vocab_rawwordfreqs.txt', sep=" ", header=None)

#Extract k series to np.array
k = df.values
k = k.reshape(1,np.size(k))
k = k[0]

#Generate array with rank of each k
r = np.ones(np.size(k))
for i in range(np.size(k)):
    r[i] += i

"--------------------------------------------------------------------"

#Measure Zipf's exponent
A,p,r2 = findPowerLaw(r,k,rSquared=True)

kMean = np.mean(k)
kStDev = np.std(k)

kSize = np.size(k)
conf95Low = kMean - 2*kStDev/np.sqrt(kSize)
conf95High = kMean + 2*kStDev/np.sqrt(kSize)


print("---k---")
print("Zipf's Exponent: %.8f with r^2 = %.8f" % (p,r2))
print("Mean: %.5e"%(kMean))
print("St Dev: %.5e"%(kStDev))
print("Confidence Interval: [%.5e,%.5e]"%(conf95Low,conf95High))
print("")



"--------------------------------------------------------------------"

fig, ax1 = plt.subplots()
ax1.plot(np.log10(r[0:100000]),np.log10(k[0:100000]),'.',color=green[0])
ax1.set_xlabel(r"$\log_{10}{r}$")
ax1.set_ylabel(r"$\log_{10}{k_r}$")
#plt.savefig("zipfRanksLog.pdf",rasterized=True)
#plt.savefig("zipfRanksLog.png")
plt.savefig("zipfRanksLog.jpg",rasterized=True)


fig, ax1 = plt.subplots()
ax1.plot(np.log10(r),np.log10(k),'-',color=green[0])
ax1.set_xlabel(r"$\log_{10}{r}$")
ax1.set_ylabel(r"$\log_{10}{k_r}$")
#plt.savefig("zipfRanksLogLine.pdf",rasterized=True)
#plt.savefig("zipfRanksLogLine.png")
plt.savefig("zipfRanksLogLine.jpg",rasterized=True)






