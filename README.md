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
## Alternative FSTs informal words
These are FSTs designed for covering out-of-vocabulary informal/noisy words and are explained in The OOV `Identification of Informal Persian words`: `docs/informal-oov.pdf`
