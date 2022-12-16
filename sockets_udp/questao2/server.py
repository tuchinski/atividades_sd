import hashlib
import json
import socket
import logging
import os
from datetime import datetime
import threading

DIRETORIO_PADRAO = 'arqs_server/'

def main():
    if not os.path.isdir('logs'):
        os.mkdir('logs')
    logging.basicConfig(filename=f'logs/{datetime.now().strftime("%d-%m-%Y-%H:%M:%S")}.log',
                        format='%(levelname)s - %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)

    with open('config.json', 'r') as arq_confs:
        confs = json.loads(arq_confs.read())
        
    logging.info("Iniciando servidor")
    ip = "127.0.0.1"
    porta = confs['serverport']
    tamanho_buffer = 1024

    logging.info("Servidor UDP Iniciado")
    # Criando o socket UDP
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as sock:
        sock.bind((ip, porta))

        while True:
            mensagem_recebida, endereco = sock.recvfrom(tamanho_buffer)

            tamanho_nome_arquivo = mensagem_recebida[0]

            _byte_fim_tam_nome_arq = tamanho_nome_arquivo + 1
            nome_arquivo = mensagem_recebida[1:_byte_fim_tam_nome_arq].decode('utf-8')

            _byte_fim_tamanho_arquivo = _byte_fim_tam_nome_arq + 5
            _tamanho_arquivo_bytes = mensagem_recebida[_byte_fim_tam_nome_arq: _byte_fim_tamanho_arquivo]
            tam_arquivo = int.from_bytes(_tamanho_arquivo_bytes, 'big')

            logging.info(f"Recebendo arquivo {nome_arquivo} de {endereco}")
            logging.info(f"Tamanho do arquivo: {tam_arquivo} bytes")

            bytes_arquivo = b''
            if tam_arquivo + _byte_fim_tamanho_arquivo > 1024 - _byte_fim_tamanho_arquivo:
                # Se entrou aqui, tem mais coisa do arquivo pra vir ainda
                bytes_arquivo += mensagem_recebida[_byte_fim_tamanho_arquivo:]
                mensagem_recebida, endereco = sock.recvfrom(tamanho_buffer)
                tam_atual_arquivo = len(bytes_arquivo)
                num_pacote = 2

                while tam_atual_arquivo + 1024 < tam_arquivo:
                    bytes_arquivo += mensagem_recebida
                    tam_atual_arquivo = len(bytes_arquivo)
                    mensagem_recebida, endereco = sock.recvfrom(tamanho_buffer)
                    num_pacote += 1
                    # print(f'recebendo pacote {num_pacote}')
                _byte_fim_tamanho_arquivo = 0

            bytes_faltantes_arquivo = tam_arquivo - len(bytes_arquivo)

            # termina de preencher os bytes do arquivo
            index_final_dados_arquivo = _byte_fim_tamanho_arquivo + bytes_faltantes_arquivo
            bytes_arquivo += mensagem_recebida[_byte_fim_tamanho_arquivo:index_final_dados_arquivo]

            with open(DIRETORIO_PADRAO + nome_arquivo, 'wb') as arquivo:
                arquivo.write(bytes_arquivo)
            logging.info(f'Arquivo {nome_arquivo} gravado em disco')

            # Verifica se os bytes com o tamanho checksum ta no mesmo pacote, ou tem que buscar
            if 1024 - index_final_dados_arquivo < 5:
                _bytes_tamanho_md5 = mensagem_recebida[index_final_dados_arquivo:]
                mensagem_recebida, endereco = sock.recvfrom(tamanho_buffer)

                _index_final_tam_md5 = 5 - len(_bytes_tamanho_md5)
                _bytes_tamanho_md5 += mensagem_recebida[0:_index_final_tam_md5]
                tamanho_md5 = int.from_bytes(_bytes_tamanho_md5, 'big')

                bytes_md5 = mensagem_recebida[_index_final_tam_md5: tamanho_md5]

            else:
                _index_final_tam_md5 = index_final_dados_arquivo + 5
                _bytes_tamanho_md5 = mensagem_recebida[index_final_dados_arquivo:_index_final_tam_md5]
                tamanho_md5 = int.from_bytes(_bytes_tamanho_md5, 'big')

            md5 = mensagem_recebida[_index_final_tam_md5:]
            # Verifica se o checksum ta no msm pacote ou tem que buscar ainda
            if 1024 - index_final_dados_arquivo < tamanho_md5:
                mensagem_recebida, endereco = sock.recvfrom(tamanho_buffer)

                md5 += mensagem_recebida[0:tamanho_md5 - len(md5)]

            md5_arquivo_server = hashlib.md5(bytes_arquivo)

            if md5_arquivo_server.digest() == md5:
                logging.info(f"Check md5 arquivo {nome_arquivo} ok!")
            else:
                logging.error(f"Erro no chack md5 do arquivo {nome_arquivo}")


if __name__ == '__main__':
    main()
