# StringSpelledByGappedPatterns(GappedPatterns, k, d)
# FirstPatterns ← the sequence of initial k - mers from GappedPatterns
# SecondPatterns ← the sequence of terminal k - mers from GappedPatterns

# PrefixString ← StringSpelledByPatterns(FirstPatterns, k)
# SuffixString ← StringSpelledByPatterns(SecondPatterns, k)
# for i = k + d + 1 to | PrefixString |
#   if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
#       return "there is no string spelled by the gapped patterns"
# return PrefixString concatenated with the last k + d symbols of SuffixString
def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    # assuming patterns in format XXXX | XXXX
    FirstPatterns  = []
    SecondPatterns = []
    for pattern in GappedPatterns:
        split = pattern.split('|')
        FirstPatterns.append(split[0])
        SecondPatterns.append(split[1])
    PrefixString = StringSpelledByPatterns(FirstPatterns)
    SuffixString = StringSpelledByPatterns(SecondPatterns)

    end = len(PrefixString)
    start = k + d + 1
    for i in range(start, end):
        if PrefixString[i] != SuffixString[i-k-d]:
            return -1 # no string spelled by the gapped patterns
    nonOverlappingSuffix = len(SuffixString) - (k+d)
    return PrefixString + SuffixString[nonOverlappingSuffix:]


## Same as GenomePathToString implemented in first Module ('01_Introduction...')
def StringSpelledByPatterns(path):
    text = ''
    text = text + path[0]
    k = len(path[0])
    for i in range(1, len(path)):
        line = path[i]
        text = text + line[k-1:k]
    return text

from collections import defaultdict
GappedPatterns = defaultdict()
GappedPatterns = [
'GACC|GCGC',
'ACCG|CGCC',
'CCGA|GCCG',
'CGAG|CCGG',
'GAGC|CGGA' ]


print(StringSpelledByGappedPatterns(GappedPatterns, 4,2))

inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/dataset_204_16.txt'
inputFile = open(inputDirectory, 'r')
# inputFile.readline()
firstline = inputFile.readline()
firstline = firstline.replace('\n', '')
inputs = firstline.split(' ')

k = int(inputs[0])
d = int(inputs[1])
inputLines = inputFile.readlines()
gappedpattern = []
for line in inputLines:
    line = line.replace('\n', '')
    if '|' in line:
        gappedpattern.append(line)

inputFile.close()
print(StringSpelledByGappedPatterns(gappedpattern, k,d ))
#print('->'.join(EulerianPath(graph)))