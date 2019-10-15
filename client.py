import socket 
import hashlib



HOST = '127.0.0.1'
PORT = 50005


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X \n'
msg = raw_input()
while msg <> '\x18':
  # txtHash[0] = nomeArquivo.txt ; txtHash[1] = conteudo do arquivo texto; txtHash[2] = conteudo encriptado com sha526
  txtHash = msg.split(";")
  # retorna em sha256
  ret = hashlib.sha256(txtHash[1].encode()).hexdigest()
  #concatena o retorno
  msg = msg + ";" + ret
  tcp.send(msg)
  msg = raw_input()
tcp.close