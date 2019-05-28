#FrequentWordsWithMismatches(Text, k, d)
#        FrequentPatterns ← an empty set
#        Neighborhoods ← an empty list
#        for i ← 0 to |Text| − k
#            add Neighbors(Text(i, k), d) to Neighborhoods
#        form an array NeighborhoodArray holding all strings in Neighborhoods
#        for i ← 0 to |Neighborhoods| − 1
#            Pattern ← NeighborhoodArray(i)
#            Index(i) ← PatternToNumber(Pattern)
#            Count(i) ← 1
#        SortedIndex ← Sort(Index)
#        for i ← 0 to |Neighborhoods| − 2
#            if SortedIndex(i) = SortedIndex(i + 1)
#                Count(i + 1) ← Count(i) + 1
#       maxCount ← maximum value in array Count
#       for i ← 0 to |Neighborhoods| − 1
#           if Count(i) = maxCount
#               Pattern ← NumberToPattern(SortedIndex(i), k)
#               add Pattern to FrequentPatterns
#       return FrequentPatterns


NB = __import__('08_Neighbors')
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
PN = __import__('04_PatternToNumber')
NP = __import__('03_NumberToPattern')

def FasterFrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = []
    Neighborhoods = []
    for i in range(0, len(Text)-k+1):
        Neighborhoods.extend(NB.Neighbors(Text[i:i+k], d))
    NeighborhoodArray = {}
    for i in range(0, len(Neighborhoods)):
        NeighborhoodArray[i] = Neighborhoods[i]
    Index = {}
    Count = {}
    SortedIndex = {}

    for i in range(0, len(Neighborhoods)):
        Pattern = NeighborhoodArray[i]

        Index[i] = PN.PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index.values())
    for i in range(0, len(Neighborhoods)-1):
        if SortedIndex[i] == SortedIndex[i+1]:
            Count[i+1] = Count[i] + 1
    maxCount = max(Count.values())
    for i in range(0, len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = NP.NumberToPattern(SortedIndex[i],k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns