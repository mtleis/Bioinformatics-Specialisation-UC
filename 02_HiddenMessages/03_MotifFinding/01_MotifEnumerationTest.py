import unittest
ME = __import__('01_MotifEnumeration')

class MotifEnumerationCase(unittest.TestCase):
    def test_sample(self):
        input = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
        k = 3
        d = 1
        expected = ['ATA', 'ATT', 'GTT', 'TTT']
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

    # check for off-by-one errors
    def test_dataset1(self):
        input = ['ACGT', 'ACGT', 'ACGT']
        k = 3
        d = 0
        expected = ['ACG', 'CGT']
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

    # check if code works for d > 0. The expected answer should contain AAA and all variants with 1 mismatch
    def test_dataset2(self):
        input = ['AAAAA', 'AAAAA', 'AAAAA']
        k = 3
        d = 1
        expected = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'AGA', 'ATA', 'CAA', 'GAA', 'TAA']
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

    # check if the code considers number of mismatches = d as well as less than d.
    # An incorrect solution could find AAA and all 1 and 2 mismatches, but not 3.
    def test_dataset3(self):
        input = ['AAAAA', 'AAAAA', 'AAAAA']
        k = 3
        d = 3
        expected = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

    # check whether code is considering last Dna sequence. In which case 'AAA' is not an option
    def test_dataset4(self):
        input = ['AAAAA', 'AAAAA', 'AACAA']
        k = 3
        d = 0
        expected = []
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

    # check whether code is considering first Dna sequence. In which case 'AAA' is not an option
    def test_dataset5(self):
        input = ['AACAA', 'AAAAA', 'AAAAA']
        k = 3
        d = 0
        expected = []
        output = ME.MotifEnumeration(input, k, d)
        self.assertEqual(sorted(expected), sorted(output))

if __name__ == '__main__':
    unittest.main()
