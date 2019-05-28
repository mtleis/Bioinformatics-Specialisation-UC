# values of skew for a string of sequence
def skew(Text):
    skew = {}
    skew[0] = 0
    for i in range(0, len(Text)):
        if Text[i] == 'G':
            skew[i+1] = skew[i] + 1
        elif Text[i] == 'C':
            skew[i+1] = skew[i] - 1
        else:
            skew[i+1] = skew[i]
    return skew

# print(*skew('GAGCCACCGCGATA'), sep= ' ')
print((0.25**9)*500*992)