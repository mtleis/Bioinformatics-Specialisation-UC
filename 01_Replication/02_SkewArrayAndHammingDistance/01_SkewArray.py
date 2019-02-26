# Input:  A String Genome
# Output: The skew array of Genome as a list.
def SkewArray(Genome):
    skew = {0:0}
    values = {'A':0, 'T':0, 'C':-1, 'G':1}

    # skip the new line character
    for i in range(0, len(Genome)):
        if(Genome[i] != '\n'):
            skew[i+1] = skew[i] + values[Genome[i]]
        else:
            skew[i+1] = skew[i]

    return skew.values()

