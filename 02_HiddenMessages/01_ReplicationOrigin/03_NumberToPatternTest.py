import unittest
NumberToPattern = __import__('03_NumberToPattern')

class NumberToPatternCase(unittest.TestCase):
    def test_example(self):
        number = 5437
        length = 7
        answer = 'CCCATTC'
        self.assertEqual(NumberToPattern.NumberToPattern(number, length), answer)

    def test_example2(self):
        number = 5437
        length = 8
        answer = 'ACCCATTC'
        self.assertEqual(NumberToPattern.NumberToPattern(number, length), answer)

if __name__ == '__main__':
    unittest.main()
