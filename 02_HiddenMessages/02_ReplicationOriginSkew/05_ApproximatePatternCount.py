#ApproximatePatternCount(Text, Pattern, d)
#        count ← 0
#        for i ← 0 to |Text| − |Pattern|
#            Pattern′ ← Text(i , |Pattern|)
#            if HammingDistance(Pattern, Pattern′) ≤ d
#                count ← count + 1
#        return count
HammingDistance = __import__('03_HammingDistance')

def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        newPattern = Text[i:i+len(Pattern)]
        if HammingDistance.HammingDistance(Pattern, newPattern) <= d:
            count = count + 1
    return count

Text = 'CATGCCATTCGCATTGTCCCAGTGA'
Pattern = 'CCC'
d = 2
#print(ApproximatePatternCount(Text, Pattern,d))