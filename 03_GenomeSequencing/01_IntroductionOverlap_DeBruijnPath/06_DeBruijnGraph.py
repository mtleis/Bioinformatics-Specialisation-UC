# Input: An integer k and a string Text.
# Output: DeBruijnk(Text), in the form of an adjacency list.
from collections import defaultdict

def DeBruijn(Text, k):
    deBruijn = defaultdict(list)
    t = len(Text)
    for i in range(0, t - k + 1):
        kmer = Text[i:i+k-1]
        deBruijn[kmer].append(Text[i+1:i+k])
    return deBruijn

# print(DeBruijn('ACTGCTA', 3))
# result = DeBruijn('ACTGCTA', 3)
# Fetch Input
inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/dataset_199_6.txt'
inputFile = open(inputDirectory, 'r')
k = int(inputFile.readline())
text = str(inputFile.readline())
text = text.replace('\n','')

text = 'TAATGGGATGCCATGTT'
k = 3
inputFile.close()
#print(*DeBruijn(str(text),int(k)), sep='\n')
result = DeBruijn(text, k)
# Change format into XXX->YYY
output = []
for key, values in result.items():
    line = key
    for value in values:
        if '->' in line:
            line = line + ',' + value
        else:
            line = line + ' -> ' + value
    output.append(line)

print(*output, sep='\n')
