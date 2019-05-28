#ClumpFinding(Genome, k, L, t)
#        FrequentPatterns ← an empty set
#        for i ← 0 to 4k − 1
#            Clump(i) ← 0
#        for i ← 0 to |Genome| − L
#            Text ← the string of length L starting at position i in Genome
#            FrequencyArray ← ComputingFrequencies(Text, k)
#            for index ← 0 to 4k − 1
#                if FrequencyArray(index) ≥ t
#                    Clump(index) ← 1
#        for i ← 0 to 4k − 1
#            if Clump(i) = 1
#                Pattern ← NumberToPattern(i, k)
#                add Pattern to the set FrequentPatterns
#        return FrequentPatterns
ComputingFrequencies = __import__('06_ComputingFrequencies')
NumberToPattern = __import__('05_NumberToPattern')

def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = []
    Clump = {}
    for i in range(0, 4*k):
        Clump[i] = 0
    for i in range(0, len(Genome)-L):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies.ComputingFrequencies(Text,k)
        for index in range(0,4*k):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(0, 4*k):
        if Clump[i] == 1:
            Pattern = NumberToPattern.NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

#print(ClumpFinding('ACCTGCAATTTACG', 2, 8, 1))