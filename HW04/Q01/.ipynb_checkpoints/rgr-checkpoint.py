#Code up the rich-get-richer model

import numpy as np
import matplotlib.pyplot as plt
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

def RGR(innovationRate,totalTimeSteps):
    #t = 1
    elephantGroups = np.ones(1) #Initial elephant
    
    #t > 1
    for t in range(1,totalTimeSteps):
        r = np.random.random() #Uniformly distributed random number from [0,1)
        if r < innovationRate: #Mutation
            elephantGroups = np.append(elephantGroups,1) #Creates elephant of new flavor
        else: #Replication
            if np.size(elephantGroups) > 1:
                flavor = np.random.randint(1,np.size(elephantGroups)) #Select existing flavor randomly
                elephantGroups[flavor] += 1 #Replicate elephant of the randomly selected flavor
            else: 
                elephantGroups[0]+=1
    return elephantGroups

def findPowerLaw(x,y):
    '''Input: x and y data (arrays of real numbers)'''
    '''Output: Prefactor and exponent of power law scaling''' 

    #Perform linear regression of x,y data
    p , logA = np.polyfit(np.log10(x),np.log10(y),deg=1)
    A = 10**(logA)
    #p: exponent, A: prefactor

    return A,p
            
'''---Main---'''
tmax = 100000 #max-time step
rho = 0.1

#Implement the Rich-Get-Richer Model for tmax
#time steps and rho innovation rate
elephantGroups = RGR(rho,tmax)

#Sort elephant groups (ascending order) to determine ranking of each group
elephantGroups = np.sort(elephantGroups)[::-1]
ranks = np.arange(np.size(elephantGroups),dtype=int)

#Find power-law of Zipf-distribution
A,p = findPowerLaw(ranks[1:],elephantGroups[1:])

print("Zipf exponent: %.4f"%-p, 1-rho)

#Get probabilities of getting elephant
#print(elephantGroups)

'''---Plot---'''

#Prepare Fit
ranksFit = np.linspace(1,ranks[-1],np.size(ranks[1:]))
elephantGroupsFit = A*ranksFit**p

fig, ax3 = plt.subplots()
ax3.plot(ranks,elephantGroups,'.',color=blue[0],label=r"$\alpha = %.3f$"%(-p))
ax3.plot(ranks[5],elephantGroups[4],'.',color=blue[0],label=r"$1-\rho = %.3f$"%(1-rho))
ax3.loglog()
ax3.set_xlabel(r"$Rank, r$")
ax3.set_ylabel(r"$s_r$")
ax3.text(0.10, 0.20,r"$\rho = %.3f$"%rho, transform=ax3.transAxes)
plt.legend(loc='best')
#ax3.set_xlim(1,300)
#ax3.set_ylim(45,100)

#plt.savefig("rgr_zipf_rho%.3f.pdf"%rho,rasterized=True)
plt.savefig("Trash.pdf")
plt.clf()

#Do bar chart at time tmax
fig, ax4 = plt.subplots()
ax4.bar(range(1,np.size(elephantGroups)+1),elephantGroups)
ax4.set_ylabel(r"Group Size")
ax4.set_xlabel(r"Elephant Flavors")
ax4.text(0.55, 0.62,r"$\rho = %.3f$"%rho, transform=ax3.transAxes)
ax4.text(0.55, 0.58,r"$t = %d$"%tmax, transform=ax3.transAxes)

plt.savefig("histogram_rho%.3f.pdf"%rho)
    


