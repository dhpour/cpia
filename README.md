<p align="center">
  
# Contemporary Persian Inflectional Analyzer  
  
</p>
<p align="center">
  <img src="https://github.com/lingwndr/cpia/blob/master/icon.png?raw=true" alt="تحلیلگر تصریفی فارسی معاصر" width="150"/>
</p>

CPIA is a multi-FST inflectional analyzer for both informal and formal Persian. FSTs rules are compiled by [Foma](https://fomafst.github.io/).
The main FST is enough for almost all tasks. The Secondary FSTs can be used for noisy informal Out-Of-Vocabulary words, they normally can produce a lot of useless inflections. They are only useful for special cases. Use them only if you know what you want.

### FSTs

| FST                  |           word          |                                                         output |
|----------------------|:-----------------------:|---------------------------------------------------------------:|
| **standard**             |           **برم**           | **<استاندارد:اسمعا=بره+وشخصی۱><br><استاندارد:اسمعا=بر+هم><br><استاندارد:اسمعا=بر+وشخصی۱+رسمی><br><استاندارد:اسمعا=بر+وربطی۱+رسمی><br><استاندارد:اسمعا=برم+رسمی><br><استاندارد:حضاف=بر+وشخصی۱+رسمی><br><استاندارد:التزامی=ر+ش۱><br><استاندارد:امری=رم+مفرد+رسمی>** |

**Secondary FSTs**

| FST                  |           word          |                                                         output |
|----------------------|:-----------------------:|---------------------------------------------------------------:|
| **homophone**            | **مسؤول<br>مسئول<br>مسیول** |                                       <**همصدا:اسمعا=مسئول+رسمی>** |
| **phone_change**                |          **شیطون**          |                                            **<آوایی:اسمعا=شیطان>** |
| **expressive**           | **چرااااااا** |                                         **<بیانی:اسمعا=چرا+رسمی>** |
| **splitter**             |         **چهاربعدی**        |               **<تقطیع:شماره=چهار+رسمی><br><تقطیع:صفت=بعدی+رسمی>** |

## How to check or use FSTs
For testing the analyzer you can check both its [Online Tool](https://infarsi.herokuapp.com/) (all FSTs) or
its [Telegram Bot](https://t.me/infarsi_bot) (only standard FST). You can also clone this repo or `app` folder and run the app by
```batch
python interfaceGrid.py
```
or run Foma as server:
```shell
flookup -S -A 127.0.0.1 ./1standard.fst
```
then quering it:
```python
>>> import socket

>>> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> sock.sendto(bytes("می‌چرخونده", "utf-8"), ("127.0.0.1", 6062))
21
>>> data, addr = sock.recvfrom(6062)
>>> print(str(data, encoding="utf-8"))
می‌چرخونده 	       	<استاندارد:ف.م.ن.م=چرخوند+وربطی۳>
```

## Evaluation

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

## Persian word structure; informal and formal
Comprehensive structure of words especially informal words are explained in the `Contemporary Persian Inflectional Analyzer` paper in full detail: [`docs/informal-analyzer.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/informal-analyzer.pdf)
### Citation
```
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
## FST word rule structure; informal and formal
All the lexicon, morphotactic and morphophonemic rules are in `lexc` folder. These files are used by Foma to compile FSTs.
How the rules of words are developed to make FSTs are explained in `Thesis`: [`docs/thesis.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/thesis.pdf)
### Citation
```
@mastersthesis{Heidarpour2018,
  title={An inflectional analyzer for contemporary Persian},
  author={Heidarpour, Davood and Salehi, Mostafa and Bi Jen Khan, Mahmoud and Veisi, Hadi},
  year={2018}
} 
```
## Secondary FSTs
These FSTs are designed for covering out-of-vocabulary informal/noisy words and are explained in `Covering Out-of-Vocabulary Words of Informal Persian` paper: [`docs/informal-oov.pdf`](https://github.com/lingwndr/cpia/blob/master/docs/informal-oov.pdf)
### Citation
```
@incollection{Heidarpour2019, 
  title = {Covering Out-of-Vocabulary Words of Informal Persian}, 
  author = {Heidarpour, Davood and Salehi, Mostafa and Bi Jen Khan, Mahmoud and Veisi, Hadi and Ranjbar, Vahid},  
  booktitle={5th National Conference on Computational Linguistics},
  URL = {https://neveeseh.com},  
  year = {2019}  
}
```
