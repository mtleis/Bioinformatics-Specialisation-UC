#IterativeNeighbors(Pattern, d)
#        Neighborhood ← set consisting of single string Pattern
#        for j = 1 to d
#            for each string Pattern’ in Neighborhood
#                add ImmediateNeighbors(Pattern') to Neighborhood
#                remove duplicates from Neighborhood
#        return Neighborhood
ImmediateNeighbors = __import__('07_ImmediateNeighbors')

def IterativeNeighbors(Pattern, d):
    Neighborhood = [Pattern]
    for j in range(0, d):
        for subPattern in [Neighborhood]:
            Neighborhood.extend(ImmediateNeighbors.ImmediateNeighbors(subPattern[0])) # as string
            Neighborhood = list(dict.fromkeys(Neighborhood))
    return Neighborhood

Pattern = 'AAT'
print(*IterativeNeighbors(Pattern,1))

