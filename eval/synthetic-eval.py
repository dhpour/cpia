formal = []
informal = []
for line in open("2-inflected.txt", 'r', encoding='utf-8'):
    if 'FN' not in line and 'FP' not in line:
        extra = 0
        if "ف.م.ا=" in line or "ف.م.ن.م=" in line or "ف.ح.ا=" in line:
            extra = 1
        if "+رسمی" in line:
            temp = line.count("+") - 1 + extra
            formal.append(temp)
        else:
            temp2 = line.count("+") + extra
            informal.append(temp2)


formalZeroLess = [x for x in formal if x!= 0]
informalZeroLess = [x for x in informal if x != 0]

print("formal sum:", sum(formal), "/ len:", len(formal), "=", sum(formal)/len(formal))
print("informal sum:", sum(informal), "/ len:", len(informal), "=", sum(informal)/len(informal))
print("formalZeroLess sum:", sum(formalZeroLess), "/ len:", len(formalZeroLess), "=", sum(formalZeroLess)/len(formalZeroLess))
print("informalZeroLess sum:", sum(informalZeroLess), "/ len:", len(informalZeroLess), "=", sum(informalZeroLess)/len(informalZeroLess))


#formal sum: 238 / len: 857 = 0.2777129521586931
#informal sum: 197 / len: 206 = 0.9563106796116505
#formalZeroLess sum: 238 / len: 198 = 1.202020202020202
#informalZeroLess sum: 197 / len: 144 = 1.3680555555555556
######################################
#formal sum: 1275 / len: 2174 = 0.5864765409383624
#informal sum: 2294 / len: 1531 = 1.4983670803396474
#formalZeroLess sum: 1275 / len: 1074 = 1.187150837988827
#informalZeroLess sum: 2294 / len: 1480 = 1.55