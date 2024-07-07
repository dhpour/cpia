from .utils import get_static_file_path

class Converter:
    def __init__(self, analyzer, by_force=True):
        self._formal = []
        self._informal = []
        self._analyzer = analyzer
        self._by_force = by_force

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
                return '', rule, ''
            else:
                res0 = self._breakInflectionLine(rule)
                res = self._f2i(res0, False)
                return res
        elif to_register == 'formal':
            if '+رسمی' in rule:
                return [], rule, []
            else:
                return self._i2f(self._breakInflectionLine(rule), force)
    
    def _breakInflectionLine(self, rule):
        debug = False
        word = ''
        right = rule.split("=")[0].split('+')
        left = rule.split("=")[-1].split('+')
        pre = '' if right[0] == right[-1] else right[0]
        pos = right[-1]
        lemma = left[0]
        if debug:
            print('--_breakInflectionLine:')
            print('--result:', [word, pre, pos, lemma] + left[1:])
        return [word, pre, pos, lemma] + left[1:]
    
    def _f2i(self, rule_parts, force):
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

        return '', whole_rule, ''
    
    def _i2f(self, rule_parts, force):
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

    def _ignore_more_then_one(self, rule, length, to_register):
        if length == 1:
            return False
        
        if to_register == 'formal':
            if rule.endswith("+رسمی"):
                return False
            return True
        elif to_register == 'informal':
            if not rule.endswith("+رسمی"):
                return False
            return True

    def convert(self, word, to_register):
        debug = False
        out_words = []
        inflecs = self._analyzer.inflect(word)
        if debug:
            print('-'*10)
        for infl in inflecs:
            pre, new_rule, extra = self._rule_convert(infl, to_register, force=self._by_force)
            if debug:
                print('convert:', 'to_register:', to_register)
                print('-word:', word)
                print('-infl:', infl)
                print('-new_rule:', new_rule)
            if not self._ignore_more_then_one(new_rule, len(inflecs), to_register) or True:
                if debug:
                    print('-_ignore_more_then_one:', False, 'length:', len(inflecs))
                res = self._analyzer.generate(new_rule)
                out_words += res
            else:
                if debug:
                    print('-_ignore_more_then_one:', True, 'length:', len(inflecs))
            if debug:
                print('-'*3)
        return list(set(out_words))