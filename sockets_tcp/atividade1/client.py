"""
Descrição: Cliente que realiza as requisições para o server
Autores: Ilzimara e Leonardo
Data de criação: 07/09/2022
"""

import socket
from hashlib import sha512

def print_man():
    """
    Imprime as opções disponíveis para o user
    """
    man = """
CONNECT <user>,<password> -> conecta a sessão com o usuário e senha informadas

PWD -> mostra o diretório corrente

CHDIR <path> -> altera o diretório atual 

GETFILES -> exibe todos os arquivos do diretório atual

GETDIRS -> exibe todos os subdiretórios

EXIT -> finaliza a sessão    
    """
    print(man)

def main():
    print("Iniciando o cliente")
    # host e porta do servidor
    host = "127.0.0.1"
    port = 12345


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        while True:
            comando_digitado_original = input("\ncmd: ")
            comando_digitado_splitado = comando_digitado_original.split(" ")

            if comando_digitado_splitado[0].lower() == "connect":

                # Convertendo senha para SHA-512
                try:
                    user,senha = comando_digitado_splitado[1].split(",")

                    hash_gerada = sha512(str(senha).encode()).hexdigest()
                except ValueError:
                    print("Usuário e senha digitado de forma incorreta")
                    continue

                sock.sendall(f"CONNECT {user},{hash_gerada}".encode())

                retorno_login = sock.recv(7).decode()
                if retorno_login == "SUCCESS":
                    print("Usuário logado com sucesso")
                elif retorno_login == "ERROR":
                    print("Erro ao realizar login, usuário e/ou senha incorreto")
                else: print("Erro ao conectar com o servidor")

            elif comando_digitado_splitado[0].lower() == "pwd":
                sock.sendall(b"PWD")
                retorno_pwd = sock.recv(1024).decode()

                if retorno_pwd == "ERROR":
                    print("Erro ao buscar o diretório atual, verifique se a sessão está logada")
                else:
                    print(retorno_pwd)

            elif comando_digitado_splitado[0].lower() == "chdir":
                sock.sendall(comando_digitado_original.encode())

                retorno = sock.recv(7)
                if retorno.decode() == "SUCCESS":
                    print("Diretório atualizado com sucesso")
                elif retorno.decode() == "ERROR":
                    print("Erro ao alterar o diretório, verifique se a sessão está logada ou se "
                          "o diretório informado existe")
                else:
                    print("Erro de comunicação com o servidor")

            elif comando_digitado_splitado[0].lower() == "getfiles":
                sock.sendall(b'GETFILES')
                retorno = sock.recv(100).decode()
                if retorno == "ERROR":
                    print("Erro ao buscar arquivos, verifique se a sessão está logada")
                    continue

                qtde_files = int(retorno)
                print(f"{qtde_files} arquivos encontrados\n")
                for _ in range(qtde_files):
                    nome_file = sock.recv(1024)
                    print(nome_file.decode())

            elif comando_digitado_splitado[0].lower() == "getdirs":
                sock.sendall(b'GETDIRS')
                retorno = sock.recv(100).decode()
                if retorno == "ERROR":
                    print("Erro ao buscar diretórios, verifique se a sessão está logada")
                    continue
                qtde_dirs = int(retorno)
                print(f"{qtde_dirs} diretórios encontrados")
                for _ in range(qtde_dirs):
                    nome_dir = sock.recv(1024)
                    print(nome_dir.decode())

            elif comando_digitado_splitado[0].lower() == "exit":
                sock.sendall(b"EXIT")
                print(f"Finalizando conexão ")
                break

            # sock.sendall(comando_digitado[0].encode())
            elif comando_digitado_splitado[0].lower() == "exit":
                break

            else: print_man()
if __name__ == '__main__':
    main()
