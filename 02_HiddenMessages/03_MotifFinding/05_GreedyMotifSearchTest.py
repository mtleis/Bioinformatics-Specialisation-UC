import unittest
GM = __import__('05_GreedyMotifSearch')

class GreedyMotifSearchTestCase(unittest.TestCase):
    def test_sample(self):
        Dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
        k = 3
        t = 5
        expected = ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
        output = GM.GreedyMotifSearch(Dna, k, t)
        self.assertEqual(sorted(expected), sorted(output))

    # Code should always pick the first occuring 'most-probable-kmer'
    def test_dataset1(self):
        Dna = ['GCCCAA', 'GGCCTG', 'AACCTA', 'TTCCTT']
        k = 3
        t = 4
        expected = ['GCC', 'GCC', 'AAC', 'TTC']
        output = GM.GreedyMotifSearch(Dna, k, t)
        self.assertEqual(sorted(expected), sorted(output))

    # Checks for off-by-one error at the beginning
    def test_dataset2(self):
        Dna = [
            'GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC', 'TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC',
            'TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT', 'GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG',
            'GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT', 'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT',
            'AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG', 'AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA'
        ]
        k = 5
        t = 8
        expected = ['GAGGC', 'TCATC', 'TCGGC', 'GAGTC', 'GCAGC', 'GCGGC', 'GCGGC', 'GCATC']
        output = GM.GreedyMotifSearch(Dna, k, t)
        self.assertEqual(sorted(expected), sorted(output))

    # Checks for off-by-one error at the end
    def test_dataset3(self):
        Dna = ['GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT',
               'CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT',
               'GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT',
               'AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC',
               'ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG' ]
        k = 6
        t = 5
        expected = ['GTGCGT', 'GTGCGT', 'GCGCCA', 'GTGCCA', 'GCGCCA']
        output = GM.GreedyMotifSearch(Dna, k, t)
        self.assertEqual(sorted(expected), sorted(output))

    def test_dataset4(self):
        Dna = [
            'GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA',
            'TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA',
            'GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA',
            'GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC',
            'AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA',
            'AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA',
            'GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA',
            'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT' ]
        k = 5
        t = 8
        expected = ['GCAGC', 'TCATT', 'GGAGT', 'TCATC', 'GCATC', 'GCATC', 'GGTAT', 'GCAAC']
        output = GM.GreedyMotifSearch(Dna, k, t)
        self.assertEqual(sorted(expected), sorted(output))

if __name__ == '__main__':
    unittest.main()
