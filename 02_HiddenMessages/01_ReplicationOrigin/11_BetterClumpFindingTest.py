import unittest
BetterClumpFinding = __import__('11_BetterClumpFinding')

class ClumpFindingCase(unittest.TestCase):
    def test_example1(self):
        input = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
        k = 5
        L = 50
        t = 4
        expected = ['CGACA', 'GAAGA']
        output = BetterClumpFinding.BetterClumpFinding(input, k, L, t)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
