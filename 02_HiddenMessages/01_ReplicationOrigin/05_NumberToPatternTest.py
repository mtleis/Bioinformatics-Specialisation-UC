import unittest
NumberToPattern = __import__('05_NumberToPattern')

class NumberToPatternCase(unittest.TestCase):
    def test_example1(self):
        number = 45
        k = 4
        output = 'AGTC'
        self.assertEqual(NumberToPattern.NumberToPattern(number, k), output)

    def test_example2(self):
        number = 5353
        k = 7
        output = 'CCATGGC'
        self.assertEqual(NumberToPattern.NumberToPattern(number, k), output)

if __name__ == '__main__':
    unittest.main()
