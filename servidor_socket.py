import socket

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 3030            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    print "Aguardando cliente.."
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()
print "Finalizado"