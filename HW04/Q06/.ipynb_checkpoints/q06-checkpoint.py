#Answers question #6 of homework 4

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

'''---Main---'''

#Parameters
N = 10 #Size of each sample
n = 1000 #Number of Samples

#Create arrays
kmaxList = np.ones(n) #Kmax of each sample
iList = np.arange(1,n+1,dtype=int) #Sample numbers

#Initialize kmax
for i in range(n):
    kmax = np.argmax(createSample(N)+1)
    kmaxList[i] = kmax

'''---Plot---'''

fig, ax1 = plt.subplots()
ax1.plot(iList,kmaxList,'.',color=green[0],label=r"$N = %d$"%N)
ax1.loglog()
ax1.set_xlabel(r"$Sample Number, i$")
#ax1.set_ylabel(r"$P_k = {\zeta(\frac{5}{2})}^{-1}k^{-5/2}$")
ax1.set_ylabel(r"$(k_{max})_i$")
plt.legend(loc='best')

plt.savefig("kmaxVsSampleNumber_N%d.pdf"%N,rasterized=True)
#plt.savefig("zipfRanksLog.png")

#fig, ax1 = plt.subplots()
#ax1.plot(np.log10(r),np.log10(k),'-',color=green[0])
#ax1.set_xlabel(r"$\log_{10}{r}$")
#ax1.set_ylabel(r"$\log_{10}{k_r}$")
#plt.savefig("zipfRanksLogLine.pdf",rasterized=True)
#plt.savefig("zipfRanksLogLine.png")
    