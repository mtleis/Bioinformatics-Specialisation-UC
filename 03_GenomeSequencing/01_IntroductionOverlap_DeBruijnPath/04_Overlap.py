# Input: A collection Patterns of k - mers.
# Output: The overlap graph Overlap(Patterns), in the form of an adjacency list (dictionary).
from collections import defaultdict
def Overlap(patterns):
    graph = defaultdict(list)
    for pattern in patterns:
        suffix = pattern[1:len(pattern)]
        for nextpattern in patterns:
            prefix = nextpattern[0:len(nextpattern)-1]
            if suffix == prefix:
                graph[pattern].append(nextpattern)

    # Remove duplicate values
    result = defaultdict(list)
    for key, values in graph.items():
        for value in values:
            if value not in result[key]:
                result[key].insert(0, value)
    return result

dna = ['ACTG', 'CTGC', 'ATTC', 'CTGA', 'AAAA']
# print(*Overlap(dna), sep='\n')
result = Overlap(dna)
# Change format into XXX->YYY
formatted = []
for key, values in result.items():
    line = key
    for value in values:
        if '->' in line:
            line = line + ',' + value
        else:
            line = line + '->' + value
    formatted.append(line)
print(*formatted, sep='\n')
for pattern, adjacencies in result.items():
    if len(adjacencies) > 0:
        print(pattern, '->', ','.join(adjacencies))

# Fetch Input
#inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/dataset_198_10.txt'
#inputFile = open(inputDirectory, 'r')
#dna = list()
#lines = inputFile.readlines()
#for line in lines:
#    line = line.replace('\n', '')
#    dna.append(line)
#inputFile.close()
#print(*Overlap(dna), sep='\n')

# This code worked for submission
#import sys
#Input = sys.stdin.readlines()
#patternList = [pattern.strip() for pattern in Input]
#overlapList = Overlap(patternList)
#for pattern, adjacencies in overlapList.items():
#    if len(adjacencies) > 0:
#        print(pattern, '->', ','.join(adjacencies))