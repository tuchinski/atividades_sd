import socket


def main():
    print("Iniciando o cliente")
    # host e porta do servidor
    host = "127.0.0.1"
    port = 12345


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        while True:
            comando_digitado_original = input()
            comando_digitado_splitado = comando_digitado_original.split(" ")

            if comando_digitado_splitado[0].lower() == "connect":
                print("Comando connect")
            elif comando_digitado_splitado[0].lower() == "pwd":
                sock.sendall(b"PWD")
                retorno_pwd = sock.recv(1024)
                print(retorno_pwd.decode())

            elif comando_digitado_splitado[0].lower() == "chdir":
                sock.sendall(comando_digitado_original.encode())

                retorno = sock.recv(7)
                if retorno.decode() == "SUCCESS":
                    print("Diretório atualizado com sucesso")
                elif retorno.decode() == "ERROR":
                    print("Erro ao alterar o diretório")
                else:
                    print("Erro de comunicação com o servidor")

            elif comando_digitado_splitado[0].lower() == "getfiles":
                sock.sendall(b'GETFILES')
                qtde_files = int(sock.recv(100).decode())
                for _ in range(qtde_files):
                    nome_file = sock.recv(1024)
                    print(nome_file.decode())

            elif comando_digitado_splitado[0].lower() == "getdirs":
                sock.sendall(b'GETDIRS')
                qtde_dirs = int(sock.recv(100).decode())
                for _ in range(qtde_dirs):
                    nome_dir = sock.recv(1024)
                    print(nome_dir.decode())

            elif comando_digitado_splitado[0].lower() == "exit":
                sock.sendall(b"EXIT")
                print(f"Finalizando conexão ")
                break

            # sock.sendall(comando_digitado[0].encode())
            if comando_digitado_splitado[0].lower() == "exit":
                break

if __name__ == '__main__':
    main()
