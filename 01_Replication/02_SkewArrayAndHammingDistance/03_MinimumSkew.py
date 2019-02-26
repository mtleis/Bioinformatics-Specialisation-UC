# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    array = SkewArray(Genome)
    print('array, ', array)
    minimum = min(array)
    print('minimum', minimum)
    for i in range(len(array)):
        if array[i] == minimum:
            print('i: ', i)
            positions.append(i)
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# simple implementation, you can also use the separate function that accounts for new lines
def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(len(Genome)):
        skew.append(score[Genome[i]] + skew[i])
    return skew


Sequence = "ATGCATGGCCTACGTACTA"
m = MinimumSkew(Sequence)
print('minimum skew ', m)