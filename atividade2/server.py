import json
from datetime import datetime
import socket
import os
import threading
from time import sleep
import logging

diretorio_padrao = "arquivos/"


def remove_bad_characters(str_entrada):
    """
    Remove os caracteres "\n" e "\t"
    """
    return str_entrada.replace("\n", '').replace("\t", "")


def monta_response_inicial(ident_comando):
    response_inicial = b""

    # Add Message Type = 2
    response_inicial += int(2).to_bytes(1, 'big')

    # Add Command Ident.
    response_inicial += int(ident_comando).to_bytes(1, 'big')

    return response_inicial


def main():
    print("Iniciando o Server Questão 2")
    if not os.path.isdir('logs'):
        os.mkdir('logs')
    logging.basicConfig(filename=f'logs/{datetime.now().strftime("%d-%m-%Y-%H:%M:%S")}.log', format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)

    logging.debug("Iniciando server")

    # Lendo as confs
    with open('config.json', 'r') as file:
        confs = json.loads(file.read())

    host = confs['host']
    porta = confs['porta']

    # Iniciando o servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, porta))
        s.listen()
        logging.debug('Server Iniciado')
        print("Server Iniciado!")

        while True:
            conn, addr = s.accept()
            print("Nova conexão no servidor: ", addr)
            logging.info(f"Nova conexão no servidor: {addr}")
            threading.Thread(target=resolve_mensagem_recebida, args=(conn, addr)).start()


def newaddfile(conexao: socket.socket):
    logging.info("Iniciando ADDFILE")
    print("[LOG] - Retornando ADDFILE")

    tam_nome_arq_byte = conexao.recv(1)
    tam_nome_arquivo = int.from_bytes(tam_nome_arq_byte, 'big')

    nome_arq_bytes = conexao.recv(tam_nome_arquivo)

    nome_arquivo_completo = diretorio_padrao + nome_arq_bytes.decode('utf-8')
    if len(nome_arq_bytes) == tam_nome_arquivo:
        response = monta_response_inicial(1)
        tam_arquivo = int.from_bytes(conexao.recv(4), 'big')

        print(f"[LOG] - Recebendo arquivo {nome_arq_bytes.decode('utf-8')}")
        with open(nome_arquivo_completo, 'wb') as arq_binario:
            for _ in range(0, tam_arquivo):
                byte_recebido = conexao.recv(1)
                if not byte_recebido:
                    break
                arq_binario.write(byte_recebido)
        logging.info(f"[LOG] - Arquivo {nome_arq_bytes.decode('utf-8')} recebido")
        print(f"[LOG] - Arquivo {nome_arq_bytes.decode('utf-8')} recebido")


def newdeletefile(conexao: socket.socket):
    logging.info("Iniciando DELETE")
    print("[LOG] - Retornando DELETE")
    tam_nome_arq_byte = conexao.recv(1)
    tam_nome_arquivo = int.from_bytes(tam_nome_arq_byte, 'big')

    nome_arq = conexao.recv(tam_nome_arquivo).decode('utf-8')

    logging.info(f"Removendo arquivo {nome_arq}")
    print(f"[LOG] - Removendo arquivo {nome_arq}")
    if len(nome_arq) == tam_nome_arquivo:
        response = monta_response_inicial(2)

        nome_completo_arq = diretorio_padrao + nome_arq

        if os.path.exists(nome_completo_arq):
            os.remove(nome_completo_arq)
            response += int(1).to_bytes(1, 'big')
            print(f"[LOG] - Arquivo {nome_arq} removido")
            logging.info(f"Arquivo {nome_arq} removido")
        else:
            response += int(2).to_bytes(1, 'big')
            logging.error(f'Arquivo {nome_completo_arq} não encontrado')
            print(f'[ERROR] - Arquivo {nome_completo_arq} não encontrado')
        conexao.sendall(response)


def newgetfileslist(conexao: socket.socket):
    logging.info('Iniciando GETFILESLIST')
    print("[LOG] - Retornando GETFILESLIST")

    response = monta_response_inicial(3)
    # try:
    # Buscando os arquivos da pasta padrão e colocando em um array
    arquivos_disponiveis = []
    for _, _, arqs in os.walk(diretorio_padrao):
        arquivos_disponiveis += arqs

    # Colocando no response o byte de status code como sucesso
    response += int(1).to_bytes(1, 'big')

    # Colocando no response a qtde de arquivos
    qtde_arquivos = len(arquivos_disponiveis)
    response += qtde_arquivos.to_bytes(2, 'big')
    conexao.sendall(response)
    sleep(0.01)

    # Enviando os arquivos
    for nome_arquivo in arquivos_disponiveis:
        tamanho_nome = len(nome_arquivo)
        response_arquivo = tamanho_nome.to_bytes(1, 'big')
        response_arquivo += nome_arquivo.encode()
        conexao.sendall(response_arquivo)
        sleep(0.01)


    # except Exception as e:
    #     print("[ERROR] - ", e)
    #     response_erro = monta_response_inicial(3)
    #     response_erro += int(2).to_bytes(1, 'big')
    #     conexao.sendall(response_erro)

def newgetfile(conexao: socket.socket):
    logging.info('Iniciando GETFILE')
    print("[LOG] - Retornando GETFILE")

    tam_nome_arq_byte = conexao.recv(1)
    tam_nome_arquivo = int.from_bytes(tam_nome_arq_byte, 'big')

    nome_arq = conexao.recv(tam_nome_arquivo).decode('utf-8')

   
    if len(nome_arq) == tam_nome_arquivo:
        response = monta_response_inicial(4)

        # Colocando no response o byte de status code como sucesso
        response += int(1).to_bytes(1, 'big')

        nome_completo_arq = diretorio_padrao + nome_arq

        try:
            with open(nome_completo_arq, 'rb') as file:
                logging.info(f"Enviando arquivo {nome_arq}")
                print(f"[LOG] - Enviando arquivo {nome_arq}")
                byte_lido = file.read(1)
                tam_arquivo_lido = os.stat(nome_completo_arq).st_size
                response += tam_arquivo_lido.to_bytes(4, 'big')
                conexao.sendall(response)
                sleep(0.01)
                while(byte_lido):
                    conexao.send(byte_lido)
                    byte_lido = file.read(1)
                logging.info(f'Arquivo {nome_arq} enviado')
                print(f'[LOG] - Arquivo {nome_arq} enviado')
        except FileNotFoundError as error:
            logging.error(f"Arquivo {nome_arq} não encontrado")
            print(f"Arquivo {nome_arq} não encontrado")
            response = response[:2] + int(2).to_bytes(1, "big") # define que deu erro ao enviar
            conexao.sendall(response)
            


def resolve_mensagem_recebida(conexao: socket.socket, addr):

    while True:
        mensagem = conexao.recv(2)
        if len(mensagem) == 0:
            break
        tipo_mensagem = mensagem[0]
        identificador_comando = mensagem[1]

        if identificador_comando == 1:
            newaddfile(conexao)
        elif identificador_comando == 2:
            newdeletefile(conexao)
        elif identificador_comando == 3:
            newgetfileslist(conexao)
        elif identificador_comando == 4:
            newgetfile(conexao)


if __name__ == '__main__':
    main()
