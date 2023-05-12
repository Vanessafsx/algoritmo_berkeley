# Código do servidor

import socket
import time

# Endereço IP e porta do servidor
IP = "127.0.0.1"
PORT = 1234

# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))

# Define o tempo padrão do servidor como 0
server_time = 0

# Função que atualiza o tempo do servidor com o tempo médio dos clientes
def update_server_time(client_time):
    global server_time
    server_time = time.time() + (client_time - time.time()) / 2

# Aguarda por conexões de clientes
sock.listen(1)
print("Servidor iniciado na porta", PORT)
while True:
    conn, addr = sock.accept()
    print("Conectado por", addr)

    # Recebe o tempo do cliente
    client_time = float(conn.recv(1024).decode())
    print("Tempo recebido do cliente:", client_time)

    # Atualiza o tempo do servidor com o tempo médio dos clientes
    update_server_time(client_time)

    # Envia o tempo do servidor de volta para o cliente
    conn.send(str(server_time).encode())

    # Fecha a conexão com o cliente
    conn.close()