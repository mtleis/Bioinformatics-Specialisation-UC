GS = __import__('03_GibbsSampler')

Dna = [
'GGAAACTGAGAGGTCTCTAGCCTTTCTACCGGGAATGTTAACCCTCTTAGTCTCACACGTCAGTAACTGTACCCTATGGACCCAAACCCACTCGTAACGGATTACTGCAGTTGGAACCTCTAAATGATTGCTATACTCCGCTTGATGGATCATACA',
'GCGAGTGTGTTCAACCGTTTGGTTCAAAGCTTATTGACGGGTGACTTCAAACCTACACTGCACTCCCCACACATATGCTTCTCGTTGGGTGTTGCCATTTGAGCGCTGGCAACGGCTTGTCACAGACATCGGTGCTCCTTGCCACCTAAGGAATCC',
'CCAAGCTGAAGGAGGATCTACCAGTCGGGTCACTGCCTCACAGGTAGTAAGGCCAGGTTTCGTGCACCACCGTCGGCGGATTGCGCATTTATACTCCCTACATAGGCCGAAACGTAGGAAAACGTATGTAGCCGCTCCCTGAGTGCGTAGACACGT',
'CTCGACGCTAGAAGCTACATCGTTTAAGCGTTCTACGGAAAACGCTGGCTCAGTACTTACGCAGACGCCGATGGGACCAGTTCTCGCGACTATACGCCGATACCCGCACTTGCTGCACGCGCGGCTCACTACGTTCAGGCATCAAGCTCGTAATCC',
'ATGCAGGAACAGCGGTGAAGAACGGCGGATAACTGCTCAGCTCCCTGAAACGCCAACATACAATCCGTCTGGGAGACAGGCTTAGGGTCCGGTCATGGTTCCAGTAGCTTTCGCGGTAAGTCCCAAGTGCTTGTCCTTATTATAAGCCACGTCTTC',
'TTGCCCCGCGTCAAACTTCTCACTTTAGTATCGCTCTTTGCGAACCGGGTAACAGTGCGCCTAAGATGCGGCCCGGCTGACTTCCCTTACACACGGTGATTTCTGAGAGGGCACCATGATAAGGATCCAAAAACTTGTTGAAGCTGGACTGCGAGT',
'TTGGTACCTTCGAGAGTGACATTGCACTCTTCGAGACTAGCATAGAACTCCTTCCCAAACTGCGATAGGTTTAGGTCCGTCTCGCCGGCTTACTCCCCACCCCAAGCGAGACCTACTGTCCTAGATCTTTAGTCTTATACCTATTACAAATACGAT',
'TAATAGTGGCAATCGGCTAACTCCTTAGGCCAAGTGAAAACTCATTGACAGGTAGACCAGGACTACGCGTCTGTGACTTTCAAGCAACGCAAAAGGTATCTATAGTGAGGTATTTGCTGGCTTCGCAAGGGAATCTGGTCTGGTTCTGGAAATATA',
'CGTAGCGGGTGAGGAGACTCGAGCTTACCGACGATGAAACTAGGAGAGGCGGCTTACTTCCTCGTCACCTGTTAGCGTCTTCTACCGTTCTCTCTCTTTCATATTATAATAATTCAAAGTGACTATTGCCACTTCAGTTGAGGAGAGGGAGTACTG',
'CGAGACACGTTATGCTAAGTCCATAGATGGTCGCGTGTTTGCATGAAACAGAATCATCCCTCTTAGCCCCACTTATCACACCCTTCCAAAGTCAACTCTGTGTCATAGCTAATCACTAGCAACTATAAGCTTTCACGGCCTGACCCGGTTAACTCC',
'GGCCCTCGCGGTCTGGCGCTGATCAAAATGGCCAAGTAAAGCCTGTGGGCGGATCACTACTTTCCCCTGACTTAGTTGAGTTAAATTGGGTCTTGAGATAAAGCGGGACCACTACCAGTCCATGAACACCATATATACTGACGAGCAACTAGTTGC',
'CTTACCCACAAAGCGGCTAACTCCGTCAAACGGCAGGCTCTGAGACAACAGAGCGTTGATACTCTTGCAGAGATGCATCGAAGACAAGTTTCGACGCGTCGATTAGGTTTGCTTATTACTCTTGCTTGGTTACGCATGAACTTTTCAGTTAATTCC',
'TTTTAGAATCGAGGGGCTACGTGTCGTTAAGAACCGGACAAGATTTAGTACCGCCGCTAAAGGAACGGAATTCCGTTGTGAAAACAACCGGAGCATGTTTGTTGTTCAGCGGGTTACTGCGCGATTATCTAGTCAGACATGGAGATACTTAAGCGA',
'GACCACGTGGCTGTACGTCCTATTGTCAAATCAGAAACTCAGAGTACAAGTCAACCGATATGCACCTACCGTCTTATTCAACGACCTCGCTTGGTCGCTAACAAACGATTCACCCAATGGAAATCTAACCGCGTTCTGTGAGTTACGGCTCACTAC',
'AGTGCTCGCTAGGATCAAACGACCTCGGCTTACTTCGCGCGGTCCGATCCGGGTGATAAAATGGGATCCATTGAGTACCGGTTCCTGCGTCCTCCTTCAGGAAAGGCGAGCCTATAATCGGGTTGACGCGCAGTAAGGGGCTTACGCTGAAGGTGA',
'AAGGGGAGAGACAATCCTTTCGCATAAGAAACTAATGTTGGCCCCGTCTGGGGTTAGCGGGCGCTGACTAATCTGTCCGAAGCCTGAAAAATCTCTCGTTAATCCCGGTCTTCATATCACGCAAGCCCCGGTTCACAGGGGGCTCCGGGTTACTCC',
'ATGCTGGGGAGGTAAAGCGATGCCAGGCACACCCGGGCCCTGACAGGGTAGAGACGGGATTCGGTTTACTGCTTCAACTAGGCTTAGTTATCCTAGGTACATGTAACGTATACAATTATACATGTAATAGGAACTCCAACTGCGTTGTCACTGAGT',
'GAAATCTGTCTACAATAATAACCAAGCCACTGAAGCAATCTGTCGAGGCTTCCACGAAATGGAGGAATTATTCCTCTCAATACTTTATGAGGCGGGTGCTTCTTCCATTCGGCTCACTGCCACTAGGGACGATTTATGTTGAGGACGGCTCGCCAA',
'CCAGACAACAGGTTTATCTACTCATCGGTTGACTTCTAGTTCCATCACCCTGGGCCTATGTGGTTGACTGGATAACCTAAGGACGATGATAAGCATATTGGACAGCACCATTGGACAACGCCCAGGCATACTAAGGCCCAGGAGTCGTGTTCCCTT',
'GCGCAGGGTAATCCCCGCCCTGCTTGTATAGTCACAGTGTCCGCCCATGACTTCCTAATTCCACATACTTGCTAGGATGACCCAACTTTTTCTCACGCCGTTAAGTTGAGAAGACTCAGCACGGATAACTTCATCGCAGACGAAAAAGTTGACTTT',
'AGGGTGTCAACAACATCTGAGGATTTTACCTTGGCGCGACAAACTCACGCGGTTTACTTCTTATCAGGACTGTCGCTGTCGGCCATCTCCCTTATGTAGGTTTGCTCGATTTGAGGATGTGTAACAAGTTTCTCCTAGGAACCTCAACCGGTAGAT',
'CGGTCGGGTACAACCCGCAACTGCGTAATTAATCCGACGGATAACTGCCAGAAGTCTCATAGCGTACAGGAGTTTATCACGACTGAAAATGTGACTTACCAGACACAAGGCTTTGACAAAGGAGTATACGATTAGAAAAACGGTAGCATCGCATTT',
'CTCCAGCACGTGTAGCGACGAGCTTCGGGTAACTCCACGAACTGGTTGGAATATAATGAGGCTAAAACTTCGAGGTCTCCCGCCCGTATGGCATGGAATTGTCAGGTTGAATATTGCGTATACCACGGCCCATTTCCGGAGATTATGATGCACTCC',
'TTCCATTTACGGAGACATATCAATTATTGCTTGGTACGCTAGTCGACGATCATCGAATGGATCTTATACCCGCACCATCAACGGTAGCTATCCCGGACGGGTTACTACAGATCGTACTGCGGACCCAGGTGTATGATAAAAGAACGGGTCCATGCC',
'GATCTCCTGGCCACCCACATACGAAAGGTGTGTCACCGCCTCCACAACGTTTCGATTGGAACTAATTGTAGATTTGTAGAGACTTGCTTAGACGAGTATGGAACTCTGGCACCACTGACGCCGGCTTACTCCTGGCACACAGGTTGATGAACTGGG']
k = 12
t = 25
ans = GS.GibbsSampler(Dna, k, t, 100000)
print('Score:', GS.Score(ans))
print(*ans)

