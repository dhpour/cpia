def mut(file):
    count = 1
    for line in open(file, 'r', encoding='utf8'):
        if " " in line.split("\t")[0]:
            print(count, end="  ")
            print(line.split("\t")[0].replace(" ", "<>"), "\t\t", line.split("\t")[1])
            count += 1
mut("ref-inf-all.txt")
