import unittest
ApproximatePatternCount = __import__('05_ApproximatePatternCount')

class ApproximatePatternCountCase(unittest.TestCase):
    def test_sample(self):
        Text = 'TTTAGAGCCTTCAGAGG'
        Pattern = 'GAGG'
        d = 2
        output = ApproximatePatternCount.ApproximatePatternCount(Text, Pattern, d)
        expected = 4
        self.assertEqual(output, expected)

    # check if the code is handling overlapping occurences in addition to greater than zero value
    def test_dataset1(self):
        Text = 'AAA'
        Pattern = 'AA'
        d = 0
        output = ApproximatePatternCount.ApproximatePatternCount(Text, Pattern, d)
        expected = 2
        self.assertEqual(output, expected)

    # check if the code allows less than d mismatches (not exactly d)
    def test_dataset2(self):
        Text = 'ATA'
        Pattern = 'ATA'
        d = 1
        output = ApproximatePatternCount.ApproximatePatternCount(Text, Pattern, d)
        expected = 1
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
