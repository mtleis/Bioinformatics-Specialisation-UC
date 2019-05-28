def StringFromReadPairs(readPairs, k, d):
    string = ''
    pairedcomposition = {}
    for read in readPairs:

    # return (k,d)-mer composition of the read pairs
    return string

def DeBruijnFromKmers(patterns):
    k = len(patterns[0])
    composition = defaultdict(list)
    # sortedComposition = defaultdict(list)
    for pattern in patterns:
        prefix = pattern[0:k-1]
        suffix = pattern[1:k]
        composition[prefix].append(suffix)

    return composition