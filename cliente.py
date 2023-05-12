# Código do cliente

import socket
import time

# Endereço IP e porta do servidor
IP = "127.0.0.1"
PORT = 1234

# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
sock.connect((IP, PORT))

# Obtem o tempo atual do cliente
client_time = time.time()

# Envia o tempo do cliente para o servidor
sock.send(str(client_time).encode())

# Recebe o tempo do servidor de volta
server_time = float(sock.recv(1024).decode())
print("Tempo recebido do servidor:", server_time)

# Calcula a diferença entre o tempo do servidor e do cliente
time_diff = server_time - client_time
print("Diferença de tempo:", time_diff)

# Atualiza o relógio do cliente com a diferença de tempo
new_time = client_time + time_diff
print("Novo tempo do cliente:", new_time)

# Fecha a conexão com o servidor
sock.close()