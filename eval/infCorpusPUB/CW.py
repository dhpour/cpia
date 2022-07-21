import sys
import codecs

def numOfWords(file):
    str = codecs.open(file, 'r', encoding='utf-8').read()
    lst = str.strip().split(' ')
    #print(lst)
    print(len(lst))
    test = input('\n')

if __name__ == "__main__":
    numOfWords(sys.argv[1])
#numOfWords('6.txt')
