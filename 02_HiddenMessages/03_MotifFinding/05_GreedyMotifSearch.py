#GreedyMotifSearch(Dna, k, t)
#        BestMotifs ← motif matrix formed by first k-mers in each string from Dna
#        for each k-mer Motif in the first string from Dna
#            Motif1 ← Motif
#            for i = 2 to t
#                form Profile from motifs Motif1, …, Motifi - 1
#                Motifi ← Profile-most probable k-mer in the i-th string in Dna
#            Motifs ← (Motif1, …, Motift)
#            if Score(Motifs) < Score(BestMotifs)
#                BestMotifs ← Motifs
#        return BestMotifs
PK = __import__('04_ProfileMostProbableKmer')

def GreedyMotifSearch(Dna, k, t):
    # Initialize BestMotifs to be the first k-mer in the DNA
    BestMotifs = []
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(PK.ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# use the Count function
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(0, k):
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

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for i in range(len(Motifs)):
        for k in range(len(consensus)):
            if consensus[k] != Motifs[i][k]:
                score += 1
    return score

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    consensus = ""
    k = len(Motifs[0])
    count = Count(Motifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

Dna = [
'GGAAACTGAGAGGTCTCTAGCCTTTCTACCGGGAATGTTAACCCTCTTAGTCTCACACGTCAGTAACTGTACCCTATGGACCCAAACCCACTCGTAACGGATTACTGCAGTTGGAACCTCTAAATGATTGCTATACTCCGCTTGATGGATCATACA',
'GCGAGTGTGTTCAACCGTTTGGTTCAAAGCTTATTGACGGGTGACTTCAAACCTACACTGCACTCCCCACACATATGCTTCTCGTTGGGTGTTGCCATTTGAGCGCTGGCAACGGCTTGTCACAGACATCGGTGCTCCTTGCCACCTAAGGAATCC',
'CCAAGCTGAAGGAGGATCTACCAGTCGGGTCACTGCCTCACAGGTAGTAAGGCCAGGTTTCGTGCACCACCGTCGGCGGATTGCGCATTTATACTCCCTACATAGGCCGAAACGTAGGAAAACGTATGTAGCCGCTCCCTGAGTGCGTAGACACGT',
'CTCGACGCTAGAAGCTACATCGTTTAAGCGTTCTACGGAAAACGCTGGCTCAGTACTTACGCAGACGCCGATGGGACCAGTTCTCGCGACTATACGCCGATACCCGCACTTGCTGCACGCGCGGCTCACTACGTTCAGGCATCAAGCTCGTAATCC',
'ATGCAGGAACAGCGGTGAAGAACGGCGGATAACTGCTCAGCTCCCTGAAACGCCAACATACAATCCGTCTGGGAGACAGGCTTAGGGTCCGGTCATGGTTCCAGTAGCTTTCGCGGTAAGTCCCAAGTGCTTGTCCTTATTATAAGCCACGTCTTC',
'TTGCCCCGCGTCAAACTTCTCACTTTAGTATCGCTCTTTGCGAACCGGGTAACAGTGCGCCTAAGATGCGGCCCGGCTGACTTCCCTTACACACGGTGATTTCTGAGAGGGCACCATGATAAGGATCCAAAAACTTGTTGAAGCTGGACTGCGAGT',
'TTGGTACCTTCGAGAGTGACATTGCACTCTTCGAGACTAGCATAGAACTCCTTCCCAAACTGCGATAGGTTTAGGTCCGTCTCGCCGGCTTACTCCCCACCCCAAGCGAGACCTACTGTCCTAGATCTTTAGTCTTATACCTATTACAAATACGAT',
'TAATAGTGGCAATCGGCTAACTCCTTAGGCCAAGTGAAAACTCATTGACAGGTAGACCAGGACTACGCGTCTGTGACTTTCAAGCAACGCAAAAGGTATCTATAGTGAGGTATTTGCTGGCTTCGCAAGGGAATCTGGTCTGGTTCTGGAAATATA',
'CGTAGCGGGTGAGGAGACTCGAGCTTACCGACGATGAAACTAGGAGAGGCGGCTTACTTCCTCGTCACCTGTTAGCGTCTTCTACCGTTCTCTCTCTTTCATATTATAATAATTCAAAGTGACTATTGCCACTTCAGTTGAGGAGAGGGAGTACTG',
'CGAGACACGTTATGCTAAGTCCATAGATGGTCGCGTGTTTGCATGAAACAGAATCATCCCTCTTAGCCCCACTTATCACACCCTTCCAAAGTCAACTCTGTGTCATAGCTAATCACTAGCAACTATAAGCTTTCACGGCCTGACCCGGTTAACTCC',
'GGCCCTCGCGGTCTGGCGCTGATCAAAATGGCCAAGTAAAGCCTGTGGGCGGATCACTACTTTCCCCTGACTTAGTTGAGTTAAATTGGGTCTTGAGATAAAGCGGGACCACTACCAGTCCATGAACACCATATATACTGACGAGCAACTAGTTGC',
'CTTACCCACAAAGCGGCTAACTCCGTCAAACGGCAGGCTCTGAGACAACAGAGCGTTGATACTCTTGCAGAGATGCATCGAAGACAAGTTTCGACGCGTCGATTAGGTTTGCTTATTACTCTTGCTTGGTTACGCATGAACTTTTCAGTTAATTCC',
'TTTTAGAATCGAGGGGCTACGTGTCGTTAAGAACCGGACAAGATTTAGTACCGCCGCTAAAGGAACGGAATTCCGTTGTGAAAACAACCGGAGCATGTTTGTTGTTCAGCGGGTTACTGCGCGATTATCTAGTCAGACATGGAGATACTTAAGCGA',
'GACCACGTGGCTGTACGTCCTATTGTCAAATCAGAAACTCAGAGTACAAGTCAACCGATATGCACCTACCGTCTTATTCAACGACCTCGCTTGGTCGCTAACAAACGATTCACCCAATGGAAATCTAACCGCGTTCTGTGAGTTACGGCTCACTAC',
'AGTGCTCGCTAGGATCAAACGACCTCGGCTTACTTCGCGCGGTCCGATCCGGGTGATAAAATGGGATCCATTGAGTACCGGTTCCTGCGTCCTCCTTCAGGAAAGGCGAGCCTATAATCGGGTTGACGCGCAGTAAGGGGCTTACGCTGAAGGTGA',
'AAGGGGAGAGACAATCCTTTCGCATAAGAAACTAATGTTGGCCCCGTCTGGGGTTAGCGGGCGCTGACTAATCTGTCCGAAGCCTGAAAAATCTCTCGTTAATCCCGGTCTTCATATCACGCAAGCCCCGGTTCACAGGGGGCTCCGGGTTACTCC',
'ATGCTGGGGAGGTAAAGCGATGCCAGGCACACCCGGGCCCTGACAGGGTAGAGACGGGATTCGGTTTACTGCTTCAACTAGGCTTAGTTATCCTAGGTACATGTAACGTATACAATTATACATGTAATAGGAACTCCAACTGCGTTGTCACTGAGT',
'GAAATCTGTCTACAATAATAACCAAGCCACTGAAGCAATCTGTCGAGGCTTCCACGAAATGGAGGAATTATTCCTCTCAATACTTTATGAGGCGGGTGCTTCTTCCATTCGGCTCACTGCCACTAGGGACGATTTATGTTGAGGACGGCTCGCCAA',
'CCAGACAACAGGTTTATCTACTCATCGGTTGACTTCTAGTTCCATCACCCTGGGCCTATGTGGTTGACTGGATAACCTAAGGACGATGATAAGCATATTGGACAGCACCATTGGACAACGCCCAGGCATACTAAGGCCCAGGAGTCGTGTTCCCTT',
'GCGCAGGGTAATCCCCGCCCTGCTTGTATAGTCACAGTGTCCGCCCATGACTTCCTAATTCCACATACTTGCTAGGATGACCCAACTTTTTCTCACGCCGTTAAGTTGAGAAGACTCAGCACGGATAACTTCATCGCAGACGAAAAAGTTGACTTT',
'AGGGTGTCAACAACATCTGAGGATTTTACCTTGGCGCGACAAACTCACGCGGTTTACTTCTTATCAGGACTGTCGCTGTCGGCCATCTCCCTTATGTAGGTTTGCTCGATTTGAGGATGTGTAACAAGTTTCTCCTAGGAACCTCAACCGGTAGAT',
'CGGTCGGGTACAACCCGCAACTGCGTAATTAATCCGACGGATAACTGCCAGAAGTCTCATAGCGTACAGGAGTTTATCACGACTGAAAATGTGACTTACCAGACACAAGGCTTTGACAAAGGAGTATACGATTAGAAAAACGGTAGCATCGCATTT',
'CTCCAGCACGTGTAGCGACGAGCTTCGGGTAACTCCACGAACTGGTTGGAATATAATGAGGCTAAAACTTCGAGGTCTCCCGCCCGTATGGCATGGAATTGTCAGGTTGAATATTGCGTATACCACGGCCCATTTCCGGAGATTATGATGCACTCC',
'TTCCATTTACGGAGACATATCAATTATTGCTTGGTACGCTAGTCGACGATCATCGAATGGATCTTATACCCGCACCATCAACGGTAGCTATCCCGGACGGGTTACTACAGATCGTACTGCGGACCCAGGTGTATGATAAAAGAACGGGTCCATGCC',
'GATCTCCTGGCCACCCACATACGAAAGGTGTGTCACCGCCTCCACAACGTTTCGATTGGAACTAATTGTAGATTTGTAGAGACTTGCTTAGACGAGTATGGAACTCTGGCACCACTGACGCCGGCTTACTCCTGGCACACAGGTTGATGAACTGGG']
k = 12
t = 25
print(*GreedyMotifSearch(Dna, k, t))