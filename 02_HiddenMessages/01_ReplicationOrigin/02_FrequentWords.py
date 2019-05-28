## Pseudo-code of the FrequentWords Class
#FrequentWords(Text, k)
#        FrequentPatterns ← an empty set
#        for i ← 0 to |Text| − k
#            Pattern ← the k-mer Text(i, k)
#            Count(i) ← PatternCount(Text, Pattern)
#        maxCount ← maximum value in array Count
#        for i ← 0 to |Text| − k
#            if Count(i) = maxCount
#                add Text(i, k) to FrequentPatterns
#        remove duplicates from FrequentPatterns
#        return FrequentPatterns
PatternCount = __import__('01_PatternCount')

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count ={}
    for i in range(0, len(Text) - k -1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount.PatternCount(Text, Pattern)
    maxCount = max(Count.values())
    for i in range(0, len(Text)-k -1):
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:i+k])
    # remove duplicates
    FrequentPatterns = list(set(FrequentPatterns))
    return FrequentPatterns

# print(FrequentWords('CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT', 3))
text = "atgaccgggatactgataaaaaaaagggggggggcgtacacattagataaacgtatgaagtacgttagactcggcgccgccgacccctattttttgagcagatttagtgacctggaaaaaaaatttgagtacaaaacttttccgaataaaaaaaaagggggggatgagtatccctgggatgacttaaaaaaaagggggggtgctctcccgatttttgaatatgtaggatcattcgccagggtccgagctgagaattggatgaaaaaaaagggggggtccacgcaatcgcgaaccaacgcggacccaaaggcaagaccgataaaggagatcccttttgcggtaatgtgccgggaggctggttacgtagggaagccctaacggacttaataaaaaaaagggggggcttataggtcaatcatgttcttgtgaatggatttaaaaaaaaggggggggaccgcttggcgcacccaaattcagtgtgggcgagcgcaacggttttggcccttgttagaggcccccgtaaaaaaaagggggggcaattatgagagagctaatctatcgcgtgcgtgttcataacttgagttaaaaaaaagggggggctggggcacatacaagaggagtcttccttatcagttaatgctgtatgacactatgtattggcccattggctaaaagcccaacttgacaaatggaagatagaatccttgcataaaaaaaagggggggaccgaaagggaagctggtgagcaacgacagattcttacgtgcattagctcgcttccggggatctaatagcacgaagcttaaaaaaaaggggggga"
print(FrequentWords(text, 15))
## You can have a faster version by implementing ComputingFrequencies
#FasterFrequentWords(Text, k)
#        FrequentPatterns ← an empty set
#        FrequencyArray ← ComputingFrequencies(Text, k)
#        maxCount ← maximal value in FrequencyArray
#        for i ← 0 to 4k − 1
#            if FrequencyArray(i) = maxCount
#                Pattern ← NumberToPattern(i, k)
#                add Pattern to the set FrequentPatterns
#        return FrequentPatterns