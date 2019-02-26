# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    l = len(Pattern)
    t = len(Text)
    for i in range(t-l+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count = count+1
    return count

# Hamming Distance
def HammingDistance(p, q):
    return sum(pi != qi for pi, qi in zip(p,q))

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[1],lines[0]))