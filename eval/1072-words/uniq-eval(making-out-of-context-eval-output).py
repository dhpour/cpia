num = 0
words = {}
outfile = open("C:\\Users\\dave\\Desktop\\uniques.txt", 'w', encoding='utf-8')
data = []
for line in open("C:\\Users\\dave\\Desktop\\intp-words-new4.txt", 'r', encoding='utf-8'):
	num += 1
	if line.strip() != '':
		parts = line.strip().split("\t")
		if len(parts) < 3:
			print(len(parts), num)
			print(line)
			print("---")
		words[(parts[0],parts[1])] = str(words.get((parts[0],parts[1]), '')) + "," + parts[2]

for (word, rule) in words.keys():
	line = word + "\t" + rule + "\t" + words[(word,rule)] + "\n"
	data.append(line)
	n = outfile.write(line)

outfile.close()


#for line in open("C:\\Users\\dave\\Desktop\\uniques.txt", 'r', encoding='utf-8'):
#	data.append(line)


import unif
data2= sorted(data, key=lambda word: [unif.order(c) for c in word])
for line in data2:
        line = line.replace(">\t, ", ">\t")
	nn = outfile.write(line)

outfile.close()
