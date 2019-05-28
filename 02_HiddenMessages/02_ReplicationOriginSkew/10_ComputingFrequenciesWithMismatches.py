#ComputingFrequenciesWithMismatches(Text, k, d)
#    for i ← 0 to 4k − 1
#        FrequencyArray(i) ← 0
#    for i ← 0 to |Text|−k
#        Pattern ← Text(i, k)
#        Neighborhood ← Neighbors(Pattern, d)
#        for each string ApproximatePattern in Neighborhood
#            j ← PatternToNumber(ApproximatePattern)
#            FrequencyArray(j) ← FrequencyArray(j) + 1
#    return FrequencyArray
Neighbors = __import__('08_Neighbors')
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
PatternToNumber = __import__('04_PatternToNumber')


def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequencyArray = {}
    for i in range(0, 4**k):
        FrequencyArray[i] = 0
    for i in range(0, len(Text)-k+1):
        Pattern = Text[i:i+k]
        Neighborhood = Neighbors.Neighbors(Pattern,d)
        for subString in Neighborhood:
            j = PatternToNumber.PatternToNumber(subString)
            FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

#print(*ComputingFrequenciesWithMismatches('ACTC', 3, 1).values())