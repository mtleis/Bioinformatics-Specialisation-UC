# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    result = ""
    for num in range(0,len(Pattern)):
        if (Pattern[num] == 'A'):
            result+='T'
        elif (Pattern[num] == 'T'):
            result+='A'
        elif (Pattern[num] == 'G'):
            result+='C'
        elif (Pattern[num] == 'C'):
            result+='G'
    return result

