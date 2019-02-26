# Code Challenge (2 points): Implement Normalize(Probabilities). Then add this function to Motifs.py.

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

Prob = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T':0.1}

newProb = Normalize(Prob)
print(newProb)

## Quiz-4, Question 6:
Prob = {'A': 0.22, 'B':0.54, 'C':0.58, 'D':0.36, 'E':0.3}
print(Normalize(Prob))

#0.45 0.63 0.09 0.27 0.36

#0.22 0.54 0.58 0.36 0.3
