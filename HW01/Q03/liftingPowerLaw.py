#Emanuel Casiano-Diaz - September 1, 2018.
#Computes the power-law scaling of lifted weight as a function of lifter's body mass

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
    
    def normedPowerLaw(x,y,p):
        '''Input: x and y data (arrays of real numbers), power law factor p'''
        '''Output: Normalized max value of y and corresponding x'''
        normedY = y/(x**p)
        return normedY

    "--------------------------------------------------------------------"

    #Main

    #Weight lifting records as of September 2018:
    #https://en.wikipedia.org/wiki/Olympic_weightlifting#Competition

    #Men
    mb = np.array((56,62,69,77,85,94,105)) #Lifter body mass in kilograms
    
    #Lifted masses by event (snatch, clean & jerk, total)(in kilograms)
    ms = np.array((139,154,166,177,187,189,200))
    mcj = np.array((171,183,198,214,220,233,246))
    mt = np.array((307,333,359,380,396,417,437))
    
    #Find prefactor and exponent for each event
    A_s , p_s = findPowerLaw(mb, ms)
    A_cj , p_cj = findPowerLaw(mb, mcj)
    A_t , p_t = findPowerLaw(mb, mt)
    
    #Determine the strongest lifter relative to body mass,
    #normalized by the power law factor
    msNormed = normedPowerLaw(mb,ms,p_s)
    mcjNormed = normedPowerLaw(mb,mcj,p_cj)
    mtNormed = normedPowerLaw(mb,mt,p_t)
    
    "--------------------------------------------------------------------"
    #Plot
    mbFit = np.linspace(56,105,1000)
    msFit = A_s*mbFit**p_s
    mcjFit = A_cj*mbFit**p_cj  
    mtFit = A_t*mbFit**p_t     

    fig, ax1 = plt.subplots()
    ax1.plot(mb,mt,'^',mfc=red[3],mew=0.75,color=red[1],label="Total",zorder=3)
    ax1.plot(mbFit, mtFit, '-',color=red[1],label='',linewidth=1)
    ax1.plot(mb,mcj,'s',mfc=green[3],mew=0.75,color=green[1],label="Clean and Jerk",zorder=3)
    ax1.plot(mbFit, mcjFit, '-',color=green[1],label='',linewidth=1)
    ax1.plot(mb,ms,'o',mfc=blue[3],mew=0.75,color=blue[1],label="Snatch",zorder=3)
    ax1.plot(mbFit, msFit, '-',color=blue[1],label='',linewidth=1)
    ax1.set_xlabel("Body mass (kg)")
    ax1.set_ylabel("Lifted mass (kg)")
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax1.loglog()
    ax1.legend(loc=(0.016,0.33),fontsize=9,frameon=False,handlelength=1,handleheight=1,title='',ncol=1)
    ax1.text(80,325,r'$M_T \propto M_{B}^{%.4f}$' % (p_t))
    ax1.text(80,250,r'$M_{CJ} \propto M_{B}^{%.4f}$' % (p_cj))
    ax1.text(80,150,r'$M_S \propto M_{B}^{%.4f}$' % (p_s))

    plt.savefig("liftingPowerLaw.pdf")
    
    #Plot normalized strengths
    mbFit = np.linspace(56,105,1000)
    msFit = (A_s*mbFit**p_s)/(mbFit**p_s)
    mcjFit = (A_cj*mbFit**p_cj)/(mbFit**p_cj)
    mtFit = (A_t*mbFit**p_t)/(mbFit**p_t)
    
    #Determine largest normalized mass for each category
    mtNormedMaxIdx = np.argmax(mtNormed)
    mcjNormedMaxIdx = np.argmax(mcjNormed)
    msNormedMaxIdx = np.argmax(msNormed)

    fig, ax1 = plt.subplots()
    ax1.plot(mb,mtNormed,'^',mfc=red[3],mew=0.75,color=red[1],label=r"$M_T / M_B^{%.4f}$"%(p_t),zorder=3)
    ax1.plot(mb[mtNormedMaxIdx],np.max(mtNormed),'o',markersize=12,mfc='None',mew=0.75,color=red[0],zorder=4)
    ax1.plot(mbFit, mtFit, '-',color=red[1],label='',linewidth=1)
    ax1.text(mb[mtNormedMaxIdx]-5,31,r'$M_B=%d kg$'%(mb[mtNormedMaxIdx]))
   
    ax1.plot(mb,mcjNormed,'s',mfc=green[3],mew=0.75,color=green[1],label=r"$M_{CJ} / M_B^{%.4f}$"%(p_cj),zorder=3)
    ax1.plot(mb[mcjNormedMaxIdx],np.max(mcjNormed),'o',markersize=12,mfc='None',mew=0.75,color=green[0],zorder=4)
    ax1.plot(mbFit, mcjFit, '-',color=green[1],label='',linewidth=1)
    ax1.text(mb[mcjNormedMaxIdx]-2,19,r'$%d kg$'%(mb[mcjNormedMaxIdx]))

    ax1.plot(mb,msNormed,'o',mfc=blue[3],mew=0.75,color=blue[1],label=r"$M_S / M_B^{%.4f}$"%(p_s),zorder=3)
    ax1.plot(mb[msNormedMaxIdx],np.max(msNormed),'o',markersize=12,mfc='None',mew=0.75,color=blue[0],zorder=4)
    ax1.plot(mbFit, msFit, '-',color=blue[1],label='',linewidth=1)
    ax1.text(mb[msNormedMaxIdx]-2,19,r'$%d kg$'%(mb[msNormedMaxIdx]))
   
    ax1.set_xlabel(r"Body mass $(kg)$")
    ax1.set_ylabel("Normalized Lifted Score")
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax1.loglog()
    ax1.legend(loc=(0.016,0.38),fontsize=10,frameon=False,handlelength=1,handleheight=1,title='',ncol=1)
    
    plt.savefig("liftingPowerLawNormed.pdf")
