##  Write a function CountWithPseudocounts(Motifs) that takes a list of strings Motifs
# as input and returns the count matrix of Motifs with pseudocounts as a dictionary of lists.
# Then add this function to Motifs.py.
# (Hint: how can you solve this problem by making a
# very small change to your original function Count(Motifs)?

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count