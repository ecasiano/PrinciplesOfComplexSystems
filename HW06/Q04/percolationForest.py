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
L = 32 #Linear size
N = int(1E+05) #Number of runs
pc = 0.6 #Tree rate
l = np.arange(1,(L**2)+1) #Possible forest sizes
Nl = np.zeros(np.size(l),dtype=int) #Array to store amount of times an l sized forest appears
probabilities = [pc,pc/2,pc+(1-pc)/2]

for p in probabilities:
    print("p = %2f"%p)
    for n in range(N):
        #Create the lattice
        lattice = createLattice(L,p)

        #Identify the clusters (or forests)
        lw, num = measurements.label(lattice)

        #Get area of each forest
        areas = measurements.sum(lattice, lw, index=arange(lw.max() + 1))

        #Run over the areas array
        #print(Nl)
        for a in areas:
            a = int(a)
            if a!=0:
                Nl[a-1]+=1
            #print(Nl)

        #Print statement to show progress
        if((n+1)%(N/10)==0): print("Checkpoint: N=%d"%(n+1))

    #Reshape data for writing into data file
    data = np.c_[l,Nl]
    filename = "forestDistributionsL%dN%dp%.2f.dat"%(L,N,p)
    header = "L = %d, N = %2e, p = %.2f\nl, Nl"%(L,N,p)
    file = np.savetxt(filename,data,fmt="%d",header=header)
                
'''---Plot---'''
#fig, ax1 = plt.subplots()
#ax1.set_xlabel(r"$p$")
#ax1.set_ylabel(r"$S_{avg}$")
#ax1.text(0.50,0.7,r"H: %.2f"%H,transform=ax1.transAxes)
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
#plt.savefig("forests1.jpg")