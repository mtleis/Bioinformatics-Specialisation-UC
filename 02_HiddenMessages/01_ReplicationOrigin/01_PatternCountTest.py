import unittest
PatternCount = __import__('01_PatternCount')

class PatternCountTest(unittest.TestCase):
    # a test method should always start with test_ !!
    def test_patterncount(self):
        Dna = 'AGAGCTGCTGCGAAGTACCGAAGTACCGTTAAAGAAGTACCATCTCGAAGTACCGGCGAAGTACAGCGAAGTACATACGGAAGTACGAAGTACAAGGAAGTACGAAGTACGAAGTACGAAGTACACCGGGAAGTACGAAGTACCACTGAAGTACTGGAAGTACGGAAGTACGAGAAGTACCTCCGAAGTACCGAAGTACCAGGAAGTACTGGGAAGTACAGAGAAGTACTTGGAAGTACCCCTGAAGTACGCGCGAAGTACGATCCTGAAGTACGAGAAGTACGGGGAAGTACTATGAAGTACGAACACCGAAGTACGGAAGTACGAGAAGTACTATCGTTGGAAGTACATTATTTGAAGTACGAAGTACCGAAGTACCGAAGTACGAAGTACAGAAGTACACCCATGAAGTACGGCGAAGTACGAAGTACTGAAGTACCAGAAGTACCCAGCGAAGTACTGCTCATCGAAGTACGCGAAGTACCTGGGAAGTACGAAGTACTTGTATTATCGAAGTACTCGAAGTACGAAGTACGCAAGACTGGAAGTACGAGTGACAGAAGTACAACGTTAAACGACGAAGTACGTCGAAGTACAACGAAGTACGTAGAAGTACAATGAAGTACGAAGTACGCGGCAGAAGTACCGAAGTACGCTGAAGTACGAAGTACTTCGAAGTACTGATAGAAGTACGTGAAGTACCAAGAAGTACTACGGTGAAGTACGCGAAGTACGAAGTACGTGCGAAGTACCATGAAGTACTGCTTGGAAGTACTGGAAGTACTGCCCTGAAGTACGAAGTACTTTTATGAAGTACGGAAGTACGAATGAAGTACAGAAGTACGAAGTACTAATCAAGGGAAGTACGAAGTACGTCGAAGTACCCCGAAGTACCGGAAGTACCCGGAAGTACCCCGAAGTACCGAAGTACGAAGTACTGGAAGTACTGAAGTACGAAGTACTCGCCACCGAGAGGAAGTACCGGGTTCGAGAAGTACGAAGTACTCCGAAGTACGAAGTACGGGGAAGTACACGAAGTACCTGTGAAGTACCGAAGTAC'
        pattern = 'GAAGTACGA'
        output = 27
        self.assertEqual(PatternCount.PatternCount(Dna, pattern), output)

if __name__ == '__main__':
    unittest.main()
