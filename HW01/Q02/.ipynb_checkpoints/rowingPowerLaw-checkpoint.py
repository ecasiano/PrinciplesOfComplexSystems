#Emanuel Casiano-Diaz - September 1, 2018.
#Computes the power-law scaling of boat speed as a function of oarspeople

import numpy as np
import matplotlib.pyplot as plt
from math import log
import colors

with plt.style.context('../../IOP_large.mplstyle'):

    #Some nice pastel colors
    red = ["#e85c47"]
    blue = ["#4173b3"]
    orange = ["#ff8c00"]
    green = ["#7dcca4"]    

    alpha = [0.8,0.5,0.1]

    for i,c in enumerate(alpha):
            red.append(colors.get_alpha_hex(red[0],alpha[i]))
            orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
            green.append(colors.get_alpha_hex(green[0],alpha[i]))
            blue.append(colors.get_alpha_hex(blue[0],alpha[i]))

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

    "--------------------------------------------------------------------"

    #Main

    #Best rowing times (2000m) as of September 2018:
    #(https://en.wikipedia.org/wiki/List_of_world_records_in_rowing)
    #http://www.worldrowing.com/events/statistics/

    #Men
    times = np.array((390.74, 368.50, 337.86, 318.68)) #seconds
    distance = 2000 #meters
    V = distance/times
    V = V * (1/1000) * (3600) #Convert speeds to km/hr
    N = ((1,2,4,8))

    A , p = findPowerLaw(N, V)
    
    #Women
    times = np.array((427.71, 409.08, 374.36, 354.16)) #seconds
    V_w = distance/times
    V_w = V_w * (1/1000) * (3600) #Convert speeds to km/hr
    
    A_w , p_w = findPowerLaw(N, V_w)

    print("Prefactor: %.4f (M), %.4f (W)" % (A,A_w))
    print("Exponent: %.4f (M), %.4f (W)" % (p,p_w))

    "--------------------------------------------------------------------"
    #Plot
    Nfit = np.linspace(1,8,1000)
    Vfit = A*Nfit**p     #Men
    Vfit_w = A_w*Nfit**p_w #Women

    fig, ax1 = plt.subplots()
    ax1.plot(N,V,'o',mfc=blue[3],mew=0.75,color=blue[1],label="Men",zorder=3)
    ax1.plot(Nfit, Vfit, '-',color=blue[1],label='',linewidth=1)
    ax1.plot(N,V_w,'s',mfc=green[3],mew=0.75,color=green[1],label="Women",zorder=3)
    ax1.plot(Nfit, Vfit_w, '-',color=green[1],label='',linewidth=1)
    ax1.set_xlabel("Number of oarspeople")
    ax1.set_ylabel("Speed (km/hr)")
    ax1.axis([0.9,10,10,30.2])
    ax1.set_xticks([1,2,4,8])
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax1.loglog()
    ax1.legend(loc='upper left',fontsize=10,frameon=False,handlelength=1,handleheight=1,title='',ncol=1)
    ax1.text(4,24.5,r'$V \propto N^{%.4f}$' % (p))
    ax1.text(4,16,r'$V \propto N^{%.4f}$' % (p_w))
    plt.savefig("rowingPowerLaw.pdf")
