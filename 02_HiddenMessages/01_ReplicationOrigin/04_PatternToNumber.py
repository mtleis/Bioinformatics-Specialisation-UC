## Pseudocode
#PatternToNumber(Pattern)
#        if Pattern contains no symbols
#            return 0
#        symbol ← LastSymbol(Pattern)
#        Prefix ← Prefix(Pattern)
#        return 4 · PatternToNumber(Prefix) + SymbolToNumber(symbol)

def PatternToNumber(Pattern):
    if Pattern == '':
        return 0
    symbol = LastSymbol(Pattern)
    prefix = Prefix(Pattern)
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def LastSymbol(Pattern):
    return Pattern[len(Pattern)-1]

def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3
    return -1

def Prefix(Pattern):
    return Pattern[0:len(Pattern)-1]

#print(PatternToNumber('CAGTGCGAAACTGTTATCT'))

