import unittest
FW = __import__('11_FrequentWordsWithMismatchesAndReverseComplements')

class FrequentWordsAndReverseComplementCase(unittest.TestCase):
    def test_sample(self):
        Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        k = 4
        d = 1
        expected = sorted(['ACAT', 'ATGT'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(Text, k, d))
        self.assertEqual(expected, output)

    # k-mers that do not actaully appear in Text
    def test_dataset1(self):
        Text = 'AAAAAAAAAA'
        k = 2
        d = 1
        expected = sorted(['AT', 'TA'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(Text, k, d))
        self.assertEqual(expected, output)

    # make sure k and d are not accidently swapped
    def test_dataset2(self):
        input = 'AGTCAGTC'
        k = 4
        d = 2
        expected = sorted(['AATT', 'GGCC'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(input, k, d))
        self.assertEqual(expected, output)

    # make sure you are finding patterns in the reverse complement as well
    def test_dataset3(self):
        input = 'AATTAATTGGTAGGTAGGTA'
        k = 4
        d = 0
        expected = sorted(['AATT'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(input, k, d))
        self.assertEqual(expected, output)

    # first make sure 'd' and less than d is considered, then make sure nor too little nor too many k-mers returned
    def test_dataset4(self):
        input = 'ATA'
        k = 3
        d = 1
        expected = sorted(['AAA', 'AAT', 'ACA', 'AGA', 'ATA', 'ATC', 'ATG', 'ATT', 'CAT', 'CTA', 'GAT', 'GTA', 'TAA', 'TAC', 'TAG', 'TAT', 'TCT', 'TGT', 'TTA', 'TTT'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(input, k, d))
        self.assertEqual(expected, output)

    # check that the code is looking in the reverse complement of Text
    def test_dataset5(self):
        input = 'AAT'
        k = 3
        d = 0
        expected = sorted(['AAT', 'ATT'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(input, k, d))
        self.assertEqual(expected, output)

    # checks that code is correctly delimiting the output, and verify that k-mers are actually of length k
    def test_dataset6(self):
        input = 'TAGCG'
        k = 2
        d = 1
        expected = sorted(['CA', 'CC', 'GG', 'TG'])
        output = sorted(FW.FrequentWordsWithMismatchesAndReverseComplements(input, k, d))
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
