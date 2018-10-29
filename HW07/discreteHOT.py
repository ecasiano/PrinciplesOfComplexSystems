#Answers question 3 of HW07.....

import numpy as np
import matplotlib.pyplot as plt
from math import e

from pylab import *
from scipy.ndimage import measurements


'''---Define Functions---'''

def emptyForest(L):
    '''Creates empty forest of dimensions LxL'''
    return np.zeros((L,L))

def Pij(i,j,L,l):
    '''Normalized Spark probability at coord i,j with characteristic scale l'''
    A = (1-e**(1/l))**2/(1-e**(-L/l))**2 #Normalization Constant
    return A*e**(-i/l)*e**(-j/l)

def clusterSize(forest,i,j):
        '''Calculate the cluster size of the cluster where the i,j coord lives.'''
        #Identify the clusters (or forests)
        lw, num = measurements.label(forest)
        
        #Return list with sizes of ALL clusters
        area = measurements.sum(forest, lw, index=arange(lw.max() + 1))
        
        cluster = lw[i,j] #Store in cluster the label (or index) given to the cluster where i,j lives
        size = area[cluster]
        
        return size

#def designedPlant(D,p,forest):
def designedPlant(D,p,forest):
    '''Plants a single tree to a forest given: design parameter,D, and spark probability, P'''
    L = np.shape(forest)[0] #Linear Size of forest
    l = L/10
    
    
    #D = design parameter, P = spark probability, p = tree rate (or density)
    for trial in range(D):
        i_zeros = np.where(forest==0)[0] #Find the indices where there are still no trees
        j_zeros = np.where(forest==0)[1]
        i_zeros_size = np.size(i_zeros)
        j_zeros_size = np.size(j_zeros)
        #if (i_zeros_size == 0 or j_zeros_size ==0): break
        i = i_zeros[np.random.randint(i_zeros_size)] #Select the coordinates randomly from the arrays 
        j = j_zeros[np.random.randint(j_zeros_size)] #containing the indices of the unplanted cells
        
        testForest = np.copy(forest)
        testForest[i,j] = 1
        #print(testForest)
        
        cost = 0 #initialize average cost
        for m in range(0,L):
            for n in range(0,L):
                cost += Pij(m+1,n+1,L,l)*clusterSize(testForest,m,n)
        
        #Calculate the yield
        Y = p - cost
        #print(Y)
                
        #Update peak yield
        if trial == 0: 
            Ypeak = Y
            i_peak = i
            j_peak = j
        else:
            if Y > Ypeak:
                Ypeak = Y
                i_peak = i
                j_peak = j
    
    print("Ypeak: %f"%Ypeak)            
    #Plant a tree at coords where peak yield was achieved
    forest[i_peak,j_peak] = 1
            
    

#def createLattice(L,p):
#    '''Create a LxL lattice with probability of site occupation p'''
#    lattice = np.zeros((L,L))
#    for a in range(L):
#        for b in range(L):
#            if p > np.random.random():
#                lattice[i][j] = 1
#    return lattice


#def designedForest():
    

'''---Main---'''

def main():
    
    #Parameters
    L = 32 #Linear size
    l = L/10 #Characteristic Scale
    p = 0.93  #Tree rate (or density)
    D = L     #Design parameter

    #Tests

    #Test emptyForest
    forest = emptyForest(L)
    print(forest)
    print("")

    #Test normalization of Pij
    Psum = 0
    for i in range(1,L+1):
        for j in range(1,L+1):
            Psum += Pij(i,j,L,l)
    print("Sum(P) = %.4f"%(Psum))
    print("")

    #Test clusterSize
    a = np.array(((1,1,1,1,1),(0,0,0,0,1),(0,0,0,0,1),(0,1,1,0,1),(0,1,1,0,1)))
    print(a)
    print("i=0,j=0: ", clusterSize(a,0,0))
    print("i=4,j=1: ", clusterSize(a,4,1))
    print("")

    #Test designedPlant
    #designedPlant(10,0.8,forest)
    #print(forest)

    #Fill up the forest inteligently
    forest = emptyForest(L)

    for n in range(L**2):
        designedPlant(D,p,forest)
        print("%d/%d"%(n+1,L*3))
    
    print(forest)

    #Plot the forest
    plt.imshow(forest,cmap='Greys')
    plt.savefig("HOTForestL32DL.pdf")
    #plt.savefig("HOTForestL32D1.pdf")
    #plt.savefig("HOTForestL32D3.pdf")

    #plt.savefig("HOTForestL32D1.pdf")
    #plt.savefig("HOTForestL32D1.pdf")



if __name__== "__main__":
  main()

'''---Plot---'''
#ax1.set_xlabel(r"$p$")
#ax1.set_ylabel(r"$S_{avg}$")
#ax1.text(0.50,0.7,r"H: %.2f"%H,transform=ax1.transAxes)
#ax1.text(0.50,0.8,"%.d X %.d lattice"%(L,L),transform=ax1.transAxes)
#ax1.text(0.50,0.9,r"MC Time Steps per point: %d"%mcSteps,transform=ax1.transAxes)
#ax1.axvline(x=0.6,color='#888888',linestyle='--',zorder=0)
#plt.legend(loc="best")
#plt.savefig("forests1.jpg")


