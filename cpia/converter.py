from .utils import get_static_file_path

class Converter:
    def __init__(self):
        self._formal = []
        self._informal = []

        for line in open(get_static_file_path("convertableWords.txt", "streats"), encoding='utf-8'):
            if line.strip() != '':
                #print(parts)
                parts = line.strip().split(" ")
                self._informal.append(parts[0])
                self._formal.append(parts[1])
        
        self._stem_formal = []
        self._stem_informal = []

        for line in open(get_static_file_path("convertableStems.txt", "streats"), encoding='utf-8'):
            if line.strip() != '':
                #print(parts)
                parts = line.strip().split(" ")
                self._stem_informal.append(parts[0])
                self._stem_formal.append(parts[1])

    def _rule_convert(self, rule, to_register, force=False):
        if to_register == 'informal':
            if '+رسمی' not in rule:
                return rule
            else:
                return self.f2i(self._breakInflectionLine(rule), force)
        elif to_register == 'formal':
            if '+رسمی' in rule:
                return [], rule, []
            else:
                return self.i2f(self._breakInflectionLine(rule), force)
    
    def _breakInflectionLine(self, rule):
        word = ''
        right = rule.split("=")[0].split('+')
        left = rule.split("=")[-1].split('+')
        pre = '' if right[0] == right[-1] else right[0]
        pos = right[-1]
        lemma = left[0]
        return [word, pre, pos, lemma] + left[1:]
    
    def f2i(self, rule_parts, force):
        register_changed = False
        lemma = rule_parts[3]
        lemma_index = -1
        
        try:
            lemma_index = self._formal.index(lemma)
        except ValueError as e:
            pass
        
        if lemma_index != -1:
            register_changed = True
            lemma = self._informal[lemma_index]
            rule_parts[3] = self._informal[lemma_index]
        
        for i, stem in enumerate(rule_parts[4:]):
            stem_index = -1
            try:
                stem_index = self._stem_formal.index(stem)
            except ValueError as e:
                pass
            
            if stem_index != -1:
                register_changed = True
                new_stem = self._stem_informal[stem_index]
                if self._stem_informal[stem_index] == '0':
                    rule_parts[i+4] = ''
                else:
                    rule_parts[i+4] = self._stem_informal[stem_index]
                
        
        if register_changed or force:
            del rule_parts[-1]

        right_hand = (' ').join(rule_parts[(1 if rule_parts[1] != '' else 2):3]).replace(' ', '+')
        left_hand = [x for x in rule_parts[3:] if x != '']
        whole_rule = right_hand + '=' + ('+').join(left_hand)

        return whole_rule
    
    def i2f(self, rule_parts, force):
        register_changed = False
        lemma = rule_parts[3]
        lemma_index = -1
        extra = []
        pre = []
        try:
            lemma_index = self._informal.index(lemma)
        except ValueError as e:
            pass
        
        if lemma_index != -1:
            register_changed = True
            lemma = self._formal[lemma_index]
            rule_parts[3] = self._formal[lemma_index]
        
        pre_index = -1
        try:
            pre_index = self._stem_informal.index(rule_parts[1])
        except ValueError as e:
            pass

        if pre_index != -1:
            if self._stem_formal[pre_index] == '0':
                rule_parts[1] = ''
                   
            if self._stem_informal[pre_index] == 'پا':
                if rule_parts[3] == 'شد':
                    pre.append("بلند")
                elif rule_parts[3] == 'شو':
                    pre.append("بلند")

        for i, stem in enumerate(rule_parts[4:]):
            stem_index = -1
            try:
                stem_index = self._stem_informal.index(stem)
            except ValueError as e:
                pass
            
            if stem_index != -1:
                register_changed = True
                new_stem = self._stem_formal[stem_index]
                if self._stem_formal[stem_index] == '0':
                    rule_parts[i+4] = ''
                    if self._stem_informal[stem_index] == 'عطف':
                        extra.append('و')
                    elif self._stem_informal[stem_index] == 'معرفه':
                        pre.append('آن')
                    elif self._stem_informal[stem_index] in ["تاکید"]:
                        pass
                    else:
                        extra.append(self._stem_informal[stem_index])
                else:
                    rule_parts[i+4] = self._stem_formal[stem_index]
        
        if register_changed or force:
            for i, part in enumerate(rule_parts):
                if "ومفعولی" in part:
                    rule_parts[i] = ''
                    object_flag = False
                    if "۱" in part:
                        pre.append("من")
                        object_flag = True
                    if "۲" in part:
                        pre.append("تو")
                        object_flag = True
                    if "۳" in part:
                        pre.append("آن")
                        object_flag = True
                    if "۴" in part:
                        pre.append("ما")
                        object_flag = True
                    if "۵" in part:
                        pre.append("شما")
                        object_flag = True
                    if "۶" in part:
                        pre.append("آنها")
                        object_flag = True
                    
                    if object_flag:
                        pre.append("را")
                        
                if "وفاعلی" in part:
                    rule_parts[i] = ''
                    
            rule_parts.append("رسمی")

        right_hand = rule_parts[(1 if rule_parts[1] != '' else 2):3]
        left_hand = [x for x in rule_parts[3:] if x != '']
        whole_rule = (' ').join(right_hand).replace(' ', '+') + '=' + ('+').join(left_hand)

        return pre, whole_rule, extra
    
