from fst_lookup import FST
from .utils import get_static_file_path
import re
import os
from cpia.converter import Converter

class Detail:
    def __init__(self):
        print(os.getcwd())

class FarsiAnalyzer:
    def __init__(self, fst_type='standard'):

        fst_path = get_static_file_path(fst_type+".fst", "fsts")
        gen_fst_path = get_static_file_path("generation.fst", "fsts")
        
        self._fst = FST.from_file(fst_path)
        self._gen_fst = FST.from_file(gen_fst_path, labels="invert")

        self._parts_help = self.__load_parts_info(get_static_file_path('rule-parts.txt', "streats"))

    def __load_parts_info(self, file):
        """loads data of parts and their meanings of inflection rules"""
        parts = {}
        for line in open(file, encoding='utf-8'):
            part = line.split("\t")[0].strip()
            desc = line.split("\t")[1].strip()
            parts[part] = desc
        return parts
    
    def __monkey_patch_out(self, inflection):

        pattern = r'\+?رسمی$'
        repl = '+رسمی'
        pattern2 = '@.*?@'
        repl2 = ''
        pattern3 = chr(8204)+"+"
        repl3 = chr(8204)

        #inflection = inflection.replace(">", "").replace("<", "").replace("استاندارد:", "")
        inflection = re.sub(pattern, repl, inflection)
        inflection = re.sub(pattern2, repl2, inflection)
        inflection = re.sub(pattern3, repl3, inflection)
        return inflection

    def lemmatize(self, infl):

        if '=' not in infl:
            infl = '=' + infl
        pos = infl.split("=")[0].split("+")[-1]
        lemma = infl.split("=")[1].split("+")[0]
        if lemma == 'را':
            pos = 'عمفعولی'
      
        out = {"lemma": lemma, "pos": pos}
        out['register'] = "رسمی" if infl.endswith("+رسمی") else "غیررسمی"

        if pos in self._parts_help.keys():
            out["long_pos"] = self._parts_help[pos]
        return out 

    def inflect(self, word):
        return list(set([self.__monkey_patch_out(x[0]) for x in list(self._fst.analyze(word))]))

    def generate(self, inflection):
        return list(set([self.__monkey_patch_out(x) for x in list(self._gen_fst.generate(inflection))]))
    
    def show_help(self):
        txt = ''
        for k in self._parts_help.keys():
            txt += "🔹  " + k + " 👈 " + self._parts_help[k] + "\n"
        return txt
