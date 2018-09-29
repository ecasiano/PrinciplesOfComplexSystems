#Count the unique and total word count in James Joyce's
#Ulysses to determine the innovation rate.

import numpy as np

'''--------Define Functions--------'''


def innovationRate(things,frequencyOfThings):
    uniqueThings = 0
    totalThings = 0
    for i in range(np.size(things)):
        uniqueThings += 1
        totalThings += frequencyOfThings[i]
    print(totalThings)
    return uniqueThings/totalThings

def groupFractions(frequencyOfThings,desiredFrequency):
    thingsWithDesiredFrequency = 0
    totalThings = 0
    for i in range(np.size(frequencyOfThings)):
        if frequencyOfThings[i] == desiredFrequency:
            thingsWithDesiredFrequency += 1
        #totalThings += frequencyOfThings[i]
        totalThings += 1

        
    print(totalThings)
    return thingsWithDesiredFrequency/totalThings


'''--------Main--------'''
#Load data
data = np.genfromtxt("ulysses.txt",delimiter=":")
words = data[:,0]
wordFrequency = data[:,1]

rho = innovationRate(words,wordFrequency)

n1g = groupFractions(wordFrequency,1)
n2g = groupFractions(wordFrequency,2)
n3g = groupFractions(wordFrequency,3)


print("Innovation Rate: %.4f"%rho)
print("1-groups fraction: %.4f"%n1g)
print("2-groups fraction: %.4f"%n2g)
print("3-groups fraction: %.4f"%n3g)