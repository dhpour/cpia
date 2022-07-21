import sys
import codecs

def numOfWords(file):
	num = 0
	index = input('which column? ')
	for line in codecs.open(file, 'r', encoding='utf-8'):
		num += int(line.strip().split("\t")[index])
    
	print(num)
	test = input('\n')

if __name__ == "__main__":
	numOfWords(sys.argv[1])
        #numOfWords('diary/mahsa93-1part(156)-lex.txt')
