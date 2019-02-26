# import Python's 'random' module here
import random

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

# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    list = []
    for i in range(t):
        Dna[i]
        num = random.randint(1, len(Dna[i])-k)
        kmer = Dna[i][num:num+k]
        list.append(kmer)
    return list

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

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    consensus = ""
    k = len(Motifs[0])
    count = Count(Motifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

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

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    result = 1
    counter = 0
    for symbol in Text:
        result *= Profile[symbol][counter]
        counter += 1
    return result

def ProfileMostProbableKmer(text, k, profile):
    # loop through every k-mer in text
    t = len(text)
    min = 0
    mostProbableKmer = text[0:k]
    for i in range(t-k+1):
        kmer = text[i:i+k]
        pr = Pr(kmer, profile)
        if pr > min:
            mostProbableKmer = kmer
            min = pr
    return mostProbableKmer

def GreedyMotifSearch(Dna, k, t):
   # Initialize BestMotifs to be the first k-mer in the DNA
   BestMotifs = []
   for i in range(t):
      BestMotifs.append(Dna[i][0:k])

   n = len(Dna[0])
   for i in range(n - k + 1):
      Motifs = []
      Motifs.append(Dna[0][i:i + k])
      for j in range(1, t):
         P = Profile(Motifs[0:j])
         Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
         if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
   return BestMotifs

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
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    # Initialize BestMotifs to be the first k-mer in the DNA
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs



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


# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
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
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p


# Write your ProfileMostProbableKmer() function here.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
    # loop through every k-mer in text
    t = len(text)
    min = 0
    mostProbableKmer = text[0:k]
    for i in range(t-k+1):
        kmer = text[i:i+k]
        pr = Pr(kmer, profile)
        if pr > min:
            mostProbableKmer = kmer
            min = pr

    return mostProbableKmer


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


Motifs = ["ATGCA", "TGGCA", "ATGCT"]
print(Count(Motifs))
print(Profile(Motifs))
print(Consensus(Motifs))
print(Score(Motifs))
print(ProfileMostProbableKmer('ATGCA', 3, Profile(Motifs)))
print(GreedyMotifSearch(Motifs, 2,1))