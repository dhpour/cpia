import socket

# cmd : flookup -S -A 127.0.0.1 ../1standard.fst
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def analyze(word):
	sock.sendto(bytes(word, "utf-8"), ("127.0.0.1", 6062))
	data, addr = sock.recvfrom(6062)
	return str(data, encoding="utf-8")