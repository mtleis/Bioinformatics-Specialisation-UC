import random
def GibbsSampler(Dna, k, t, N):
    gBestMotifs = [] # output variable
    gMotifs = RandomMotifs(Dna, k, t)
    gBestMotifs = gMotifs.copy()

    for j in range(1,N):
        i = random.randint(0,t-1)
        gMotifs.remove(gMotifs[i])
        profile = ProfileWithPseudocounts(gMotifs)
        gMotifs.insert(i, ProfileGeneratedString(Dna[i], profile, k))
        if Score(gMotifs) < Score(gBestMotifs):
            gBestMotifs = gMotifs.copy()
    return gBestMotifs

def RandomMotifs(Dna, k, t):
    rlist = []
    for i in range(t):
        Dna[i]
        num = random.randint(1, len(Dna[i])-k)
        kmer = Dna[i][num:num+k]
        rlist.append(kmer)
    return rlist

def Profile(pMotifs):
    t = len(pMotifs)
    k = len(pMotifs[0])
    pprofile = {}
    pcount = Count(pMotifs)
    for symbol in 'ACGT':
        pprofile[symbol] = []

    for i in range(k):
        sum = 0
        for symbol in 'ACGT':
            sum = sum + pcount[symbol][i]

        for symbol in 'ACGT':
            pprofile[symbol].append(pcount[symbol][i]/sum)

    return pprofile

def Count(cMotifs):
    ccount = {}
    k = len(cMotifs[0])
    for symbol in "ACGT":
        ccount[symbol] = []
        for j in range(k):
            ccount[symbol].append(0)

    t = len(cMotifs)
    for i in range(t):
        for j in range(k):
            symbol = cMotifs[i][j]
            ccount[symbol][j] += 1

    return ccount

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}

    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def Score(sMotifs):
    consensus = Consensus(sMotifs)
    sscore = 0
    for i in range(len(sMotifs)):
        for k in range(len(consensus)):
            if consensus[k] != sMotifs[i][k]:
                sscore += 1
    return sscore

def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    i = 0
    cumProb = {}
    for key in Probabilities:
        if i == 0:
            cumProb[i] = Probabilities[key]
        else:
            cumProb[i] = Probabilities[key] + cumProb[i-1]
        if p < cumProb[i]:
            kmer = key
            return kmer
        i = i + 1
    return kmer

def Consensus(kMotifs):
    kconsensus = ""
    k = len(kMotifs[0])
    kcount = CountWithPseudocounts(kMotifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if kcount[symbol][j] > m:
                m = kcount[symbol][j]
                frequentSymbol = symbol
        kconsensus += frequentSymbol
    return kconsensus

def Normalize(Probabilities):
    result = {}
    sum = 0
    for key in Probabilities:
        sum += Probabilities[key]
    for key in Probabilities:
        result[key] = Probabilities[key]/sum
    return result

def CountWithPseudocounts(cpMotifs):
    t = len(cpMotifs)
    k = len(cpMotifs[0])
    cpcount = {}

    for symbol in "ACGT":
        cpcount[symbol] = []
        for j in range(k):
            cpcount[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = cpMotifs[i][j]
            cpcount[symbol][j] += 1
    return cpcount

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        symbol = Text[i]
        p *= Profile[symbol][i]
    return p

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = CountWithPseudocounts(Motifs)
    for symbol in 'ACGT':
        profile[symbol] = []

    for i in range(k):
        sum = 0
        for symbol in 'ACGT':
            sum = sum + count[symbol][i]

        for symbol in 'ACGT':
            profile[symbol].append(count[symbol][i] / sum)

    return profile

if __name__ == "__main__":
    k, t, N = [int(a) for a in input().strip().split(" ")]
    Dna = []
    for _ in range(t):
        Dna.append(input())

    BestMotifsr = GibbsSampler(Dna, k, t, N)

    ans = GibbsSampler(Dna, k, t, N)
    for a in ans:
        if a != '':
            print(a)