import unittest
from pathlib import Path
DBK = __import__('07_DeBruijnFromKmers')

class DBFromKmersTestCase(unittest.TestCase):
    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/deBruijnGraphPatterns/inputs'
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
            for line in inputLines:
                line = line.replace('\n', '')
                patterns.append(line)
            inputFile.close()

            # read output
            outputFile = open(outputPath, 'r')
            expected = list()
            outlines = outputFile.readlines()
            for outline in outlines:
                outline = outline.replace('\n', '')
                expected.append(outline)
            outputFile.close()

            result = DBK.DeBruijnFromKmers(patterns)
            # Change format into XXX->YYY
            output = []
            for key, values in result.items():
                line = key
                print('line:', line)
                for value in values:
                    if '->' in line:
                        line = line + ',' + value
                    else:
                        line = line + ' -> ' + value
                output.append(line)

            self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
