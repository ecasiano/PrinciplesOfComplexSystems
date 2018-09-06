#Emanuel Casiano-Diaz - September 6, 2018.
#Given the surface area as a function of volume for allometric scaling
#of Minecraft organisms, determine the scaling exponents that will make
#S(V) converge faster.

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
    def S(V,gamma1,gamma2,gamma3):
        return 1*(1 + V**-(abs(gamma1-gamma2)) + V**-(abs(gamma1-gamma3)))
        
    "--------------------------------------------------------------------"

    #Plot
    V = np.linspace(0,2000.1,10000)
    
    fig, ax1 = plt.subplots()
    ax1.plot(V,S(V,1/3,1/3,1/3), '-',color=violet[1],label=r'($\frac{1}{3},\frac{1}{3},\frac{1}{3}$)',linewidth=1)
    ax1.plot(V,S(V,1/4,1/4,1/2), '-',color=blue[1],label=r'($\frac{1}{4},\frac{1}{4},\frac{1}{2}$)',linewidth=1)
    ax1.plot(V,S(V,0,0,1), '-',color=green[1],label=r'($0,0,1$)',linewidth=1)
    ax1.plot(V,S(V,0,1/4,3/4), '-',color=orange[1],label=r'($0,\frac{1}{4},\frac{3}{4}$)',linewidth=1)
    ax1.plot(V,S(V,0,1/2,1/2), '-',color=red[1],label=r'($0,\frac{1}{2},\frac{1}{2}$)',linewidth=1)
    ax1.plot(V,1*np.ones(np.size(V)),'--',color="#aaaaaa")
    ax1.set_xlabel(r"$V [L^3]$")
    ax1.set_ylabel(r"$S(V) [L^2]$")
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax1.set_ylim(0.8,3.2)
    ax1.set_xlim(-5,2000.1)
    ax1.legend(loc=(0.24,0.16),fontsize=9,frameon=False,handlelength=1,handleheight=1,title=r'($\gamma_1,\gamma_2,\gamma_3$)',ncol=3)
    ax1.text(750,2.6,r"$S(V) = 1 + \frac{1}{V^{|\gamma_1 - \gamma_2|}} + \frac{1}{V^{|\gamma_1 - \gamma_3|}}$",fontsize=10)    
    plt.savefig("minecraftConvergence.pdf")
    
    