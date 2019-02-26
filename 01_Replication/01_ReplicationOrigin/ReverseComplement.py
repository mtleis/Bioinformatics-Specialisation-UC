import reverse

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    Pattern = reverse.Reverse(Pattern)
    Pattern = reverse.Complement(Pattern)
    return Pattern


