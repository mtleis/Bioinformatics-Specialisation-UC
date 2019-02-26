# first, import the random package
import random

# then, copy Pr, Normalize, and WeightedDie below this line

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    print('p', p)
    i = 0
    cumProb = {}
    for key in Probabilities:
        print('key', key)
        if i == 0:
            cumProb[i] = Probabilities[key]
        else:
            cumProb[i] = Probabilities[key] + cumProb[i-1]
        if p < cumProb[i]:
            kmer = key
            return kmer
        i = i + 1

    return kmer

# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    result = {}
    sum = 0
    for key in Probabilities:
        sum += Probabilities[key]
    for key in Probabilities:
        result[key] = Probabilities[key]/sum
    return result

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    result = 1
    counter = 0
    for symbol in Text:
        result *= Profile[symbol][counter]
        counter += 1
    return result

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    n = len(Text)
    probabilities = {}

    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)



Text = 'AAACCCAAACCC'
profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
k = 2

print(ProfileGeneratedString(Text, profile, k))