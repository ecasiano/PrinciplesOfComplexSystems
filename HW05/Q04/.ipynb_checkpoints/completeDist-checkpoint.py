#Code used to answer question #4 of assignment #5 of CSYS300-2018

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

'''---Define functions---'''

def completeDist(A,p,lowerLimit,upperLimit):
    #Given the pre-factor and scaling exponent of a CCDF,
    #returns the distribution from lowerLimit to upperLimit
    #A = pre-factor, p = scaling exponent
    
    k = np.arange(1,upperLimit+1)
    return A*k**p   

'''---Main---'''

#Parameters
kLow = 1
kHigh = int(1E+07)
A = 3.46E+08
p = -0.661

k = np.arange(kLow,kHigh+1)
Nk = completeDist(A,p,kLow,kHigh)

#Get mean and variance of the sample from k=1 to k=199
mean = np.mean(Nk)
var = np.var(Nk)

#Get the fraction of words that show up only once
N1 = Nk[0] #Number unique words that show up only once
totalWords = np.sum(Nk*k)
uniqueWords = np.sum(Nk) #Total unique words

N1_g = N1/totalWords
Nu_g = uniqueWords/totalWords

##Get the fraction of total words that belong to 1 < k < 200
Nlf_g = np.sum(Nk[0:200]*k[0:200])/totalWords

#Print desired info to the screen
print('''---3b---''')
print("Mean: %.2e"%(mean))
print("Variance: %.2e"%(var))

print("")
print('''---3ci''')

print("Words that show up only once: %.2e"%N1) #Number of distinct words that show up once
print("Total words: %.2e"%totalWords)
print("Fraction of words that show up only once: %.2e"%N1_g)

print("")
print('''---3cii---''')
print("Unique words: %.2e"%uniqueWords)
print("Fraction of unique words: %.2e"%Nu_g)

print("")
print('''---3ciii---''')
print("Fraction of total words left out by providing only words with frequency greater or equal to 200: %.2e"%Nlf_g)
print("Fraction of total words that belong to k>=200: %.2e"%(np.sum(Nk[200:]*k[200:])/totalWords))

'''---Plot---'''

fig, ax1 = plt.subplots()
ax1.plot(k[0:20000],Nk[0:20000],'.',color=violet[0])
ax1.set_xlabel(r"$k$")
ax1.set_ylabel(r"$N_k$")
ax1.loglog()
ax1.text(0.58,0.75,r"$N_k = (%.2e)k^{%.3f}$"%(A,p),transform=ax1.transAxes)
ax1.text(0.1,0.20,r"Average $N_k: %.2e$"%(mean),transform=ax1.transAxes)
ax1.text(0.1,0.10,r"Variance of $N_k: %.2e$"%(var),transform=ax1.transAxes)
plt.savefig("wordFrequencyCCDFLog_extrapolated.pdf",rasterized=True)

