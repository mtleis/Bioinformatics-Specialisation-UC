import unittest
MS = __import__('02_MedianString')

class MedianStringCase(unittest.TestCase):
    # there is actually two solutions for sample dataset
    def test_sample(self):
        Dna = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG']
        expected = 'ACG'
        expected2= 'GAC'
        output = MS.MedianString(Dna,3)
        self.assertEqual((expected or expected2), output)

    # is the output of correct length? (exactly of length k)
    def test_dataset1(self):
        Dna = ['ACGT','ACGT','ACGT']
        k = 3
        expected = 'ACG'
        expected2= 'CGT'
        output = MS.MedianString(Dna, k)
        self.assertEqual((expected or expected2), output)

    # Checks if the code considers k-mer that are not in the input
    def test_dataset2(self):
        Dna = ['ATA', 'ACA', 'AGA', 'AAT', 'AAC']
        k = 3
        expected = 'AAA'
        output = MS.MedianString(Dna, k)
        self.assertEqual(expected, output)

    # check if output contains a single k-mer
    def test_dataset3(self):
        Dna = ['AAG', 'AAT']
        k = 3
        expected = 'AAG'
        expected2= 'AAT'
        output = MS.MedianString(Dna, k)
        self.assertEqual((expected or expected2), output)
if __name__ == '__main__':
    unittest.main()
