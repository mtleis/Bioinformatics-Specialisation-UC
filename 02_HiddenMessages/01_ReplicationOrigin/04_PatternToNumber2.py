# Solution by learner 'Justin Amarin'
#def PatternToNumber(Pattern):
#    bases = {"A": 0, "C": 1, "G": 2, "T": 3}
#    counter = len(Pattern)
#    number = 0
#    for i in Pattern:
#        counter -= 1
#        number += bases[i] * 4 ** counter
#    return number


## leaner re-solve without recursion:

def symbolToNumber(c):
    tableDict = {"A": 0, "C":1, "G":2, "T":3}
    return tableDict.get(c)

#########################
# Non recursive version #
#########################

def PatternToNumber(pattern):
    number = 0
    for i, exponent in zip(pattern, range(len(pattern)-1, -1, -1)):
        number += symbolToNumber(i)<<(2*exponent)
    return number