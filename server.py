import socket
import hashlib

HOST = '0.0.0.0'
PORT = 50005

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
  con, cliente = tcp.accept()
  print 'Conextado por', cliente
  while True:
    msg = con.recv(1024)
    if not msg: break
    # txtHash[0] = nomeArquivo.txt ; txtHash[1] = conteudo do arquivo texto; txtHash[2] = conteudo encriptado com sha526
    txtHash = msg.split(";")
    #Encripa o conteudo com sha256 para comparar com o hash recebido. 
    ret = hashlib.sha256(txtHash[1].encode()).hexdigest()
    #se os hashs forem iguais, nao houve manipulacao na mensagem
    if ret == txtHash[2]:
      print "Mensagem decodificada esta segura e sera salva em disco"
      #salva no disco
      arquivo = open( txtHash[0] ,'w')
      #escreve o conteudo
      arquivo.write(txtHash[1])
      arquivo.close()

  print 'Finalizando conexao do cliente', cliente
  con.close()

  