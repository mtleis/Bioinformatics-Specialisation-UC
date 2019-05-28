import itertools
SR = __import__('04_StringReconstruction')

# input: an integer K
# output : a k-universal string (0 & 1s)
def kuniversal(k):
    # obtain all contigs of k-strings
    strings = itertools.product('01', repeat=k)
    patterns = []
    for s in strings:
        text =''
        for item in s:
            text = text+item
        patterns.append(text)
    kuniversal = SR.StringReconstruction(patterns)

    # discard last k-1 elements since it is circular string
    endpoint = len(kuniversal) - (k-1)
    kuniversal = kuniversal[0:endpoint]

    return kuniversal

print(kuniversal(8))
