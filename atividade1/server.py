import socket
import threading



def conexao_recebida(conexao: socket.socket, endereco: tuple):
    """
    Trata a conexão recebida de um cliente
    :param conexao: socket da conexão recebida
    :param endereco: tupla com o endereço e porta do cliente
    """

    diretorio_atual = '/'
    while True:
        mensagem_recebida = conexao.recv(1024).decode()
        if not mensagem_recebida:
            break
        comando_recebido = mensagem_recebida.split(" ")

        if comando_recebido[0].lower() == "connect":
            print("Comando connect")
        elif comando_recebido[0].lower() == "pwd":
            print("Comando pwd")
            conexao.sendall(diretorio_atual.encode("UTF-8"))
        elif comando_recebido[0].lower() == "chdir":
            print("Comando chdir")
        elif comando_recebido[0].lower() == "getfiles":
            print("Comando getfiles")
        elif comando_recebido[0].lower() == "getdirs":
            print("Comando getdirs")
        elif comando_recebido[0].lower() == "exit":
            print(f"Finalizando conexão com o cliente {endereco}")
            break
        else:
            print(f"Comando recebido inválido: {mensagem_recebida}")


def main():
    print("Iniciando o server")

    # host e porta do servidor
    host = "127.0.0.1"
    port = 12345

    # criando o socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # desocupa a porta assim que o server é finalizado
        s.bind((host, port))
        s.listen()

        print("Servidor iniciado")
        while True:
            conn, addr = s.accept() # aguarda nova conexão com o server
            print(f"Recebida nova conexão com o server: {addr}")
            threading.Thread(target=conexao_recebida, args=(conn, addr,)).start()




if __name__ == '__main__':
    main()
