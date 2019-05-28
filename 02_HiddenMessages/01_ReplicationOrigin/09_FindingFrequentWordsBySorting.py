#FindingFrequentWordsBySorting(Text , k)
#        FrequentPatterns ← an empty set
#        for i ← 0 to |Text| − k
#            Pattern ← Text(i, k)
#            Index(i) ← PatternToNumber(Pattern)
#            Count(i) ← 1
#        SortedIndex ← Sort(Index)
#        for i ← 1 to |Text| − k
#            if SortedIndex(i) = SortedIndex(i − 1)
#                Count(i) = Count(i − 1) + 1
#        maxCount ← maximum value in the array Count
#        for i ← 0 to |Text| − k
#            if Count(i) = maxCount
#                Pattern ← NumberToPattern(SortedIndex(i), k)
#                add Pattern to the set FrequentPatterns
#        return FrequentPatterns
PatternToNumber = __import__('04_PatternToNumber')
NumberToPattern = __import__('05_NumberToPattern')

def FindingFrequentWordsBySorting(Text, k):
    FrequentPatterns = []
    Index = {}
    Count = {}
    for i in range(0, len(Text) -k):
        Pattern = Text[i:i+k]
        Index[i] = PatternToNumber.PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index.values())
    for i in range(1, len(Text)-k):
        if SortedIndex[i] == SortedIndex[i-1]:
            Count[i] = Count[i-1] + 1
    maxCount = max(Count.values())
    for i in range(0, len(Text) - k):
        if Count[i] == maxCount:
            Pattern = NumberToPattern.NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

print(FindingFrequentWordsBySorting('AGCTAGCTAGCTACT', 4))