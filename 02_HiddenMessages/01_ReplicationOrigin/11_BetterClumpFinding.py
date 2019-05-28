#BetterClumpFinding(Genome, k, t, L)
#        FrequentPatterns ← an empty set
#        for i ← 0 to 4k − 1
#            Clump(i) ← 0
#        Text ← Genome(0, L)
#        FrequencyArray ← ComputingFrequencies(Text, k)
#        for i ← 0 to 4k − 1
#            if FrequencyArray(i) ≥ t
#                Clump(i) ← 1
#        for i ← 1 to |Genome| − L
#            FirstPattern ← Genome(i − 1, k)
#            index ← PatternToNumber(FirstPattern)
#            FrequencyArray(index) ← FrequencyArray(index) − 1
#            LastPattern ← Genome(i + L − k, k)
#            index ← PatternToNumber(LastPattern)
#            FrequencyArray(index) ← FrequencyArray(index) + 1
#            if FrequencyArray(index) ≥ t
#                Clump(index) ← 1
#        for i ← 0 to 4k − 1
#            if Clump(i) = 1
#                Pattern ← NumberToPattern(i, k)
#                add Pattern to the set FrequentPatterns
#        return FrequentPatterns
## Implementation didn't work, still needs debugging
import timeit

ComputingFrequencies = __import__('06_ComputingFrequencies')
#PatternToNumber = __import__('04_PatternToNumber')
PatternToNumber = __import__('04_PatternToNumber2')
NumberToPattern = __import__('05_NumberToPattern')

def BetterClumpFinding(Genome, k, L, t):
    start = timeit.default_timer()
    FrequentPatterns = []
    Clump = {}
    index  = 0
#    for i in range(0, 4**k):
#        Clump[i] = 0
#    print('Initializing array : ', timeit.default_timer() - start )
    Text = Genome[0:L]
    FrequencyArray = ComputingFrequencies.ComputingFrequencies(Text,k)
    print('Computing Frequencies : ', timeit.default_timer() - start )
    for i in range(0, 4**k):
        Clump[i] = 0
        if FrequencyArray[i] >= t:
            Clump[i] = 1
    print('Identifying Clumps : ', timeit.default_timer() - start)
    start = timeit.default_timer()


    print('Just assign i to i', len(Genome), ' times :', timeit.default_timer() - start)
    for i in range(1,len(Genome)-L):
        FirstPattern = Genome[i-1:i-1+k]
        index = PatternToNumber.PatternToNumber(FirstPattern)
        FrequencyArray[index] = FrequencyArray[index] - 1
        LastPattern = Genome[i+L-k:i+L]
        index = PatternToNumber.PatternToNumber(LastPattern)
        FrequencyArray[index] = FrequencyArray[index] + 1
        if FrequencyArray[index] >= t:
            Clump[index] = 1
    print('Sliding through genome : ', timeit.default_timer() - start)
    for i in range(0, 4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern.NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)

    print('Appending patterns: ', timeit.default_timer() - start)
    return FrequentPatterns

#Genome = 'GGTGAGGCTCCAACGCCGGATTGAGTTGAAATAAAGTAAAATCATTCCGAACCGTTGTTCATGGGCTCAGAAGTCGGAGAGCACGTTAGGTGGGGTATGTCCGGCCCTAAAGTTTATAGAGAACCCGGGTGTTACAATGGCTATGCACCAGTACTCTATCAACTATCAACACTGTAAAGAGATGAGGAATGTGGCAAGAACACGTCACTGCGTTCTGGTATCCTCTCCTACGTTTTCCATTCCGCGTGACATAAGGGCCGGAGGAGCTCAGGCGGGCTATAGATTCAACACTTCAACACTTATATTATAGCATTATAGCTATAGCATAGCATCATGACGTCGGGCGCACGGGCCACCTACCGGGCCGCTCAGCTAAGAGACGGGAGCACTGATGGTTGACGAGCTTACTGGTTCTTTAGACACCCTCCTTTTTGGACAACGTGAGTGAGAGAAGGTACAACGTGACACCCATCTGTAGTGCCGAGGTAGTGAAGGATAGCCCCGCGGCTATATTTACACCCCCCCGCTAAGAACACCTTACAGTCTCCCGTGAAGCTCGGCGGCTGACGAGAAAGAAAAAAGCGGGAAGCGGGTCTCCGCATTCAACCTAGCTCCAGGCTCGCTAGCGGCCCCGGAGGGTCTAAGTATCTTCATCGACTCACGTATCACGAGACTTGAAATCTTTACTTTAATCTTTAAATCTTTAGAGATGTTAGAATATTGAGAGCTGCACACGAACATCCGTTGCAGCGCGTGTCTGAGCATGATAGCCCTACAAAACAGGTCAAAGGTCAACAGGTCAAAACCACTACCGAGATCTACTGGATCAGCCCTCAGGCGGACAAGAAGAACTCTTTTAAAATTAACCGTGCATATGAGTCCGACCAAGCCGCTCCCGTTTGGGCGGGATGAGCAATTTAGCGACCAAAGAAACGTTCTAAACGACACAAGCCGTGCCGATCTGTTATGTTATTGGATGTTATTGGCGAGACCGAGGACCCAAACGATAGCCTAACTTATACCGACCTCTTTTTTCGACCTCTTTTGGCAGTCCTTCCACCTCGGCAGCAGAAAGATTAAGGTCATAGTGCTCGCAACAAGGTCTTTTCAAGGTAAGGTCTTCAGCACGGCCATTAACTTGCCTTTCTTGCTTCTCGAAGCTATAGGAGCATTTGAGCGATGGAATACATGACGATACAAAAATAGAACCCTTGGTGTGGAATTCTGGATTGAGTCGCCGCACCTGATAAAACTCTACTACAAACTCTACTCTACTCCCAACGACGACCGTCCCCGTCCCGTCCTGTCAAATGCTAGTAGGGTGCGGGCGGCTAAAAGCTAAAAGGCTAAAAATAGGAGATCTGACTCCGGACTAAGGTATGAACCAGCTTCTCGCTTACCCTGACACTCACCCCAGAGTTTTGCACATACGTAACTACTTGCCACTTGGATAGTGGACTTCACACAAGGCGTTTTGCCCAAACGTCAATCCTTCGGCTGCGCAGGTTATTGGTCTATTTATTGGTCTGGTCCCACACCGCAAAATGGGTCTCGTACTGTGCACGCCGTGATACACGGCGCGGTAAAATAGCAGATGTATCGTTGATTCTCGGTACGCTTACATGTCAGTGTGCACTTTTCAAAAGGATCGACAATACGTCAACAGCATCGTATCACTTATCTCCTTATTTATCTCCTTTATCTCCCATCCCGACATCCCGATCCCGCTATCCCGCTATCCCGCTATCCATCCCGCTCGCTCAACTCAACAACTCAACAACTCAACAACTCAACAACTCAACAACTCAA'
#k = 8
#L = 28
#t = 3
#start_time = timeit.default_timer()
#print(BetterClumpFinding(Genome, k, L, t))
#print('Execution time:', timeit.default_timer() - start_time)
#print(*BetterClumpFinding(Genome,k,L,t), sep = ' ')
##print(BetterClumpFinding('ACGTATAGTCATGCCCATA', 2, 4, 1))
#ecoli = open('Salmonella_enterica.txt',  'r')
#Genome = ecoli.read()
#print(Genome)
#L = 500
#k = 9
#t = 3
#start_time = timeit.default_timer()
#nineMers = BetterClumpFinding(Genome, k, L, t)
#print('9-mers', len(nineMers))
##print(*BetterClumpFinding(Genome,k,L,t), sep = ' ')
#print('Execution time:', timeit.default_timer() - start_time)

