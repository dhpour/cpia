import sys
import codecs

def numOfWords(file):
	num = 0
	lemmas = []
	index = input('which column? ')
	for line in codecs.open(file, 'r', encoding='utf-8'):
		elem =line.strip().split("\t")
		if len(elem) <= index:
			lemmas.append(' ')
		else:
			lemmas.append(line.strip().split("\t")[index])
    
	print(len(set(lemmas)))
	test = input('\n')

if __name__ == "__main__":
	numOfWords(sys.argv[1])
        #numOfWords('diary/mahsa93-1part(156)-lex.txt')
