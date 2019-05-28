#MedianString(Dna, k)
#    distance ← ∞
#    for i ←0 to 4k −1
#        Pattern ← NumberToPattern(i, k)
#        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna)
#            distance ← DistanceBetweenPatternAndStrings(Pattern, Dna)
#            Median ← Pattern
#    return Median

import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_replicationOrigin')
NP = __import__('05_NumberToPattern')
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/02_replicationOriginSkew')
HD = __import__('03_HammingDistance')
DP = __import__('03_DistanceBetweenPatternAndStrings')

def MedianString(Dna, k):
    distance = sys.maxsize
    Median = ''
    for i in range(0, 4**k):
        Pattern = NP.NumberToPattern(i, k)
        #hamming = HD.HammingDistanceList(Pattern, Dna)
        hamming = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        if distance > hamming:
            distance = hamming
            Median = Pattern
    return Median

Dna = [
'CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'
    ]
k = 7

print(0.3*0.4*0.4*0.5*0.1)
print(MedianString(Dna, k))
