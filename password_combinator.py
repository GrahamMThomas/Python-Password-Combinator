import os
import sys, argparse

def main():

	#Parser
	parser = argparse.ArgumentParser()
	parser.add_argument('--word', action='store', dest='word',type=str, help='word to scramble')
	parser.add_argument('--file', action='store', dest='file',type=str, help='file destination')
	parser.add_argument('--num', action='store', dest='digits',type=str, help='digits to add')

	args = parser.parse_args()
	#End Parser


	try:
		word = args.word
		digitsToAdd = int(args.digits)
	except:
		print "usage: --word <testWord> --file <textFileName> --num #"
		exit(0)
	defaultNumber = ''
	count = 0
	try:
		f = open(args.file, 'w')
	except:
		print "usage: --word <testWord> --file <textFileName> --num #"
		exit(0)
	#Create a string based on the amount of
	#digits the user wants to add.
	#ex. 3 -> '999'
	for j in range(0, digitsToAdd):
		defaultNumber += '9'
	
	#Current iteration number
	numberI = 0;
	
	#How many different combos the program will generate
	numberOfReps = 2**len(word)
	
	print "This generate %d password combinations" % numberOfReps
	

	for i in range(0, numberOfReps):
		
		#Format the current iteration to binary ex. 6 = 0110
		#Note: The binary string is set to be as long as the word
		binaryNum = ('{0:0%db}' % (len(word))).format(numberI)
		wordTemp = ''

		#Run through the length of the word and
		#build a changed word based on the binary 
		#interpretation for the current iteration
		for x in range(0,len(word)):
			if binaryNum[x] == "1":
				wordTemp += word[x].upper()
			else:
				wordTemp += word[x]
		print >> f, wordTemp
		count += 1
	
		#Most users have a number combination
		#at the end of their passwords this allows
		#you to add number iterations at the end of
		#each password change
		if defaultNumber != '':
			for num in xrange(0,int(defaultNumber)+1):
				print >> f, wordTemp + str(num)
				count += 1	
	

		numberI += 1
	print "Generated %d passwords" % count

if __name__ == '__main__':
	main()
