import unittest
from pathlib import Path
OG = __import__('04_Overlap')

class OverlapCase(unittest.TestCase):

    # input & output are 1 string list each
    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/OverlapGraph/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            print('Input Path: ' , inputPath)

            # Fetch Input
            inputFile = open(inputPath, 'r')
            inputKmers = list()
            lines = inputFile.readlines()
            for line in lines:
                line = line.replace('\n', '')
                inputKmers.append(line)
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            expected = list()
            outlines = outputFile.readlines()
            for outline in outlines:
                outline = outline.replace('\n', '')
                expected.append(outline)
            outputFile.close()

            # call method and get output
            result = OG.Overlap(inputKmers)
            # Change format into XXX->YYY
            output = []
            for key, values in result.items():
                line = key
                for value in values:
                    if '->' in line:
                        line = line + ',' + value
                    else:
                        line = line + '->' + value
                output.append(line)

            self.assertEqual(sorted(output), sorted(expected))

if __name__ == '__main__':
    unittest.main()
