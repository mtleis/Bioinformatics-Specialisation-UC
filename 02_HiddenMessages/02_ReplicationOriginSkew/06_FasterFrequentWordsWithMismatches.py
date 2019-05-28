#FasterFrequentWords(Text, k)
#        FrequentPatterns ← an empty set
#        FrequencyArray ← ComputingFrequencies(Text, k)
#        maxCount ← maximal value in FrequencyArray
#        for i ← 0 to 4k − 1
#            if FrequencyArray(i) = maxCount
#                Pattern ← NumberToPattern(i, k)
#                add Pattern to the set FrequentPatterns
#        return FrequentPatterns
ComputingFrequenciesWithMismatches = __import__('10_ComputingFrequenciesWithMismatches')
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
NumberToPattern = __import__('03_NumberToPattern')

def FasterFrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = []
    FrequencyArray = ComputingFrequenciesWithMismatches.ComputingFrequenciesWithMismatches(Text, k, d)
    maxCount = max(FrequencyArray.values())
    for i in range(0, 4**k):
        if FrequencyArray[i] == maxCount:
            Pattern = NumberToPattern.NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns