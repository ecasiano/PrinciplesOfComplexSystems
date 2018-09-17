#Emanuel Casiano-Diaz - September 12, 2018.
#INSERT PROGRAM DESCRIPTION

import numpy as np
import matplotlib.pyplot as plt
from math import log
from scipy.stats import linregress
import colors

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
data = np.loadtxt("vocab_cs_mod.txt")
dataSlice = np.loadtxt("vocab_cs_modSliced.txt")

k = data[:,0] #How many times a set of words appears
Nk = data[:,1] #How many words are in the set that appears k times

kSlice = dataSlice[:,0] # Same but in the region where eyeballing
NkSlice = dataSlice[:,1] # says Nk follows a power law in k.

#Eye-balled max
eyeBalledMax = 1E+04

#Find the power law exponent and pre-factor in the region 
#where eye-ballingology says the data follows a power-law.
A,p,r2 = findPowerLaw(kSlice,NkSlice,rSquared=True)

#Use the obtained pre-factor and exponent to perform a fit in the eye-balled region
kFit = np.linspace(kSlice[-1],kSlice[0],1000)
NkFit = A*kFit**p

#Mean and standard deviation of the sample
NkMean = np.mean(Nk)
NkVar = np.var(Nk)
NkStDev = np.std(Nk)

print("---Nk---")
print("k Bounds: low: %.2E high: %.2E"%(k[-1],k[0]))
print("Power Law Exponent: %.4f"%(p))
print("Mean: %.4f"%(NkMean))
print("Variance: %.4f"%(NkVar))
print("Standard Deviation: %.4f"%(NkStDev))

"--------------------------------------------------------------------"
#Plot    
fig, ax1 = plt.subplots()
ax1.plot(k,Nk, 'o',color=violet[1],mfc='None',label=r'($\frac{1}{3},\frac{1}{3},\frac{1}{3}$)',linewidth=0.5,markersize=1.25)
ax1.set_xlabel(r"$N_k$")
ax1.set_ylabel(r"$k$")
ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', labelbottom='on', direction = 'in')
#plt.savefig("wordFrequency.pdf")

fig, ax2 = plt.subplots()
ax2.plot(k,Nk, 'o',color=violet[1],mfc='None',label=r'($\frac{1}{3},\frac{1}{3},\frac{1}{3}$)',linewidth=0.5,markersize=1.25)
ax2.plot(kFit,NkFit, '-',color='black',mfc='None',label=r'($\frac{1}{3},\frac{1}{3},\frac{1}{3}$)',linewidth=0.75)
ax2.set_ylabel(r"$N_k$")
ax2.set_xlabel(r"$k$")
ax2.loglog()
plt.axvspan(k[np.argmax(Nk)],eyeBalledMax, facecolor=orange[1], alpha=0.25)
ax2.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', labelbottom='on', direction = 'in')
ax2.text(2E+05,1E+03,r"$(N_K)_{10^2 \leq k \leq 10^4} \approx (3.67x10^8) k^{-1.70}$",fontsize=12)
ax2.text(2E+05,3E+02,r"$R^2 = %.5f$"%(r2),fontsize=12)
#plt.savefig("wordFrequencyLog.pdf")