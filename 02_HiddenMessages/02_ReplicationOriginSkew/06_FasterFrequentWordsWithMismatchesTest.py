import unittest
# FrequentWords = __import__('06_FasterFrequentWordsWithMismatches')
FrequentWords = __import__('06_FrequentWordsWithMismatchesSorted')

class FrequentWordsCase(unittest.TestCase):
    def test_sample(self):
        input = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        k = 4
        d = 1
        expected = sorted(['GATG', 'ATGC', 'ATGT'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # checks that the result includes k-mers not included in Text
    def test_dataset1(self):
        input = 'AAAAAAAAAA'
        k = 2
        d = 1
        expected = sorted(['AA','AC','AG','CA','AT','GA','TA'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # make sure k and d are not accidently swapped
    def test_dataset2(self):
        input = 'AGTCAGTC'
        k = 4
        d = 2
        expected = sorted(['TCTC', 'CGGC', 'AAGC', 'TGTG', 'GGCC', 'AGGT', 'ATCC', 'ACTG', 'ACAC', 'AGAG', 'ATTA', 'TGAC', 'AATT', 'CGTT', 'GTTC', 'GGTA', 'AGCA', 'CATC'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # make sure you are not finding patterns in the reverse complement
    def test_dataset3(self):
        input = 'AATTAATTGGTAGGTAGGTA'
        k = 4
        d = 0
        expected = sorted(['GGTA'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # first make sure 'd' and less than d is considered, then make sure nor too little nor too many k-mers returned
    def test_dataset4(self):
        input = 'ATA'
        k = 3
        d = 1
        expected = sorted(['GTA', 'ACA', 'AAA', 'ATC', 'ATA', 'AGA', 'ATT', 'CTA', 'TTA', 'ATG'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # check that the code is not looking in the reverse complement of Text
    def test_dataset5(self):
        input = 'AAT'
        k = 3
        d = 0
        expected = sorted(['AAT'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

    # checks that code is correctly delimiting the output, and verify that k-mers are actually of length k
    def test_dataset6(self):
        input = 'TAGCG'
        k = 2
        d = 1
        expected = sorted(['GG', 'TG'])
        output = sorted(FrequentWords.FasterFrequentWordsWithMismatches(input, k, d))
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
