import matplotlib.pyplot as plt
SkewArray = __import__('01_SkewArray')

with open('E_coli.txt') as file:
    genome = file.read()

skew = SkewArray.SkewArray(genome)
plt.plot(skew)
plt.xlabel('genome position')
plt.ylabel('skew')
plt.show()

