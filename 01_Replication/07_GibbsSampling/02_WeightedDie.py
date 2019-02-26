# first, import the random package
import random

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    i = 0
    cumProb = {}
    for key in Probabilities:
        if i == 0:
            cumProb[i] = Probabilities[key]
        else:
            cumProb[i] = Probabilities[key] + cumProb[i-1]
        if p < cumProb[i]:
            kmer = key
            return kmer
        i = i + 1

    return kmer

dict = {'AA':0.5, 'G':0.1, 'C':0.1, 'T':0.1}
res = WeightedDie(dict)
print(res)