import socket 
import hashlib

# def encrypt_string(hash_string):
#     return hashlib.sha256(hash_string.encode()).hexdigest()


HOST = '127.0.0.1'
PORT = 50001


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X \n'
msg = raw_input()
while msg <> '\x18':
  txtHash = msg.split(";")
  ret = hashlib.sha256(txtHash[1].encode()).hexdigest()
  msg = msg + ";" + ret
  tcp.send(msg)
  msg = raw_input()
tcp.close