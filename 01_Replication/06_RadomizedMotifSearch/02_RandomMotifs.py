## Write a function RandomMotifs(Dna, k, t) that uses random.randint to choose a random k-mer
# from each of t different strings Dna, and returns a list of t strings.
# Then add this function to Motifs.py.

# import Python's 'random' module here
import random

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

k = 3
t = 5
dna = [
'TTACCTTAAC',
'GATGTCTGTC',
'ACGGCGTTAG',
'CCCTAACGAG',
'CGTCAGAGGT'
    ]
RandomMotifs(dna, k, t)