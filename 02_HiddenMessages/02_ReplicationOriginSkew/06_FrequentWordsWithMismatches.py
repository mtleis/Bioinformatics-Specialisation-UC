# WARNING: This is a non-efficient algorithm, for demo purposes only
ApproximatePatternCount = __import__('05_ApproximatePatternCount')
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
NumberToPattern = __import__('03_NumberToPattern')
# PatternToNumber = __import__('04_PatternToNumber')

def FrequentWordsWithMismatches(Text, k, d):
    allPatterns = {}
    patterns = []
    # genenate all 4^k patterns
    for i in range(0, 4**k+1):
        Pattern = NumberToPattern.NumberToPattern(i,k)
        # compute ApproximatePatternCount for every pattern
        allPatterns[i] = ApproximatePatternCount.ApproximatePatternCount(Text, Pattern, d)

    maxCount = max(allPatterns.values())
    for i in range(0, 4**k+1):
        if allPatterns[i] == maxCount:
            patterns.append(NumberToPattern.NumberToPattern(i,k))
    # return patterns with maximum occurences
    return patterns


Text = 'AGTTGGCTCCGGGCAGTTGGCAGTTTCCGCCGGGCTCCGTCCGCCGTCCGGGTGGCAGTTTCCGGGCGGCCCGAGTTCCGCCGAGTTGGTCCGGGCCCGAGTTTCCGTCCGGGCTCCGAGTTAGTTCCGGGTTCCGGGTCCGGGCAGTTCCGCCGCCGAGTTGGCCCGCCGAGTTGGTGGTTCCGAGTTAGTTCCGGGTGGTTCCGAGTTCCGGGCTCCGAGTTCCGGGCGGCGGTCCGGGTCCGTCCGGGCCCGCCGGGCCCGGGTGGTCCGGGCTCCGAGTTTCCGTCCGCCGGGCAGTTGGCCCGGGTAGTTTCCGGGTGGT'
k = 7
d = 2
# print(FrequentWordsWithMismatches(Text, k, d))


