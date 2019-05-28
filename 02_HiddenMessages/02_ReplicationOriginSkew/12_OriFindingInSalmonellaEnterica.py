import timeit
import sys
sys.path.insert(0, '/Users/tleis/PycharmProjects/BioInformaticsI/02_HiddenMessages/01_ReplicationOrigin')
CF = __import__('11_BetterClumpFinding')
MS = __import__('02_MinimumSkew2')
FW = __import__('11_FrequentWordsWithMismatchesAndReverseComplements')

def runit():
	salmonella = open('Salmonella_enterica.txt',  'r')
	Genome = salmonella.readlines()
	# remove the header line
	Genome = Genome[1:-1]
	# strip off the newline character
	Genome = "".join(map(str.strip, Genome))
	L = 500
	k = 9
	t = 3
	start_time = timeit.default_timer()

	print('Minimum Skew: ', MS.MinimumSkew(Genome))

	# define a window around the minimum skew
	window = Genome[3764357:3765357]
	fw = FW.FrequentWordsWithMismatchesAndReverseComplements(window, k, 1)
	print('Looking within a window of length: ', len(window))
	print('Frequent Words Within ', len(window) , ' bp of estimated ori:', len(fw))
	print(*fw)
	# to the right of minimum skew:	CCAGGATCC	CCCGGATCC	CCGGATCCG	CGGATCCGG	GGATCCGGG	GGATCCTGG
	# to the left of minimum skew: 16 k-mers ( 1 mismatch ); 4 k-mers (0 mismatch)
#	nineMers = CF.BetterClumpFinding(Genome, k, L, t)
#	print('9-mers', len(nineMers))
	# 1359 9-mers found
	#print(*BetterClumpFinding(Genome,k,L,t), sep = ' ')
	print('Execution time:', timeit.default_timer() - start_time)
runit()