import os
import socket
from time import sleep
import hashlib
import json

# Formato protocolo
# 1 byte - Tamanho nome arquivo
# 1 ~ 255 bytes - nome arquivo
# 5 bytes - tamanho arquivo
# 1 ~ 2^32 bytes - arquivo


with open('config.json', 'r') as arq_confs:
    confs = json.loads(arq_confs.read())


UDP_IP = "127.0.0.1"
UDP_PORT = confs['serverport']
DIRETORIO_PADRAO = 'arqs_cliente/'

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)


sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

nome_arquivo = input("DIGITE O NOME DO ARQUIVO:")

nome_arquivo_completo = DIRETORIO_PADRAO + nome_arquivo
with open(nome_arquivo_completo, 'rb') as arq_binario:
    tamanho_arquivo = os.stat(nome_arquivo_completo).st_size
    tamanho_nome_arquivo = len(nome_arquivo)

    # Criando pacote de envio
    pacote_envio = b''
    pacote_envio += tamanho_nome_arquivo.to_bytes(1, 'big')  # add tamanho do nome do arq.
    pacote_envio += nome_arquivo.encode('utf-8')  # Add nome arquivo

    pacote_envio += tamanho_arquivo.to_bytes(5, 'big')

    bytes_arquivo_lido = arq_binario.read()
    pacote_envio += bytes_arquivo_lido

    md5 = hashlib.md5(bytes_arquivo_lido)
    bytes_md5 = md5.digest()
    tam_md5 = len(bytes_md5)
    print('tam_md5', tam_md5)
    print(md5.digest())

    # Add o md5 no pacote de envio
    pacote_envio += tam_md5.to_bytes(5, 'big') + bytes_md5

    # sock.sendto(pacote_envio, (UDP_IP, UDP_PORT))

    start = 0
    end = 1024

    count = 0

    while True:
        count += 1
        print(f'Enviando Pacote {count}')
        sock.sendto(pacote_envio[start:end], (UDP_IP, UDP_PORT))
        if tamanho_arquivo/1024 > 1000:
            sleep(0.01)
        start = end
        end += 1024
        if start >= len(pacote_envio):
            break



# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
