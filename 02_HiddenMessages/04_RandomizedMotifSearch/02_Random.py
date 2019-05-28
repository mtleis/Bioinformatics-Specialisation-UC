import random

def Random(probabilities):
    sum = 0
    for key in probabilities:
        sum += probabilities[key]

    # normalize the probabilities, so that they sum to 1
    for key in probabilities:
        probabilities[key] = probabilities[key]/sum

    p = random.uniform(0,1)
    cumProb = {}
    i = 0
    for key in probabilities:
        if i == 0:
            cumProb[i] = probabilities[key]
        else:
            cumProb[i] = probabilities[key] + cumProb[i-1]
        if p < cumProb[i]:
            return i
        i = i + 1
    return -1

#Probabilities = {'a':1, '2':0.9, '3':0.1}
#print(Random(Probabilities))

