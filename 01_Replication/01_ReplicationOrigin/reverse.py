def main():
	Reverse("ATAG")
	Complement("ATGC")

def Complement(Pattern):
	result = ""
	for num in range(0,len(Pattern)):
		if (Pattern[num] == 'A'):
			result+='T'
		elif (Pattern[num] == 'T'):
			result+='A'
		elif (Pattern[num] == 'G'):
			result+='C'
		elif (Pattern[num] == 'C'):
			result+='G'
	print(result)

def Reverse(Pattern):
	result=""    
	for num in range(len(Pattern),0,-1):
		result+=Pattern[num-1]
	print(result)

if __name__ == "__main__":
    main()
