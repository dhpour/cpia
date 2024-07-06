from fst_lookup import FST
import re
import os

class Detail:
    def __init__(self):
        print(os.getcwd())

class FarsiAnalyzer:
    def __init__(self, fst_type='standard'):

        fst_path = get_static_file_path(fst_type+".fst")
        gen_fst_path = get_static_file_path("generation.fst")
        
        self.fst = FST.from_file(fst_path)
        self.gen_fst = FST.from_file(gen_fst_path, labels="invert")

    def __monkey_patch_out(self, inflection):

        pattern = r'\+?رسمی$'
        repl = '+رسمی'
        pattern2 = '@.*?@'
        repl2 = ''

        inflection = inflection.replace(">", "").replace("<", "").replace("استاندارد:", "")
        inflection = re.sub(pattern, repl, inflection)
        inflection = re.sub(pattern2, repl2, inflection)
        return inflection

    def lemmatize(self, infl, show_pos=True):

        if '=' not in infl:
            infl = '=' + infl
        pos = infl.split("=")[0]
        stem = infl.split("=")[1].split("+")[0]
        if stem == 'را':
            pos = 'عمفعولی'

        if not show_pos:
            return stem
        
        return stem, pos

    def inflect(self, word):
        return list(set([self.__monkey_patch_out(x[0]) for x in list(self.fst.analyze(word))]))

    def generate(self, inflection):
        return list(set([self.__monkey_patch_out(x) for x in list(self.gen_fst.generate(inflection))]))
    

def get_static_file_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fsts', filename)