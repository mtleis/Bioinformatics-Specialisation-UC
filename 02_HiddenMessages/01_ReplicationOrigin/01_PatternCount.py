# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


# print(PatternCount('GACCATCAAAACTGATAAACTACTTAAAAATCAGT', 'AAA'))
print(PatternCount('TACGCATTACAAAGCACA', 'AA'))
