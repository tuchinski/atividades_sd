"""
Descrição: Cliente que realiza requisições para o servidor
Autores: Ilzimara e Leonardo
Data de criação: 07/09/2022
"""
import os
import socket
import json

diretorio_padrao = "arqs-cliente/"


def main():
    # Lendo as confs
    with open('config.json', 'r') as file:
        confs = json.loads(file.read())

    host = confs['host']
    porta = confs['porta']
    dir_padrao = "arqs-cliente/"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, porta))
        print("Comandos: ")
        print("-> ADDFILE: adiciona um arquivo novo")
        print("-> DELETE: remove um arquivo existente")
        print("-> GETFILESLIST: retorna uma lista com o nome dos arquivos.")
        print("-> GETFILE: faz download de um arquivo.")
        print("-> EXIT: finaliza a conexão")
        while True:
            print("Insira o comando: ")
            texto_digitado = input()
            if texto_digitado == "":
                print("Digite um comando válido!")
                continue
            texto_separado = texto_digitado.split(" ")
            comando = texto_separado[0]

            request_message = b''
            request_message += int(1).to_bytes(1, "big")  # primeira parte do cabecalho

            if len(texto_separado) == 1 and comando == "GETFILESLIST":
                # Buscando a lista dos arquivos
                request_message += int(3).to_bytes(1, "big")
                sock.sendall(request_message)
                response = sock.recv(2048)
                tipo_resposta = response[1]
                if tipo_resposta == 3:
                    qtde_arquivos = int.from_bytes(response[3:], "big")
                    print(f"{qtde_arquivos} arquivo(s) recebidos")
                    for i in range(0, qtde_arquivos):
                        dados_arquivo = sock.recv(1024)
                        len_arquivo = dados_arquivo[0]
                        if len_arquivo == len(dados_arquivo[1:]):
                            print(f'{i} - {dados_arquivo[1:].decode()}')

            elif comando == "ADDFILE":
                request_message += int(1).to_bytes(1, "big")
                nome_arq = texto_separado[1]
                tam_nome_arq = len(nome_arq)
                request_message += tam_nome_arq.to_bytes(1, 'big')
                request_message += nome_arq.encode('utf-8')

                try:
                    with open(diretorio_padrao + nome_arq, 'rb') as arq_binario:
                        sock.sendall(request_message)

                        byte_lido = arq_binario.read(1)
                        tam_arquivo_lido = os.stat(diretorio_padrao + nome_arq).st_size

                        sock.send(tam_arquivo_lido.to_bytes(4, 'big'))

                        print("Enviando arquivo")
                        while byte_lido:
                            sock.send(byte_lido)
                            byte_lido = arq_binario.read(1)
                        print("Arquivo enviado")
                except FileNotFoundError:
                    print("Arquivo nao encontrado")
            elif comando == "DELETE":
                request_message += int(2).to_bytes(1, "big")
                nome_arq = texto_separado[1]
                tam_nome_arq = len(nome_arq)
                request_message += tam_nome_arq.to_bytes(1, 'big')
                request_message += nome_arq.encode('utf-8')
                sock.sendall(request_message)

                response = sock.recv(3)

                if response[2] == 2:
                    print("Problemas ao deletar o arquivo")
                elif response[2] == 1:
                    print(f"Arquivo {nome_arq} excluido")

            elif comando == "GETFILE":
                request_message += int(4).to_bytes(1, "big")
                nome_arq = texto_separado[1]
                tam_nome_arq = len(nome_arq)
                request_message += tam_nome_arq.to_bytes(1, 'big')
                request_message += nome_arq.encode('utf-8')
                sock.sendall(request_message)

                response = sock.recv(7)
                tipo_resposta = response[1]
                status_resposta = response[2] # valida se a request deu certo ou nao
                if tipo_resposta == 4 and status_resposta != 2 :
                    tam_arquivo = int.from_bytes(response[3:7], 'big')
                    print("Recebendo arquivo")
                    with open(diretorio_padrao + nome_arq, 'wb') as arq_binario:
                        for _ in range(0, tam_arquivo):
                            byte_recebido = sock.recv(1)
                            if not byte_recebido:
                                break
                            arq_binario.write(byte_recebido)
                    print("Arquivo Recebido!")
                else:
                    print("Erro na requisição")
                    
            elif comando == "EXIT":
                sock.close()
                exit()


if __name__ == '__main__':
    main()
