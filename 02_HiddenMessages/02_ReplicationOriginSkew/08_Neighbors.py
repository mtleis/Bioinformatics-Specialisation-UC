#Neighbors(Pattern, d)
#        if d = 0
#            return {Pattern}
#        if |Pattern| = 1
#            return {A, C, G, T}
#        Neighborhood ← an empty set
#        SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
#        for each string Text from SuffixNeighbors
#            if HammingDistance(Suffix(Pattern), Text) < d
#                for each nucleotide x
#                    add x • Text to Neighborhood
#            else
#                add FirstSymbol(Pattern) • Text to Neighborhood
#        return Neighborhood
HammingDistance = __import__('03_HammingDistance')

def Neighbors(Pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return list([Pattern])
    if len(Pattern) == 1:
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:len(Pattern)], d)
    for i in range(0, len(SuffixNeighbors)):
        Text = SuffixNeighbors[i]
        if HammingDistance.HammingDistance(Pattern[1:len(Pattern)], Text) < d:
            for x in nucleotides:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return Neighborhood

Pattern = 'ACGT'
neighbors = Neighbors(Pattern,3)
print(len(neighbors))
