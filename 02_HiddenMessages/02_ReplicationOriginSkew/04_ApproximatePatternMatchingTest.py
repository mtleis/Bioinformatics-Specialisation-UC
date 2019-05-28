import unittest
ApproximatePatternMatching = __import__('04_ApproximatePatternMatching')

class ApproximatePatternMatchingCase(unittest.TestCase):
    def test_sample(self):
        pattern = 'ATTCTGGA'
        text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
        d = 3
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [6, 7, 26, 27]
        self.assertEqual(output, expected)

    # make sure you are not only couting instances equal to d
    def test_dataset1(self):
        pattern = 'AAA'
        text = 'TTTTTTAAATTTTAAATTTTTT'
        d = 2
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [4, 5, 6, 7, 8, 11, 12, 13, 14, 15]
        self.assertEqual(output, expected)

    # check for off-by-one error at the beginning
    def test_dataset2(self):
        pattern = 'GAGCGCTGG'
        text = 'GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT'
        d = 2
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [0, 30, 66]
        self.assertEqual(output, expected)

    # checks for off-by-one at the end of Text
    def test_dataset3(self):
        pattern = 'AATCCTTTCA'
        text = 'CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGCGCCATAATCCAAACA'
        d = 3
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [3, 36, 74, 137]
        self.assertEqual(output, expected)

    # are we correctly accouting for overlapping of Pattern within Text?
    def test_dataset4(self):
        pattern = 'CCGTCATCC'
        text = 'CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATTGC'
        d = 3
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [0, 7, 36, 44, 48, 72, 79, 112]
        self.assertEqual(output, expected)

    # are you only counting less than d mismatches?
    def test_dataset5(self):
        pattern = 'TTT'
        text = 'AAAAAA'
        d = 3
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [0, 1, 2, 3]
        self.assertEqual(output, expected)

    # are you only counting less than d mismatches?
    def test_dataset6(self):
        pattern = 'CCA'
        text = 'CCACCT'
        d = 0
        output = ApproximatePatternMatching.ApproximatePatternMatching(text, pattern, d)
        expected = [0]
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
