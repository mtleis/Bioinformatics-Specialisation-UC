# Copy your PatternMatching function below this line.
def PatternMatching(Pattern, Genome):
        positions=[]
        l = len(Pattern)
        g = len(Genome)
        for i in range(0,g):
                if (Genome[i:i+l] == Pattern) :
                        positions.append(i)
        return positions

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
positions = PatternMatching("CTTGATCAT", v_cholerae)
# and store the output as a variable called positions