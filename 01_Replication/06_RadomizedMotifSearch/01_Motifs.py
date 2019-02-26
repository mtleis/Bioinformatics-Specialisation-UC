# Write a function Motifs(Profile, Dna) that takes a profile matrix Profile corresponding to a list of strings Dna as input and returns a list of the Profile-most probable k-mers in each string from Dna. Then add this function to Motifs.py.

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs = []
    k = len(Profile['A']) # Profile is a dictionary
    for i in range(len(Dna)):
        motifs.append(ProfileMostProbableKmer(Dna[i], k, Profile))
    return motifs

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
def ProfileMostProbableKmer(text, k, profile):
    # loop through every k-mer in text
    t = len(text)
    min = 0
    mostProbableKmer = text[0:k]
    for i in range(t-k+1):
        kmer = text[i:i+k]
        pr = Pr(kmer, profile)
        if pr > min:
            mostProbableKmer = kmer
            min = pr

    return mostProbableKmer



# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p

ProfileTestCase0= { 'A': [0.8, 0.0, 0.0, 0.2 ],'C': [ 0.0, 0.6, 0.2, 0.0], 'G': [ 0.2 ,0.2 ,0.8, 0.0], 'T': [ 0.0, 0.2, 0.0, 0.8]}
DnaTC0=['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
Motifs(ProfileTestCase0, DnaTC0)

