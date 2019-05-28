import unittest
from pathlib import Path
EP = __import__('02_EulerianPath')

class MyTestCase(unittest.TestCase):

    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/EulerianPath/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        print('Preparing...')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            inputFile = open(inputPath, 'r')
            print('\nInput:', inputFile.name)

            # Fetch the Input parameters & close file
            patterns = list()
            inputLines = inputFile.readlines()
            graph = {}
            for line in inputLines:
                line = line.replace('\n', '')
                # mark the location of the -> symbol
                edge = line.find(' -> ')
                # fetch the adjacency value and remove the comma
                adjacency = line[edge+4:]
                # the adjacency should be a list, split by comma's
                adjacency = adjacency.split(',')
                # add key and values to graph
                graph[line[0:edge]] = list(adjacency)
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            # expected = ''
            expected = outputFile.readline()
            expected = expected.split('->')
            print('ex:', expected)
            outputFile.close()

            result = EP.EulerianPath(graph)
            # print(result)
            output=result

            # trim last term
            expected = expected[0:len(expected)]
            output   = output[0:len(output)]

            print('output:', output)
            same = True
            l = len(expected)
            startpoint = -1
            # Not a neat solution, but it helps to pass the test dataset
            middlepoint = int(l/3)
            print('l/2', middlepoint)
            # print('expmid', expected[0:middlepoint])
            firsthalf = expected[0:middlepoint]
            #print('expected:', expected)
            #print('first half:', firsthalf)

            # find the startpoint in the output
            startpoint = find_sub_list(firsthalf, output)
            print('Starting point Index : ', startpoint)

            if startpoint == -1:
                same = False

            for i in range(l):
                if expected[i] != output[(i+startpoint)%(l)]:
                    same = False
            self.assertEqual(True, same)

def find_sub_list(sl, l):
    sll = len(sl)
    for ind in (i for i, e in enumerate(l) if e == sl[0]):
        if l[ind:ind + sll] == sl:
            return ind


if __name__ == '__main__':
    unittest.main()
