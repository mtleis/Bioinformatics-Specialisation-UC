#NumberToPattern(number, k)
#    quotient ←  Quotient(number, 4)
#    r ←  Remainder(number, 4)
#    symbol ←  NumberToSybmol(r)
#    if k = 1
#        return symbol
#    PrefixPattern ←  NumberToPattern(quotient, k-1)
#    return concatenation of PrefixPattern with symbol

def NumberToPattern(number, k):
    quotient = Quotient(number, 4)
    r = Remainder(number, 4)
    symbol = NumberToSymbol(r)
    if k == 1:
        return symbol
    PrefixPattern = NumberToPattern(quotient, k-1)
    return PrefixPattern + symbol

def NumberToSymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'
    return 'M'

def Quotient(index, k):
    return int(index/k)

def Remainder(index,k):
    return index % k

#print(NumberToPattern(6676, 10))
