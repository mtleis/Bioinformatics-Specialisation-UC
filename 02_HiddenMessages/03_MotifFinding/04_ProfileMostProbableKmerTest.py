import unittest
PK = __import__('04_ProfileMostProbableKmer')

class ProfileMostProbableKmerTestCase(unittest.TestCase):
    # checks off-by-one error at the beginning
    def test_dataset1(self):
        text = 'AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT'
        k = 8
        profile = {
            'A': [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
            'C': [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
            'G': [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
            'T': [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1] }
        expected = 'AGCAGCTT'
        output = PK.ProfileMostProbableKmer(text, k, profile)
        self.assertEqual(expected, output)

    # checks for off-by-one error at the end of text
    def test_dataset2(self):
        text = 'TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA'
        k = 12
        profile = {
        'A': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
        'C': [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
        'G': [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
        'T': [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3] }
        expected = 'AAGCAGAGTTTA'
        output = PK.ProfileMostProbableKmer(text, k, profile)
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
