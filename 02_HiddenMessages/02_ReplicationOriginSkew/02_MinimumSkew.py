skew = __import__('01_Skew')

def MinimumSkew(Genome):
    skew_array = skew.skew(Genome)
    minimum = min(skew_array.values())
#    print('min ', minimum)
    result = []
    for i in range(0, len(skew_array)):
        if skew_array[i] == minimum:
            result.append(i)
    return result

#genome = 'GGGCATGCGCCCCAATACGTACTGCC'
#print(*MinimumSkew(genome), sep =' ')

genome = 'CATTCCAGTACTTCGATGATGGCGTGAAGA'
#print(*MinimumSkew(genome), sep =' ')
