import re
import unittest
from pathlib import Path
Composition = __import__('02_Composition')

class CompositionCase(unittest.TestCase):

    def test_sample(self):
        text = 'CAATCCAAC'
        k = 5
        output = Composition.Composition(text, k)
        expected =  [ 'CAATC', 'AATCC', 'ATCCA', 'TCCAA', 'CCAAC' ]
        self.assertEqual(output, expected)

    # dataset 1
    def test_dataset1(self):
        file = open('dataset1', 'r')
        file.readline() # this is Input label
        k = int(file.readline())
        text = str(file.readline())
        print('text len:', len(text))

        expected = list()
        f = file.readlines()
        for line in f:
            line.replace('\n', '')
            expected.append(line)
        output = sorted(Composition.Composition(text, k))
        file.close()
        # list are very long and takes a long time, hence only comparing lengths
        self.assertEqual(len(output), len(expected))

    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/kmerComposition/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            inputFile = open(inputPath, 'r')
            print('Input:', inputFile.name)

            # Fetch the Input parameters & close file
            k = int(inputFile.readline())
            text = str(inputFile.readline())
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            expected = list()
            lines = outputFile.readlines()
            for line in lines:
                line = line.replace('\n', '')
                expected.append(line)
            outputFile.close()

            # call method and get output
            output = sorted(Composition.Composition(text, k))

            self.assertEqual(sorted(output), sorted(expected))

if __name__ == '__main__':
    unittest.main()
