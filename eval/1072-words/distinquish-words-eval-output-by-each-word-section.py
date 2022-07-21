count = 0

lastword = ''
for line in open("C:/Users/dave/Desktop/intp-words-1.txt", 'r', encoding='utf-8'):
    if ("ف." in line or "امری" in line or "التزامی" in line ) and lastword == '':
        count += 1
        lastline = '-'
    else:
        #num = out.write(line)
        pass
    if line.strip() == '':
        lastword = ''
