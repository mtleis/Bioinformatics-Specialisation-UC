import unittest
ReverseComplement = __import__('07_ReverseComplement')

class ReverseComplementCase(unittest.TestCase):
    def test_example1(self):
        input = 'AAAACCCGGT'
        expected = 'ACCGGGTTTT'
        output = ReverseComplement.ReverseComplement(input)
        self.assertEqual(expected, output)

    def test_example2(self):
        input = 'GCACTAAAGCACCAGCGAGACTAGACAGTGCCTTACGCTGTATAGGGATAAAAGTTGTCAAGATGACTTGCGGGAATCGTTAGGCTGACACGCACTAATGCTCGCCTTCCGGGTGTTCTGTGAGTACGGTTGATCACGGTCGCCCTGCGGATGTACTACCATGAAAGTTGATCACGTGCCGCGCGCTCCCTAAGCTTAGAAGTTTGCACAATCTGCATTCTATCCTGCCACGCCTTCAATAATAAGTGGTGTATGCAATTTGGAGTCGATCTGGGAACCAACGATTAACTTGGGAAGTGGCTATATCAAAATACGATGTCTTCAGCGTCGCGGTCGACGCTGCGCAACGAACGAAAAGTCCGATGGACCCGAACTCTGATTATACCGAATCTCCGCTTTTACGACTCGCCACATACCGGCATAAGCCATTCTGGGGCTTTGCCCCCTTAGGTCTAGCCCACCCCCGACCTAGCTTGAGCGTGTCACACCCCAACAGCCGCATTACGCCCGCTCACCGACACTTGGCGGTCGTATAAGAAATCCAAAACCGAGACGAAAACTGAAGAATAAGGTTCATTCAGCATTGTGGAGTTGACAACATCAGTATGAGGGTGAGTTGCGTCAAAGTCGAAGAATATGGAGGGTCAAATCACGAGATGTAACATCCACGCGAACACTTAGCTAGTAATCATTTTTCCGTAAAGAGTCGTTGAGTCCGACCAGTTGAAGCTCAGTGTTTATCCGGTAGGGAATTGTAGGATCAACGATAGGGTCGCGGAACCGCCGTATTATAGAAAGAGATAGTCCCAACGTTCTTTATGCACTTCGCTGAGAGAGGGTGACCGGGCACGCAGAGACTTTGGCTTTGTAGCCCCATTCCGCGGCTCTTCGGATACTGACTGAGCTGTAGTCGGCACATCCTTTACAACAAAAAAGCTCATGTCCGAGATTTTAATGGCGGCGCACGGTCACTCGGAGTTGACGAATGCGCAGCGAATCGTTGGTTCCAGATAAAGGCAAGGCTGTGTTACTGTTTCGGAGGGCAATCGTCAACGAGCAAAGATGTTAGAATAGAAATCGGAGCGAGGCTCCCAGCAAATATGAGTTAGGATCTTTTTTGCGAAAGGGTTGGTCTCCATCTCCTCTCGCCTGCGAGCGAGTCCCCGAAGCACGTTCAACCTATTTGATTCGGTGCAGGACACCCTAGATTAGCATACAGGTATAATATCAGGAAGAGTCACCTTTCATTCCCGACCAGTAGGATGTATAGGAATGAGACTATCCAGTTCTTTGTCAGCTCAAGACAGCGTTGGCAATACGGCCGAGTATTGGGGGGAATACCCCGGAACATAGTATTGTGCCTTAGCTATTGCCCTAGATACCACGCGGCCCTTGAGCATTTGTCTACACTTTGGTGATCCTAGGCACCCCGCGCTCGTGGCAACGTCAGCATCTTGTGATAGCAAAGCGTATGTACCTGTAATGTAACATCAAAGTATATCGGCACCCTAGTGGGGGCGAAGGTTGGATCGCTTATCACTCGGGACGACGGTGGTATCCAGCCACAGTGTTGCTCATTAACGACCACACAGCTCTTGGAATCGAGCCATGGACAGGGGACGCCCCAGGATACATGATGTTCCTGTGAGCACAAGCACTATGGCAGGCTTAGAGCTAATTCTTCCATTGGGCCGGTAAGACGCCAGAGAAAGTCACCGGTGTGAGAAAGGGTTTCGTGTGGGGGAGGCGTCAAACAACAAGGATTTACGTCGAACCGATCAGCCCTTGTCTGATTCATTCCAGGTTTAAGCGAGCCCTGGCGGTGACCTCCCGGGGATTCTTGGTGACGATAAGTGTAGACTGGTTTATGACTGTCTATAAGTGCAAGCAGTCCGCGACTCGGCCGCTCCTCAGATCTCGTCCTCCCAATCCTTACGAGGCACTATTCCGGCCCTAAAAACTTACCTACCAACCGGACATAGCGAACGGTCTAAGTTTTCGGAAATTGAATAACACTCGAACAAAGGAGCCCAATACATGGCACAAGCACACATAAAGCTTGGCGCTGCTGACGGCCGGCCCCCACAGCAGGTGGGTATATCAGGATAATGCTCTACCTCCTCGGGGATGACCAGAGACGAACGTTCGGACGCTATTAGTTAGTGGTCGCCCAGATATTCTCCTAATCAAGCCCTCGAAGGCTAGTCTAAATTTTAGCAAAAACTCGTATAGCAGCACATGCGGTAGACTGGGCCTCAGCCAGGTAGAGCTGTGGCTGCACTCGAGCAATCACTACCGTATAGAGTGGTGTTATTTCGGGGTGAATGTCAGGGGTGGTCCAAAATCACAAACACGTCTATTCGCACCCGGGAATGCTCATGTTCCCACGGCGGGCCTGTACAGATGTGAGAGGCAGCGATCATACAAAGTTGCCTGGCCTCCCCACGAACACACGGCGGCCCATTAGGTCTGAACAGGTTTATCGTTAATATATTTTGCGGTGG'
        expected = 'CCACCGCAAAATATATTAACGATAAACCTGTTCAGACCTAATGGGCCGCCGTGTGTTCGTGGGGAGGCCAGGCAACTTTGTATGATCGCTGCCTCTCACATCTGTACAGGCCCGCCGTGGGAACATGAGCATTCCCGGGTGCGAATAGACGTGTTTGTGATTTTGGACCACCCCTGACATTCACCCCGAAATAACACCACTCTATACGGTAGTGATTGCTCGAGTGCAGCCACAGCTCTACCTGGCTGAGGCCCAGTCTACCGCATGTGCTGCTATACGAGTTTTTGCTAAAATTTAGACTAGCCTTCGAGGGCTTGATTAGGAGAATATCTGGGCGACCACTAACTAATAGCGTCCGAACGTTCGTCTCTGGTCATCCCCGAGGAGGTAGAGCATTATCCTGATATACCCACCTGCTGTGGGGGCCGGCCGTCAGCAGCGCCAAGCTTTATGTGTGCTTGTGCCATGTATTGGGCTCCTTTGTTCGAGTGTTATTCAATTTCCGAAAACTTAGACCGTTCGCTATGTCCGGTTGGTAGGTAAGTTTTTAGGGCCGGAATAGTGCCTCGTAAGGATTGGGAGGACGAGATCTGAGGAGCGGCCGAGTCGCGGACTGCTTGCACTTATAGACAGTCATAAACCAGTCTACACTTATCGTCACCAAGAATCCCCGGGAGGTCACCGCCAGGGCTCGCTTAAACCTGGAATGAATCAGACAAGGGCTGATCGGTTCGACGTAAATCCTTGTTGTTTGACGCCTCCCCCACACGAAACCCTTTCTCACACCGGTGACTTTCTCTGGCGTCTTACCGGCCCAATGGAAGAATTAGCTCTAAGCCTGCCATAGTGCTTGTGCTCACAGGAACATCATGTATCCTGGGGCGTCCCCTGTCCATGGCTCGATTCCAAGAGCTGTGTGGTCGTTAATGAGCAACACTGTGGCTGGATACCACCGTCGTCCCGAGTGATAAGCGATCCAACCTTCGCCCCCACTAGGGTGCCGATATACTTTGATGTTACATTACAGGTACATACGCTTTGCTATCACAAGATGCTGACGTTGCCACGAGCGCGGGGTGCCTAGGATCACCAAAGTGTAGACAAATGCTCAAGGGCCGCGTGGTATCTAGGGCAATAGCTAAGGCACAATACTATGTTCCGGGGTATTCCCCCCAATACTCGGCCGTATTGCCAACGCTGTCTTGAGCTGACAAAGAACTGGATAGTCTCATTCCTATACATCCTACTGGTCGGGAATGAAAGGTGACTCTTCCTGATATTATACCTGTATGCTAATCTAGGGTGTCCTGCACCGAATCAAATAGGTTGAACGTGCTTCGGGGACTCGCTCGCAGGCGAGAGGAGATGGAGACCAACCCTTTCGCAAAAAAGATCCTAACTCATATTTGCTGGGAGCCTCGCTCCGATTTCTATTCTAACATCTTTGCTCGTTGACGATTGCCCTCCGAAACAGTAACACAGCCTTGCCTTTATCTGGAACCAACGATTCGCTGCGCATTCGTCAACTCCGAGTGACCGTGCGCCGCCATTAAAATCTCGGACATGAGCTTTTTTGTTGTAAAGGATGTGCCGACTACAGCTCAGTCAGTATCCGAAGAGCCGCGGAATGGGGCTACAAAGCCAAAGTCTCTGCGTGCCCGGTCACCCTCTCTCAGCGAAGTGCATAAAGAACGTTGGGACTATCTCTTTCTATAATACGGCGGTTCCGCGACCCTATCGTTGATCCTACAATTCCCTACCGGATAAACACTGAGCTTCAACTGGTCGGACTCAACGACTCTTTACGGAAAAATGATTACTAGCTAAGTGTTCGCGTGGATGTTACATCTCGTGATTTGACCCTCCATATTCTTCGACTTTGACGCAACTCACCCTCATACTGATGTTGTCAACTCCACAATGCTGAATGAACCTTATTCTTCAGTTTTCGTCTCGGTTTTGGATTTCTTATACGACCGCCAAGTGTCGGTGAGCGGGCGTAATGCGGCTGTTGGGGTGTGACACGCTCAAGCTAGGTCGGGGGTGGGCTAGACCTAAGGGGGCAAAGCCCCAGAATGGCTTATGCCGGTATGTGGCGAGTCGTAAAAGCGGAGATTCGGTATAATCAGAGTTCGGGTCCATCGGACTTTTCGTTCGTTGCGCAGCGTCGACCGCGACGCTGAAGACATCGTATTTTGATATAGCCACTTCCCAAGTTAATCGTTGGTTCCCAGATCGACTCCAAATTGCATACACCACTTATTATTGAAGGCGTGGCAGGATAGAATGCAGATTGTGCAAACTTCTAAGCTTAGGGAGCGCGCGGCACGTGATCAACTTTCATGGTAGTACATCCGCAGGGCGACCGTGATCAACCGTACTCACAGAACACCCGGAAGGCGAGCATTAGTGCGTGTCAGCCTAACGATTCCCGCAAGTCATCTTGACAACTTTTATCCCTATACAGCGTAAGGCACTGTCTAGTCTCGCTGGTGCTTTAGTGC'
        output = ReverseComplement.ReverseComplement(input)
        self.assertEqual(expected, output)

    # This makes sure you didn't forget one of the two steps(Reverse, complement)
    def test_example3(self):
        input = 'ACACAC'
        expected = 'GTGTGT'
        output = ReverseComplement.ReverseComplement(input)
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()