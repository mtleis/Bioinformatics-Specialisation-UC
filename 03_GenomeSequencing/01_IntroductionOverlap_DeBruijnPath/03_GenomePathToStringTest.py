import unittest
from pathlib import Path
GP = __import__('03_GenomePathToString')

class GenomePathToStringCase(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, False)

    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/GenomePath/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            print('Input Path: ' , inputPath)

            # Fetch Input
            inputFile = open(inputPath, 'r')
            genomePath = list()
            lines = inputFile.readlines()
            for line in lines:
                line = line.replace('\n', '')
                genomePath.append(line)
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            expected = str(outputFile.readline())
            outputFile.close()

            # call method and get output
            output = (GP.GenomePathToString(genomePath))

            self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
