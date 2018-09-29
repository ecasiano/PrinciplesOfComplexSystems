#Answers question #7 of homework 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
import colors

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
        
'''---Define Functions---'''

def createSample(sampleSize):
    r = np.random.random(sampleSize) #Uniformly distributed numbers from [0,1)
    Pk = (1/zeta(5/2))*r**(-5/2)
    return Pk

def findPowerLaw(x,y):
    '''Input: x and y data (arrays of real numbers)'''
    '''Output: Prefactor and exponent of power law scaling''' 

    #Perform linear regression of x,y data
    p , logA = np.polyfit(np.log10(x),np.log10(y),deg=1)
    A = 10**(logA)
    #p: exponent, A: prefactor

    return A,p

'''---Main---'''

#Parameters
NList = [10,100,1000,10000,100000,1000000] #Size of each sample
#NList = [10,100,1000,10000] #Set of Sizes of each sample
n = 1000 #Number of Samples

#Create arrays
kmaxList = np.ones(n) #Kmax of each sample
iList = np.arange(1,n+1,dtype=int) #Sample numbers
kmaxAverageList = np.ones(np.size(NList)) #Average Kmax for each set of N-size samples

#Initialize kmax
for j in range(np.size(NList)):
    N = NList[j]
    kmaxList = np.ones(n) #Kmax of each sample
    for i in range(n):
        kmax = np.argmax(createSample(N)+1)
        kmaxList[i] = kmax
    kmaxAverageList[j] = np.mean(kmaxList)
    
#Get power-law prefactor and scaling exponent
A,p = findPowerLaw(NList,kmaxAverageList)

'''---Plot---'''
print(findPowerLaw(NList,kmaxAverageList)[1])

fig, ax2 = plt.subplots()
ax2.plot(NList,kmaxAverageList,'.',color=violet[0],label=r"$\langle k_{max} \rangle \propto N^{%.4f}$"%p)
ax2.loglog()
ax2.set_xlabel(r"$Sample Size, N$")
#ax2.set_ylabel(r"$P_k = {\zeta(\frac{5}{2})}^{-1}k^{-5/2}$")
ax2.set_ylabel(r"$\langle k_{max} \rangle_{N}$")
plt.legend(loc='best')

plt.savefig("kmaxAverageVsSampleSize.pdf",rasterized=True)
    
