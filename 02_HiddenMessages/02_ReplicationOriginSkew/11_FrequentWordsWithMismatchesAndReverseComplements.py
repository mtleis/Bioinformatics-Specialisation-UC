import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
RC = __import__('07_ReverseComplement')
FA = __import__('10_ComputingFrequenciesWithMismatches')
NTP = __import__('03_NumberToPattern')

def FrequentWordsWithMismatchesAndReverseComplements(text, k, d):
    FrequentPatterns = []
    textRC = RC.ReverseComplement(text)
    FrequencyArray = FA.ComputingFrequenciesWithMismatches(text,k,d)
    FrequencyArrayRC = FA.ComputingFrequenciesWithMismatches(textRC, k, d)
    for i in range(0, len(FrequencyArray)):
        FrequencyArray[i] = FrequencyArray[i] + FrequencyArrayRC[i]
    maxCount = max(FrequencyArray.values())
    for i in range(0, 4 ** k):
        if FrequencyArray[i] == maxCount:
           Pattern = NTP.NumberToPattern(i, k)
           FrequentPatterns.append(Pattern)
    return FrequentPatterns

text = 'CTTTAGTCATTTCACTAGTTCCTCAAGCCCTTCATCAAGTCATCACTTTCTAGTTCCAGAGTTAGCTCTTTTTAGCCCTTCACTCCTCATTAGTTCTAGCCTCATTCCCCCCCCCTCCCCCTTTAGCCAGAGTCACCTTTTCCCCAGCTTCAAGCTAGTTTTCTCTCTAGCTTTAGTCATCATTTCAAGTCAAGTCACCTTAG'
k = 6
d = 2
print(*FrequentWordsWithMismatchesAndReverseComplements(text, k,d))
