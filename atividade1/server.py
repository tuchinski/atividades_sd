import os.path
import socket
import threading
import time

# USERS
# teste:123
# admin:admin

diretorio_atual_maquina = './server_files'
def conexao_recebida(conexao: socket.socket, endereco: tuple):
    """
    Trata a conexão recebida de um cliente
    :param conexao: socket da conexão recebida
    :param endereco: tupla com o endereço e porta do cliente
    """

    diretorio_atual = '/'
    sessao_logada = False

    while True:
        mensagem_recebida = conexao.recv(1024).decode()
        if not mensagem_recebida:
            break
        comando_recebido = mensagem_recebida.split(" ")

        if comando_recebido[0].lower() == "connect":
            print("Comando connect")
            if len(comando_recebido) != 2:
                # Parametros enviados inválidos
                conexao.sendall(b"ERROR")
                continue
            try:
                user,password = comando_recebido[1].split(",")
            except ValueError:
                conexao.sendall(b"ERROR")
                continue

            if valida_login(user, password):
                print(f"Logando o usuário {user}")
                sessao_logada = True
                conexao.sendall(b"SUCCESS")
            else:
                conexao.sendall(b"ERROR")
                continue

        elif comando_recebido[0].lower() == "pwd":
            if not sessao_logada:
                conexao.sendall(b"ERROR")
                continue

            conexao.sendall((diretorio_atual).encode("UTF-8"))

        elif comando_recebido[0].lower() == "chdir":
            if not sessao_logada:
                conexao.sendall(b"ERROR")
                continue

            if len(comando_recebido) != 2:
                # Caso tenha sido passado mais de dois parâmetros, retorna erro
                conexao.sendall(b"ERROR")
                continue

            # voltando um diretório
            if comando_recebido[1] == '..':
                novo_dir = "/".join(diretorio_atual.split("/")[0:-2]) + "/" # Removendo o diretório atual
            else:
                novo_dir = diretorio_atual  + comando_recebido[1] + '/'

            # Verifica se o diretório informado é válido
            if os.path.isdir(diretorio_atual_maquina + novo_dir):
                diretorio_atual = novo_dir
                conexao.sendall(b"SUCCESS")
            else:
                # Caso nao tenha passado um diretorio correto, retorna erro
                conexao.sendall(b"ERROR")
                continue

        elif comando_recebido[0].lower() == "getfiles":
            if not sessao_logada:
                conexao.sendall(b"ERROR")
                continue
            arquivos = get_files(diretorio_atual_maquina + diretorio_atual)
            conexao.sendall(str(len(arquivos)).encode())
            time.sleep(0.01)
            for item in arquivos:
                time.sleep(0.01)
                conexao.sendall(item.encode())

        elif comando_recebido[0].lower() == "getdirs":
            if not sessao_logada:
                conexao.sendall(b"ERROR")
                continue
            diretorios = get_dirs(diretorio_atual_maquina + diretorio_atual)
            conexao.sendall(str(len(diretorios)).encode())
            time.sleep(0.01)
            for item in diretorios:
                conexao.sendall(item.encode())
                time.sleep(0.01)

        elif comando_recebido[0].lower() == "exit":
            print(f"Finalizando conexão com o cliente {endereco}")
            break

        else:
            print(f"Comando recebido inválido: {mensagem_recebida}")

def valida_login(user: str, passwd: str) -> bool:
    """
    Valida a tentativa de login no server
    :param user: usuário que está tentando logar
    :param passwd: senha do usuário em SHA-512
    :rtype: bool
    :return:
    """
    # lendo a lista com os usuários
    with open("users", "r") as users_file:
        linhas = users_file.readlines()
        for linha in linhas:
            linha = remove_bad_chars(linha)
            user_linha, senha_linha = linha.split(":")
            if user_linha == user:
                if senha_linha == passwd:
                    return True
                else:
                    return False

    return False

def remove_bad_chars(linha: str) -> str:
    """
    Remove caracteres que não fazem parte da string
    :param linha:
    :return:
    """
    return linha.replace("\n", "").replace("\t","")

def get_dirs(nome_dir: str) -> list:
    """
    Retorna todos os subdiretórios do diretório corrente
    :param nome_dir: nome do diretório raiz
    :return: lista com os diretórios
    :rtype: list
    """
    diretorios_disponiveis = []
    # busca todos os subdiretórios
    for file in os.listdir(nome_dir):
        if os.path.isdir(nome_dir + '/' + file):
            diretorios_disponiveis.append(file)
    return diretorios_disponiveis

def get_files(nome_dir: str) -> list:
    """
    Retorna todos os arquivos do diretório informado por parâmetro
    :param nome_dir:
    :return: lista com os arquivos do diretório
    :rtype: list
    """
    arquivos_disponiveis = []
    # busca todos os arquivos
    for file in os.listdir(nome_dir):
        if os.path.isfile(nome_dir + '/' + file):
            arquivos_disponiveis.append(file)
    return arquivos_disponiveis

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
