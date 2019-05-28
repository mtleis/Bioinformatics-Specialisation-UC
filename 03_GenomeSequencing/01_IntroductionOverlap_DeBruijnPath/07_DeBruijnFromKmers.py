# Construct DeBruijn Graph from a given set of Kmers
# Input: A collection of K-mer patterns.
# Output: De Bruijn graph.
from collections import defaultdict

def DeBruijnFromKmers(patterns):
    k = len(patterns[0])
    composition = defaultdict(list)
    # sortedComposition = defaultdict(list)
    for pattern in patterns:
        prefix = pattern[0:k-1]
        suffix = pattern[1:k]
        composition[prefix].append(suffix)

    return composition

print(DeBruijnFromKmers(['ACT', 'CTA', 'CTG', 'TAC']))
dna = ['GAGG', 'CAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
result = DeBruijnFromKmers(dna)

import sys
# The following is used for online submission (reading input)
# kmer_list = [line.rstrip() for line in sys.stdin]


# Change format into XXX->YYY
for pattern, adjacencies in result.items():
    if len(adjacencies) > 0:
        print(pattern, '->', ','.join(adjacencies))

#inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/dataset_200_8.txt'
#inputFile = open(inputDirectory, 'r')
#dna = list()
#lines = inputFile.readlines()
#for line in lines:
#    line = line.replace('\n', '')
#    dna.append(line)

#inputFile.close()

result = DeBruijnFromKmers(dna)
# Change format into XXX->YYY
for pattern, adjacencies in result.items():
    if len(adjacencies) > 0:
        print(pattern, '->', ','.join(adjacencies))