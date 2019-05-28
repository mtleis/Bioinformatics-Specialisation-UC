import unittest
from pathlib import Path
PKG = __import__('07_PairedCompositionGraph')

class MyTestCase(unittest.TestCase):
    def test_something(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/02_GenomeAssembly/PairedStringReconstruction/inputs'
        pathlist = Path(inputDirectory).glob('**/*.txt')
        for path in pathlist:
            # Read input, output paths
            inputPath = str(path)
            outputPath = inputPath.replace('inputs', 'outputs')
            inputFile = open(inputPath, 'r')
            print('Input:', inputFile.name)

            # Fetch the Input parameters & close file
            patterns = list()
            firstline = inputFile.readline()
            params = firstline.split()
            k = int(params[0])
            d = int(params[1])

            inputLines = inputFile.readlines()
            for line in inputLines:
                line = line.replace('\n', '')
                patterns.append(line)
            inputFile.close()
            print(patterns)
            # read output
            outputFile = open(outputPath, 'r')
            expected = ''
            outlines = outputFile.readlines()
            for outline in outlines:
                outline = outline.replace('\n', '')
                # expected.append(outline)
                expected = outline
            outputFile.close()

            output = PKG.PairedCompositionGraph(patterns, k,d)
            print('expected:', expected)
            self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
