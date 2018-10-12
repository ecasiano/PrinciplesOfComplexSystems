#Answers question 3 of HW06.....

import numpy as np
import matplotlib.pyplot as plt

from pylab import *
from scipy.ndimage import measurements


'''---Define Functions---'''

def createLattice(L,p):
    '''Create a LxL lattice with probability of site occupation p'''
    lattice = np.zeros((L,L))
    for i in range(L):
        for j in range(L):
            if p > np.random.random():
                lattice[i][j] = 1
    return lattice

'''---Main---'''

#Parameters
L = 100 #Linear size
N = 100 #Tests per point
probabilities = np.arange(0.01,1.01,0.01)
s_avgs = np.ones(np.size(probabilities))

fig, ax1 = plt.subplots()

#for L in [20,50,100,200,500,1000]:
for L in [5,10,15,20,25]:
    for i,p in enumerate(probabilities):
        s_avg = 0
        for n in range(N):
            #Create the lattice
            lattice = createLattice(L,p)

            #Identify the clusters (or forests)
            lw, num = measurements.label(lattice)

            #Get area of each forest
            area = measurements.sum(lattice, lw, index=arange(lw.max() + 1))

            #Calculate the ratio of largest area to lattice size
            s = np.max(area)/np.size(lattice)
            s_avg += s #Add s fractional areas to get ready to take the average later

        s_avg = s_avg/N #Actually take the average s over N tests
        s_avgs[i] = s_avg #Include element in array of average s's
        
        if(p==probabilities[-1] and n==(N-1)):
            print("L=%d done"%(L))
    ax1.plot(probabilities,s_avgs,label='L = %d'%L)


'''---Plot---'''
#ax1.set_xlabel(r"$p$")
#ax1.set_ylabel(r"$S_{avg}$")
#ax1.text(0.50,0.7,r"H: %.2f"%H,transform=ax1.transAxes)
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
#plt.savefig("forests1.jpg")