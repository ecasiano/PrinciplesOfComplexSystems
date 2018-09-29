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
            
    

'''---Main---'''
tmax = 100 #max-time step
rho = 0.025

elephantGroups = RGR(rho,tmax)

#Sort elephant groups (ascending order) to determine ranking of each group
elephantGroups = np.sort(elephantGroups)[::-1]
ranks = np.arange(np.size(elephantGroups),dtype=int)

#Get probabilities of getting elephant
#print(elephantGroups)

'''---Plot---'''

fig, ax3 = plt.subplots()
ax3.plot(ranks,elephantGroups,'.',color=blue[0],label=r"$\langle k_{max} \rangle \propto N^{%.4f}$")
ax3.loglog()
ax3.set_xlabel(r"$Rank, r$")
#ax2.set_ylabel(r"$P_k = {\zeta(\frac{5}{2})}^{-1}k^{-5/2}$")
ax3.set_ylabel(r"$k_r$")
#plt.legend(loc='best')
#ax3.set_xlim(1,300)
#ax3.set_ylim(45,100)

plt.savefig("rgr_zipf.pdf",rasterized=True)
    


