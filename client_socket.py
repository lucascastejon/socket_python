import socket

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 3030            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print 'Para sair use CTRL+X\n'

print "Digite sua mensagem: "
msg = raw_input()
# msg = "820259008407AAA00000010103950560800000009F1A0200769C01009F3704AFFB4A7A9F2701809F360200059F10200FA501A20800580000000000000000000F0000000000000000000000000000009F26084218EE98008AC74A"

while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()

print "Cliente Finalizado"