def extLemma(file):
    lems = {}
    for line in open(file, 'r', encoding='utf8'):
        token = line.split("\t")[4].strip()
        lems[token] = lems.get(token, 0) + 1
    with open("-lem-lex-"+file, 'w', encoding='utf8') as out:
        for key, item in lems.items():
            line = key + "\t" + str(item) + "\n"
            out.write(line)
extLemma("wLem-1stPase-all-inform-lex.txt")
