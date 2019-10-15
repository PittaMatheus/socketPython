import socket

HOST = '0.0.0.0'
PORT = 50001

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

# con, cliente = tcp.accept()
# print 'Concertado por', cliente

# while True:
#     msg = con.recv(1024)
#     if not msg: break
#     print cliente, msg

# print 'Finalizando conexao do cliente', cliente
# con.close()

while True:
  con, cliente = tcp.accept()
  print 'Conextado por', cliente
  while True:
    msg = con.recv(1024)
    if not msg: break
    print cliente, msg
  print 'Finalizando conexao do cliente', cliente
  con.close()

  