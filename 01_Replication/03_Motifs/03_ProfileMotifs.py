##  Write a function Profile(Motifs) that takes Motifs as input
# and returns their profile matrix as a dictionary of lists.
# Then place this function into Motifs.py.
# Make sure that you use the Count(Motifs) function that we already wrote as a subroutine!

# use the Count function
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



# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    count = Count(Motifs)
    for symbol in 'ACGT':
        profile[symbol] = []

    for i in range(k):
        sum = 0
        for symbol in 'ACGT':
            sum = sum + count[symbol][i]

        for symbol in 'ACGT':
            profile[symbol].append(count[symbol][i]/sum)

    return profile

Motifs = ["ATGCA", "TGGCA", "ATGCT"]
print(Count(Motifs))
print(Profile(Motifs))
