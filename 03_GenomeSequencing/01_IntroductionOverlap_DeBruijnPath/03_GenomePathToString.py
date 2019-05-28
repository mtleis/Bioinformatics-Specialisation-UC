def GenomePathToString(path):
    text = ''
    text = text + path[0]
    k = len(path[0])
    for i in range(1, len(path)):
        line = path[i]
        text = text + line[k-1:k]
    return text

path = ['ACT', 'CTC', 'TCG', 'CGT']
print(GenomePathToString(path))

# Fetch Input
#inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/dataset_198_3.txt'
#inputFile = open(inputDirectory, 'r')
#dna = list()
#lines = inputFile.readlines()
#for line in lines:
#    line = line.replace('\n', '')
#    dna.append(line)
#inputFile.close()
#print(GenomePathToString(dna))
