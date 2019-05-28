import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/01_IntroductionOverlap_DeBruijnPath')
DB = __import__('07_DeBruijnFromKmers')
EP = __import__('02_EulerianPath')
GP = __import__('03_GenomePathToString')

def StringReconstruction(Patterns):
    dB = DB.DeBruijnFromKmers(Patterns)
    path = EP.EulerianPath(dB)
    Text = GP.GenomePathToString(path)
    return Text

Patterns = ['ATC', 'TCG', 'CGG']
print('Calling String Reconstruction...')
sr = StringReconstruction(Patterns)
print('SR:', sr)

inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/dataset_203_7.txt'
inputFile = open(inputDirectory, 'r')
k = inputFile.readline()
inputLines = inputFile.readlines()
patterns = []
for line in inputLines:
    line = line.replace('\n', '')
    patterns.append(line)
inputFile.close()
print('SR::', StringReconstruction(patterns))
