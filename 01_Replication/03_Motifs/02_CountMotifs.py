## Write a function Count(Motifs) that takes a list of strings Motifs as input
# and returns the count matrix of  Motifs (as a dictionary of lists).
# Then place this function into a new Python file for this chapter called "Motifs.py".

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count


Motifs = ["ATGCA", "TGGCA", "ATGCT"]
print(Count(Motifs))