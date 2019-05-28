# randomized algorithm and GibbsSampler, This also is my try
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/04_RandomizedMotifSearch')
RN = __import__('01_RandomizedMotifSearch')
GB = __import__('03_GibbsSampler')

def comboSearch(Dna, k, rand, gibs):
    t = len(Dna)
    BestMotifs = RN.RandomizedMotifSearch(Dna, k, t)
    for i in range(rand):
        motifs = RN.RandomizedMotifSearch(Dna, k, t)
        if RN.Score(motifs) < RN.Score(BestMotifs):
            BestMotifs = motifs.copy()
    print('Score of Rand:', GB.Score(BestMotifs))
    # Starting from BestMotifs found by Randomized, apply Gibbs
    res = GB.GibbsSamplerWithMotifs(Dna, BestMotifs, k, t, gibs)
    print('Score of Gibs:', GB.Score(res))
    return BestMotifs

def getPositions(Dna, motifs):
    positions = []
    for i in range(0,len(Dna)):
        string = Dna[i]
        pattern = motifs[i]
        positions.append(str.find(string, pattern))
    return positions

## load the sequences from file into a dna string
mtb = open('MTB-upstream250.txt',  'r')
Dna = []
names = []
# first read is for seq. name, second read will read the actual seq.
for line in mtb:
    if line[0] == '>':
        line = line.replace('\n', '')
        line = line.replace('>', '')
        names.append(line)
    else:
        text = line.replace('\n', '')
        Dna.append(text)
    #text = mtb.readline()
    #print('a new text:', text)
    #text = text.replace('\n', '')
    #Dna.append(text)
#print(Dna)
bestMotifs = comboSearch(Dna, 20, 200, 5000)
positions  = getPositions(Dna, bestMotifs)

#print(*bestMotifs, sep='\n')
#print(*positions , sep='\n')
#print(*names, sep='\n')

for i in range(0, len(bestMotifs)):
    print(names[i], '\t\t', positions[i], '\t', bestMotifs[i])
