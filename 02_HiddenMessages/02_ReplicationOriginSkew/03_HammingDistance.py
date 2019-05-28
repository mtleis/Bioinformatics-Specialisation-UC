# Hamming Distance between two DNA strings
def HammingDistance(text1, text2):
    # under the assumption that both string have the same length
    if len(text1) == len(text2):
        hamming = 0
        for i in range(0, len(text1)):
            if text1[i] != text2[i]:
                hamming = hamming + 1
        return hamming
    else:
        return 'length of input strings is not equal!'

# developed to solve MedianString Problem. however another implementation (same!) in ./03_DistanceBetweenPatternAndStrings
def HammingDistanceList(Pattern, list):
    # length differs
    hamming = 0
    k = len(Pattern)
    for i in range(0, len(list)):
        subHamming = 0
        Text = list[i]
        found = False
        for j in range(0, len(Text)-k+1):
            subPattern = Text[j:j+k]
            if Pattern != subPattern:
                subHamming += 1
        hamming += subHamming
    return hamming

text1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
text2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
#print(HammingDistance(text1, text2))
Dna = ['ATCATC', 'ATAATG']
# print(HammingDistanceList('ATC', Dna))