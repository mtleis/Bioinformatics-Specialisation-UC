# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    l = len(Pattern)
    t = len(Text)
    for i in range(t-l+1):
        if ( HammingDistanceZip(Text[i:i+l], Pattern) <= d):
            positions.append(i)
    return positions

# The HammingDistance
def HammingDistanceZip(p, q):
    return sum(pi!=qi for pi, qi in zip(p,q))


pattern = "ATTCTGGA"
text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"

positions = ApproximatePatternMatching(text,pattern, 3)
print(positions)
