import unittest
DP = __import__('03_DistanceBetweenPatternAndStrings')

class DistanceBetweenPatternAndStringsCase(unittest.TestCase):
    def test_sample(self):
        Dna = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
        Pattern = 'AAA'
        expected = 5
        output = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        self.assertEqual(expected, output)

    # checks that all 3 sequences are used, also check that it is not using the first kmer nor the last kmers in the sequence
    def test_dataset1(self):
        Dna = ['TTTATTT', 'CCTACAC', 'GGTAGAG']
        Pattern = 'TAA'
        expected = 3
        output = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        self.assertEqual(expected, output)

    # ensures that min is used, not max or sum
    def test_dataset2(self):
        Dna = ['AAACT', 'AAAAC', 'AAAG']
        Pattern = 'AAA'
        expected = 0
        output = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        self.assertEqual(expected, output)

    # Check for off-by-one error at the end of sequence
    def test_dataset3(self):
        Dna = ['TTTTAAA', 'CCCCAAA', 'GGGGAAA']
        Pattern = 'AAA'
        expected = 0
        output = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        self.assertEqual(expected, output)

    # Check for off-by-one error at the beginning of sequence
    def test_dataset4(self):
        Dna = ['AAATTTT', 'AAACCCC', 'AAAGGGG']
        Pattern = 'AAA'
        expected = 0
        output = DP.DistanceBetweenPatternAndStrings(Pattern, Dna)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
