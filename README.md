Contemporary Persian Inflectional Analyzer  
==========================================
[![PyPI version](https://img.shields.io/badge/pypi-v2024.7.71-blue)](https://pypi.org/project/cpia/)
[![calver YYYY.MM.DD](https://img.shields.io/badge/calver-YYYY.MM.MICRO-22bfda.svg)](http://calver.org/)

Analyze Informal and Formal words of contemporary Persian.

Install
-------
    pip install cpia

Usage
-----
```python
>>> from cpia import FarsiAnalyzer, Converter
>>> farsi = FarsiAnalyzer()

>>> farsi.inflect("کتاب‌هایشان")
['اسمعا=کتاب+جها+وشخصی۶+رسمی']

>>> farsi.inflect("بشینین")
['التزامی=نشین+ش۵', 'امری=نشین+ش۵']

>>> farsi.generate("امری=گو+مفرد+رسمی")
['بگو']

>>> print(farsi.generate('ف.ح.ا=خور+ش۱+ومفعولی۲')[0])
می‌‌خورمت

>>> farsi.lemmatize(farsi.inflect("میچرخوندمش")[0])
{'lemma': 'چرخوند',
 'pos': 'ف.م.ا',
 'register': 'غیررسمی',
 'long_pos': 'فعل ماضی استمراری'}

>>> converter = Converter(farsi)
>>> print(converter.convert("میچرخوندمش", "formal")[0])
می‌چرخاندم

```
For understanding abbreviations used in inflection rules:
```python
>>> farsi.show_help()
🔹  ف.م.ب 👈 فعل ماضی بعید*
🔹  ف.م.ال 👈 فعل ماضی التزامی*
🔹  ف.م.ا.ب 👈 فعل ماضی ابعد*
🔹  ف.آ 👈 فعل مستقبل (آینده)*
🔹  اسمعام 👈 اسم عام
          ...
```
Other than `standard` fst for inflection and `generation` fst for generating words from rules, cpia has secondary fsts. The main fst is enough for almost all tasks but the secondary fsts can be used for noisy informal Out-Of-Vocabulary words, they normally can produce a lot of useless inflections. They are only useful for special cases. Use them only if you know what you want.
If you need to use other fsts, just pass their name as argument to the FarsiAnalyzer constructor:
```python
>>> farsi = FarsiAnalyzer("homophone")
```

Fsts
----

| Name                  |           word          |                                                         output |
|----------------------|:-----------------------:|---------------------------------------------------------------:|
| **standard**             |           **برم**           | **<استاندارد:اسمعا=بره+وشخصی۱><br><استاندارد:اسمعا=بر+هم><br><استاندارد:اسمعا=بر+وشخصی۱+رسمی><br><استاندارد:اسمعا=بر+وربطی۱+رسمی><br><استاندارد:اسمعا=برم+رسمی><br><استاندارد:حضاف=بر+وشخصی۱+رسمی><br><استاندارد:التزامی=ر+ش۱><br><استاندارد:امری=رم+مفرد+رسمی>** |

Secondary Fsts
--------------

| Name                  |           word          |                                                         output |
|----------------------|:-----------------------:|---------------------------------------------------------------:|
| **homophone**            | **مسؤول<br>مسئول<br>مسیول** |                                       <**همصدا:اسمعا=مسئول+رسمی>** |
| **phone_change (avaee)**                |          **شیطون**          |                                            **<آوایی:اسمعا=شیطان>** |
| **expressive**           | **چرااااااا** |                                         **<بیانی:اسمعا=چرا+رسمی>** |
| **splitter**             |         **چهاربعدی**        |               **<تقطیع:شماره=چهار+رسمی><br><تقطیع:صفت=بعدی+رسمی>** |

<p align="center">
  <img src="https://github.com/lingwndr/cpia/blob/master/icon.png?raw=true" alt="تحلیلگر تصریفی فارسی معاصر" width="150"/>
</p>

Evaluation
----------

The analyzer is not aware of context but the output should provide all possible inflections for all possible contexts. Eval dataset is in `eval` folder. For 1786 unique words extracted from dataset analyzer produced 3,704 inflections rules. Here are the shortcomings counted based on their occurances.

| register | OOV | OO-Rules | homophone / Ezafeh Const. | stucking words | phone changing | spelling error |
|:--------:|:---:|:--------:|:-------------------------:|:--------------:|:--------------:|:--------------:|
| informal |  40 |     4    |             3             |        3       |        5       |        8       |
|  formal  |  83 |     6    |             0             |        1       |        0       |       17       |

The **`recall`** metric is calculated for all FSTs as below

| register / FST          | standard   | homophone | phone_change | expressive | splitter |
|-------------------------|------------|-----------|--------------|------------|----------|
| informal                | **96.33%** | 96.42%    | 97.3%        | 97.3%      | 97.48%   |
| formal                  | **95.1%**  | 95.1%     | 95.1%        | 95.1%      | 95.1%    |
| combined (Contemporary) | **95.56%** | 95.64%    | 96%          | 96%        | 96.08%   |

OOVs and OO-Rules
-----------------
There is a list of words and inflections in [OOs/extra.txt](https://github.com/lingwndr/cpia/blob/master/app/OOs/extra.txt) that are not included in FSTs. You can directly contribute to this list or report lack of words/rules by online tools and update this list. Both [Online Tool](https://infarsi.herokuapp.com/) and [Telegram Bot](https://t.me/infarsi_bot) have report capability. This list will be used to update FSTs in a proper manner periodically. For contributing directly to this list, please use the following format, and for inflection, use the structure of this analyzer. Note that the third column (the context that the word appears in) is optional.

`فونت[TAB]اسمعام=فونت+رسمی[TAB]فونت قشنگی استفاده کردن`

Persian word structure; informal and formal
--------------------------------------------
Comprehensive structure of words especially informal words are explained in the `Contemporary Persian Inflectional Analyzer` paper in full detail: [`docs/informal-analyzer.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/informal-analyzer.pdf); [paper on the Journal website](https://jipm.irandoc.ac.ir/article-1-4337-en.html%3B)
### Citation
```bibtex
@article{Heidarpour2021, 
  title = {Contemporary Persian Inflectional Analyzer}, 
  author = {Heidarpour, Davood and S.Sebt, Elham and Bi Jen Khan, Mahmoud and Salehi, Mostafa and Veisi, Hadi },  
  volume = {36}, 
  number = {4},  
  URL = {http://jipm.irandoc.ac.ir/article-1-4337-en.html},  
  eprint = {http://jipm.irandoc.ac.ir/article-1-4337-en.pdf},  
  journal = {Iranian Journal of Information Processing and Management},   
  doi = {10.52547/jipm.36.4.945},  
  year = {2021}  
}
```
Fst word rule structure; informal and formal
--------------------------------------------
All the lexicon, morphotactic and morphophonemic rules are in `lexc` folder. These files are used by Foma to compile FSTs.
How the rules of words are developed to make FSTs are explained in `Thesis`: [`docs/thesis.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/thesis.pdf)
### Citation
```bibtex
@mastersthesis{Heidarpour2018,
  title = {An inflectional analyzer for contemporary Persian},
  author = {Heidarpour, Davood and Salehi, Mostafa and Bi Jen Khan, Mahmoud and Veisi, Hadi},
  year = {2018}
} 
```
Secondary Fsts
--------------
These FSTs are designed for covering out-of-vocabulary informal/noisy words and are explained in `Covering Out-of-Vocabulary Words of Informal Persian` paper: [`docs/informal-oov.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/informal-oov.pdf)
### Citation
```bibtex
@incollection{Heidarpour2019, 
  title = {Covering Out-of-Vocabulary Words of Informal Persian}, 
  author = {Heidarpour, Davood and Salehi, Mostafa and Bi Jen Khan, Mahmoud and Veisi, Hadi and Ranjbar, Vahid},  
  booktitle = {5th National Conference on Computational Linguistics},
  URL = {https://neveeseh.com},  
  year = {2019}  
}
```

Fst rules are compiled by [Foma](https://fomafst.github.io/).

License
-------
Licensed under GNU General Public License Version 3 (GPLv3)