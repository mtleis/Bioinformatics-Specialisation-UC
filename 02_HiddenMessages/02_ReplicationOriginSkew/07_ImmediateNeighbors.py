#ImmediateNeighbors(Pattern)
#        Neighborhood ← the set consisting of single string Pattern
#        for i = 1 to |Pattern|
#            symbol ← i-th nucleotide of Pattern
#            for each nucleotide x different from symbol
#                Neighbor ← Pattern with the i-th nucleotide substituted by x
#                add Neighbor to Neighborhood
#        return Neighborhood

def ImmediateNeighbors(Pattern):
    Neighborhood = []
    bases = ['A', 'C', 'G', 'T']
    for i in range(0, len(Pattern)):
        symbol = Pattern[i]
        for x in bases:
            if x == symbol: continue
            Neighbor = Pattern[0:i] + x + Pattern[i+1:len(Pattern)]
            Neighborhood.append(Neighbor)
    return Neighborhood

Pattern = 'ACGT'
print(*ImmediateNeighbors(Pattern))
