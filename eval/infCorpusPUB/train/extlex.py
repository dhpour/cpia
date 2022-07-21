zwnj = '\u200c'
space = ' '

with open('lex.txt', 'w', encoding='utf-8') as out:
    for line in open('wLem-72percent-uniq-inf.txt', 'r', encoding='utf-8'):
        nline = line.split('\t')[0].strip().replace(zwnj, '').replace(space, '') + '\n'
        out.write(nline)
