#MotifEnumeration(Dna, k, d)
#        Patterns ← an empty set
#        for each k-mer Pattern in the first string in Dna
#            for each k-mer Pattern’ differing from Pattern by at most d mismatches
#                if Pattern' appears in each string from Dna with at most d mismatches
#                    add Pattern' to Patterns
#        remove duplicates from Patterns
#        return Patterns
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/02_ReplicationOriginSkew')
NG = __import__('08_Neighbors')

# Dna is a list
# find all (k, d)-motifs in Dna
def MotifEnumeration(Dna, k, d):
    Patterns = []
    for i in range(0, len(Dna[0])-k+1):
        Pattern = Dna[0][i:i+k]
        Neighbors = NG.Neighbors(Pattern, d)
        # for j in range(0, len(Neighbors)):
            #Neighbors[j]
        for neighbor in Neighbors:
            if existInDna(neighbor, Dna, d):
                Patterns.append(neighbor)
        Patterns = set(Patterns)
        Patterns = list(Patterns)
    return Patterns

def existInDna(neighbor, Dna, d):
    for i in range(0, len(Dna)):
        found = False
        newNeighbors = NG.Neighbors(Dna[i], d)
        for newNeigbor in newNeighbors:
            if neighbor in newNeigbor:
                found = True
                break
        # if not found in any of the string in the Dna list:
        if found == False:
            return False
    # at the end of the search, found was never false
    return True

#Dna = ['ATCGTAGCATCG', 'ATCGTAGCAACC', 'ATCGTAGCATCG']
#Dna = ['AGACGAGCTAGTCCTGAGGTCTCCC', 'AGCTAGTGCGACGCGATTTTATGTG', 'AGGTATAGCCTTGACTGTTTCGGCG', 'GTTCCTCCGCAGTTACGGTCGGGAT', 'ACGTGAGATATTACTTAGTTGGCAG', 'ACCGGAGTTAGGTCTGAGATACCTA']
#k = 5
#d = 1
#print(*MotifEnumeration(Dna, k, d))
import math


def log(n):
    return math.log2(n)

print(-(4*0.2*log(0.2) + 8*0.1*log(0.1) + 2*0.3*log(0.3) + 3* 0.4 * log(0.4)  +
        + 0.5 * log(.5) + 2*0.6*log(0.6) + 2*0.7*log(0.7) + 0.8*log(.8)
        + 3* 0.9* log(0.9) + 2 * log(1) ))
#print('Probability of Pattern:', 0.7*0.6*1*)
