# Contemporary Persian Inflectional Analyzer
CPIA is a multi-FST inflectional analyzer for both informal and formal Persian. FSTs rules are compiled by [Foma](https://fomafst.github.io/).

## Test
For checking the analyzer you can check both its [Online Tool](http://infarsi.herokuapp.com/) or
its [Telegram Bot](https://t.me/infarsi_bot). Also you can clone this repo or `app` folder and run the app by
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
## Persian word structure; informal and formal
Comprehensive structure of words specially informal words are explained in the `Contemporary Persian Inflectional Analyzer` paper in full detail: `docs/informal-analyzer.pdf
### Citation
```
@ARTICLE{Heidarpour2021, 
  title = {Contemporary Persian Inflectional Analyzer}, 
  author = {Heidarpour, Davood and S.Sebt, Elham and Bi Jen Khan, Mahmoud and Salehi, Mostafa and Veisi, Hadi and },  
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
How the rules of words are developed to make FSTs are explained in `Thesis`: `docs/thesis.pdf`
### Citation
```
@mastersthesis{heidarpour2018,
  title={An inflectional analyzer for contemporary Persian},
  author={Heidarpour, Davood and Salehi, Mostafa and Bijankhan, Mahmoud and Veisi, Hadi},
  year={2018}
} 
```
## Secondary FSTs
These FSTs are designed for covering out-of-vocabulary informal/noisy words and are explained in The OOV `Identification of Informal Persian words`: `docs/informal-oov.pdf`
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
