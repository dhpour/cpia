def extrLemmas(file):
    tmp = ""
    tmp2 = ""
    count = 0
    count2 = ""
    copulaCount = 0
    outFile = open("wLem-"+file, 'w', encoding="UTF-8")
    for line in open(file, 'r', encoding="UTF-8"):
        morphs = line.strip().split("\t")[1]
        for morph in morphs.split("+"):
            if  morph != "ب" and morph != "بی" and morph != "ن" and morph !="می":
                if tmp != morph:
                    count += 1
                    tmp2 = morph
                    count2 = str(count)
                else:
                    #tmp2 = "\""
                    count2 = ""
                if "است" in morphs:
                    copulaCount += 1
                    #print(copulaCount, morphs)
                #print(count, morph)
                #nLine = line.strip() + "\t" + tmp2 + "\t" + count2 + "\n"
                nLine = line.strip().split("\t")[0] + "\t" + line.strip().split("\t")[1] + "\t" +  line.strip().split("\t")[2] + "\t" + line.strip().split("\t")[3] + "\t" + tmp2 + "\n"
                outFile.write(nLine)
                tmp = morph
                break
    print(file, "has\t", copulaCount)
    outFile.close()

extrLemmas('1stPase-all-inform-lex.txt')

'''
files = ['ref-inf-all.txt']
for file in files:
    extrLemmas(file)
'''
