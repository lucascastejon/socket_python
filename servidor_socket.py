import socket

HOST = '192.168.0.28'     # Endereco IP do Servidor
PORT = 8080            # Porta que o Servidor esta
tcp  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    print "Aguardando cliente.."
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg       = con.recv(1024) # recebe a mensagem
        msg_send  = con.send(msg)	 # envia a mensagem
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()

print "Servidor Finalizado"