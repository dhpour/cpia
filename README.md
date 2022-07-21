# Contemporary Persian Inflectional Analyzer
CPIA is a multi-FST inflectional analyzer for both informal and formal Persian. FSTs rules are compiled by [Foma](https://fomafst.github.io/).

## Test
For checking the analyzer you can check both its [Online tool](http://infarsi.herokuapp.com/) or
its [Telegram Bot](https://t.me/infarsi_bot). Also you can clone this repo or `app` folder and run the app by
```batch
python interfaceGrid.py
```
or run Foma as server:
```batch
flookup -S -A 127.0.0.1 ./1standard.fst
```
then quering it:
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes("پیچونده", "utf-8"), ("127.0.0.1", 6062))
data, addr = sock.recvfrom(6062)
print(str(data, encoding="utf-8")

>>><پیچونده <استاندارد:صمفعولی=پیچونده
```
## Persian word structure; informal and formal
Comprehensive structure of words specially informal words are explained in the `Contemporary Persian Inflectional Analyzer` paper in full detail: `docs/informal-analyzer.pdf
## FST word rule structure; informal and formal
How the rules of words are developed to make FSTs are explained in `Thesis`: `docs/thesis.pdf`
Citation
```
@ARTICLE{Heidarpour2021, 
  author = {Heidarpour, Davood and S.Sebt, Elham and Bi Jen Khan, Mahmoud and Salehi, Mostafa and Veisi, Hadi and },  
  title = {Contemporary Persian Inflectional Analyzer}, 
  volume = {36}, 
  number = {4},  
  abstract ={In recent years, the use of informal writing in Persian has grown significantly due to the increasing expansion of cyberspace and social media and platforms, and the tendency of users to bring the written language closer to colloquial speech. But on the other hand, proper tools to process this language register are not developed very much. One of the tools for low level processing of textual data is an inflectional analyzer. However, such tools are not developed for this register yet. Informal words have their own structures, stems, morphemes and clitics and they also make use of formal structures and units. Moreover, this register also consists of formal words so any analyzer for informal words should have the potential to analyze formal words, too. In this paper, it is tried to cover all inflectional structures of informal Persian language to build an inflectional analyzer. A corpus of most of its known sub-registers is constructed to extract words, morphemes and inflectional rules and morphotactics. A part of this corpus is used for testing the analyzer. After extracting 1786 unique words of the test part, inflectional analyzer f-measure is equal to 97.67%. This tool can be used in computational processing of Persian language and it can also be used in teaching Persian, specifically colloquial Persian to non-Persian learners. },  
  URL = {http://jipm.irandoc.ac.ir/article-1-4337-en.html},  
  eprint = {http://jipm.irandoc.ac.ir/article-1-4337-en.pdf},  
  journal = {Iranian Journal of Information Processing and Management},   
  doi = {10.52547/jipm.36.4.945},  
  year = {2021}  
}
```
## Secondary FSTs
These FSTs are designed for covering out-of-vocabulary informal/noisy words and are explained in The OOV `Identification of Informal Persian words`: `docs/informal-oov.pdf`
