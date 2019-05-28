import unittest
from pathlib import Path
DB = __import__('06_DeBruijnGraph')

class DeBruijnCase(unittest.TestCase):
    def test_input(self):
        inputDirectory = '/Users/tleis/PycharmProjects/BioInformaticsI/03_GenomeSequencing/deBruijnGraphString/inputs'
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
            outlines = outputFile.readlines()
            for outline in outlines:
                outline = outline.replace('\n', '')
                expected.append(outline)
            outputFile.close()

            result = DB.DeBruijn(text,k)
            # Change format into XXX->YYY
            output = []
            for key, values in result.items():
                line = key
                for value in values:
                    if '->' in line:
                        line = line + ',' + value
                    else:
                        line = line + ' -> ' + value
                output.append(line)

            self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
