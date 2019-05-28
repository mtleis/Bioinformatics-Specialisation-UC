import unittest
from pathlib import Path
EC = __import__('01_EulerianCycle')

class MyTestCase(unittest.TestCase):
    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/EulerianCycle/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            inputFile = open(inputPath, 'r')
            print('Input:', inputFile.name)

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
                print('Adjacency: ', adjacency)
                # adjacency = adjacency.replace(',', '')
                # add key and values to graph
                graph[line[0:edge]] = list(adjacency)
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            #expected = ''
            expected = outputFile.readline()
            #for outline in outlines:
            #    outline = outline.replace('\n', '')
            #    expected.append(outline)
            # print(expected)
            # expected=list(expected)
            # expected = list(expected.replace('->', ','))
            expected = expected.split('->')
            print('ex:', expected)
            outputFile.close()

            result = EC.EulerianCycle(graph)
            print(result)
            output=result
            # Change format into X->Y->...->Z
            #output = []
            #for i in range(len(result)):
            #    output = '->'.join(result)

            # print('output', output)
            # output = output.replace('->', '')


            # trim last term
            expected = expected[0:len(expected)-1]
            output   = output[0:len(output)-1]

            print('output:', output)
            same = True
            l = len(expected)
            startpoint = -1
            middlepoint = int(l/2)
            print('l/2', middlepoint)
            print('expmid', expected[0:middlepoint])
            firsthalf = expected[0:middlepoint]
            print('expected:', expected)
            print('first half:', firsthalf)

            # find the startpoint in the output
            startpoint = find_sub_list(firsthalf, output)
            print('Starting point : ', startpoint)

            # to be sub-list in list
            #n = int(l/2)
            #expectedlists = [i for j in [[expected[t:t + n] for x in expected[:1:t + 1] if (t % n) == False] for t in range(len(expected))] for i in j]
            #print('the first half: ', expectedlists[0])

            # find the sub list location
            # startpoint = output.find(expected[0:middlepoint])

            if startpoint == -1:
                same = False

            for i in range(l):
            #    print('i', i)
                if expected[i] != output[(i+startpoint)%l]:
            #       print('index', (i+startpoint)%l)
                    same = False
            # print('Start: ', startpoint, 'expec[0]', expected[0])
            self.assertEqual(True, same)
            # self.assertEqual(expected, output)



def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind

if __name__ == '__main__':
    unittest.main()
