# contemporary-persian-inflectional-analyzer
CPIA is a multi-FST inflectional analyzer for both informal and formal Persian. FSTs rules are designed and compiled by [Foma](https://fomafst.github.io/).

##Test
For checking the anlyzer you can check both its [Online tool](http://infarsi.herokuapp.com/) or
its [Telegram Bot](https://t.me/infarsi_bot). Also you can clone this repo or `app` folder and run the app by
```
python interfaceGrid.py
```
or run Foma as server
```
flookup -S -A 127.0.0.1 ./1standard.fst
```
and quering it
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes("پیچونده", "utf-8"), ("127.0.0.1", 6062))
data, addr = sock.recvfrom(6062)
print(str(data, encoding="utf-8")

>>><پیچونده <استاندارد:صمفعولی=پیچونده
```
