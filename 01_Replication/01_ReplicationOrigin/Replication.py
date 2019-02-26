import sys
import FrequencyMap
import SymbolArray
import PatternCount

def main():
	print("Symbol-Array Imported")
	print("Hi")
	kmer = FrequencyMap.FrequencyMap("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3)
	print(kmer)

	Text = 	"aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga"
	Text = Text.upper()
	count_1 = PatternCount.PatternCount("ATGATCAAG", Text)
	count_2= PatternCount.PatternCount("CTTGATCAT", Text)
	print(count_1+count_2)
	cgcg = PatternCount.PatternCount("TGT", "ACTGTACGATGATGTGTGTCAAAG")
	print("CGCG count:")
	print(cgcg)
	print("Symbol Array Test:")
	SymbolArray.SymbolArray("A", "AAAGGG")

if __name__== "__main__":
	main()
