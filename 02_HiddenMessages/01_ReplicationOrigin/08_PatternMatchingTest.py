import unittest
PatternMatching = __import__('08_PatternMatching')

class PatternMatchingCase(unittest.TestCase):
    def test_example1(self):
        pattern = 'ATAT'
        genome = 'GATATATGCATATACTT'
        expected = [1, 3, 9]
        output = PatternMatching.PatternMatching(pattern, genome)
        self.assertEqual(output, expected)

    # This makes sure reverse complement are not returned
    def test_example2(self):
        pattern = 'ACAC'
        genome = 'TTTTACACTTTTTTGTGTAAAAA'
        expected = [4]
        output = PatternMatching.PatternMatching(pattern, genome)
        self.assertEqual(output, expected)

    # checks for off-by-one error at the begining of genome
    def test_example3(self):
        pattern = 'AAA'
        genome = 'AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT'
        expected = [0, 46, 51, 74]
        output = PatternMatching.PatternMatching(pattern, genome)
        self.assertEqual(output, expected)

    # Checks for off-by-one error at the end of genome
    def test_example4(self):
        pattern = 'TTT'
        genome = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
        expected = [88, 92, 98, 132]
        output = PatternMatching.PatternMatching(pattern, genome)
        self.assertEqual(output, expected)

    # accounts for overlapping cases in genome
    def test_example5(self):
        pattern = 'ATA'
        genome = 'ATATATA'
        expected = [0,2,4]
        output = PatternMatching.PatternMatching(pattern, genome)
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
