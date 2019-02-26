# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    Motifs = RandomMotifs(Dna, k, t)
    #print('Motifs ', Motifs)
    # ﻿BestMotifs ← Motifs
    BestMotifs = Motifs.copy()

    for j in range(1,N):
        ##print('Motifs 1 ', Motifs)
        i = random.randint(0,t-1)
        ##print('i', i)
        #print('i', i)
        #print('Motifs[i]', Motifs[i])
        Motifs.remove(Motifs[i])
        #print('Motifs 2', Motifs)
        profile = ProfileWithPseudocounts(Motifs)
        ##print('profile', profile)
        ##print('i', i)
#        kmer = ProfileGeneratedString(Dna[i], profile, k)
        ##print('kmer', kmer)
        # Motifs.append(ProfileGeneratedString(Dna[i], profile, k))
        Motifs.insert(i, ProfileGeneratedString(Dna[i], profile, k))
        #print('Motifs', Motifs)
        #print('Score ' , Score(Motifs))
        #print('Score(Best) ', Score(BestMotifs))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs.copy()

    return BestMotifs



# place all subroutines needed for GibbsSampler below this line
def RandomMotifs(Dna, k, t):
    list = []
    for i in range(t):
        Dna[i]
        num = random.randint(1, len(Dna[i])-k)
        kmer = Dna[i][num:num+k]
        list.append(kmer)
    return list


# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    count = Count(Motifs)
    for symbol in 'ACGT':
        profile[symbol] = []

    for i in range(k):
        sum = 0
        for symbol in 'ACGT':
            sum = sum + count[symbol][i]

        for symbol in 'ACGT':
            profile[symbol].append(count[symbol][i]/sum)

    return profile


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    ##print('Text', Text)
    n = len(Text)
    ##print('n', n)
    probabilities = {}

    for i in range(0, n-k+1):
        ##print('i', i)
        ##print('Text i+k:', Text[i:i+k])
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    ##print('probab ', probabilities)
    probabilities = Normalize(probabilities)
    ##print('prob ', probabilities)
    return WeightedDie(probabilities)


# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for i in range(len(Motifs)):
        for k in range(len(consensus)):
            if consensus[k] != Motifs[i][k]:
                score += 1
    return score


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


def Consensus(Motifs):
    consensus = ""
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


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


def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    count = CountWithPseudocounts(Motifs)
    for symbol in 'ACGT':
        profile[symbol] = []

    for i in range(k):
        sum = 0
        for symbol in 'ACGT':
            sum = sum + count[symbol][i]

        for symbol in 'ACGT':
            profile[symbol].append(count[symbol][i] / sum)

    return profile
#k = 8
#t = 5
#N = 100
#Dna = [
#'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
#'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
#'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
#'AATCCACCAGCTCCACGTGCAATGTTGGCCTA' ]
#
##print('Result : ', GibbsSampler(Dna, k, t, N))


# Test Dataset:
k = 5
t = 10
dna = [
'TGGTACCGGTCACGCTCTCCCGCCCCTGGTA',
'CCGGTGAGGCCACGCTCTCCCGCCCCTGGTA',
'GTCAAGACAAATGCCCACCAGACCCCTTCGA',
'CTTGCGGGCGTGTTCAAGATGTTGGGGGATA',
'AGACCATTTTGGTGACAGTACGGGGCGCGGT',
'TAAGTGATGTCCGATTCACGAAGTGTCCGTT',
'GAATATTAGGGTTTTGTCAAGAACTATGTTT',
'TGGGTTAAATGGAGACGTACTTCCACCGACG',
'TTGAGCGTAGGTGAAGAGGGTTGAGAACAGA',
'AGGACTCGAAGCACCTCAACTTGTGAGCGGT' ]
N=100

print (GibbsSampler(dna, k, t, N))
# Your output
 # ['GTCCG', 'GACCA', 'GGCCA', 'GACAA', 'GACAA', 'GAACA', 'GACAA', 'CACCA', 'GTCCG', 'GAACA']

# Correct output:
# ['CACGC', 'CACGC', 'CAAGA', 'CAAGA', 'CGCGG', 'CACGA', 'CAAGA', 'GACGT', 'GAAGA', 'CTCGA']