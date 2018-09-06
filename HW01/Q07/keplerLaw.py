#Emanuel Casiano-Diaz - September 5, 2018.
#Plots square of the orbital period and cube of orbital radius
#of planets in the Solar System to test Kepler's Law

import numpy as np
import matplotlib.pyplot as plt
from math import log
from scipy.stats import linregress
import colors

with plt.style.context('../../IOP_large.mplstyle'):

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
    def findPowerLaw(x,y):
        '''Input: x and y data (arrays of real numbers)'''
        '''Output: Prefactor and exponent of power law scaling''' 

        #Perform linear regression of x,y data
        p , logA = np.polyfit(np.log10(x),np.log10(y),deg=1)
        A = 10**(logA)
        #p: exponent, A: prefactor

        return A,p
    
    def normedPowerLaw(x,y,p):
        '''Input: x and y data (arrays of real numbers), power law factor p'''
        '''Output: Normalized max value of y and corresponding x'''
        normedY = y/(x**p)
        return normedY
        
    "--------------------------------------------------------------------"

    #Main

    #Orbital periods (in days) and radii (in 10^6 km) for planets in the Solar System
    #https://nssdc.gsfc.nasa.gov/planetary/factsheet/

    data = np.loadtxt("keplerLawData.dat")
    r = data[:,0]    #radii 
    T = data[:,1]    #periods
    
    #Do least squares fitting of T^2 vs. r^3 to determine goodness of fit
    slope, intercept, r_value, p_value, std_err = linregress(r**3,T**2)
    rSquared = r_value**2
    
    "--------------------------------------------------------------------"
    #Plot
    rFit = np.linspace(r[0],r[-1],1000)
    T2Fit = slope*(rFit**3)+intercept
    
    fig, ax1 = plt.subplots()
    ax1.plot(r**3,T**2,'*',markersize=10,mfc=violet[3],mew=0.75,color=violet[1],zorder=3)
    ax1.plot(rFit**3,T2Fit, '-',color=violet[1],label='',linewidth=1)
    ax1.set_xlabel(r"$r^3 (km^3)$")
    ax1.set_ylabel(r"$T^2 (days^2)$")
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    #ax1.loglog()
    #ax1.legend(loc=(0.016,0.33),fontsize=9,frameon=False,handlelength=1,handleheight=1,title='',ncol=1)
    ax1.text(1.17E+29,0.13E+10,r"$R^2 = %.5f$"%(rSquared),fontsize=10)
    ax1.text(0.74E+29,0.2E+10,r"$T^2 = (%.2E) r^3 - (%.2E)$"%(slope,-intercept),fontsize=10)
    
    plt.savefig("keplerLawPlot.pdf")
    
    