## Solve the Profile-most Probable k-mer Problem
# by writing a function ProfileMostProbablePattern(Text, k, Profile).
# (Hint: make sure to use the function Pr(Text, Profile) as a subroutine.)

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p

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


# Write your ProfileMostProbableKmer() function here.
# The profile matrix assumes that the first row corresponds to A, the second corresponds to C,
# the third corresponds to G, and the fourth corresponds to T.
# You should represent the profile matrix as a dictionary whose keys are 'A', 'C', 'G', and 'T' and whose values are lists of floats
def ProfileMostProbableKmer(text, k, profile):
    # loop through every k-mer in text
    t = len(text)
    min = 0
    mostProbableKmer = ""
    for i in range(t-k+1):
        kmer = text[i:i+k]
        pr = Pr(kmer, profile)
        if pr > min:
            mostProbableKmer = kmer
            min = pr

    return mostProbableKmer

Motifs = ["ATGCA", "TGGCA", "ATGCT"]
print(Count(Motifs))
print(Profile(Motifs))
print('Pr:', Pr('ATGCA', Profile(Motifs)))
print(ProfileMostProbableKmer('ATGCA', 3, Profile(Motifs)))