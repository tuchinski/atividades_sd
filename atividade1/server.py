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
    user_atual = None

    while True:
        mensagem_recebida = conexao.recv(1024).decode()
        if not mensagem_recebida:
            break
        comando_recebido = mensagem_recebida.split(" ")

        if comando_recebido[0].lower() == "connect":
            print(f"Recebendo CONNECT do cliente {endereco}")
            if len(comando_recebido) != 2:
                # Parametros enviados inválidos
                print(f"Erro CONNECT do cliente {endereco}")
                conexao.sendall(b"ERROR")
                continue
            try:
                user,password = comando_recebido[1].split(",")
            except ValueError:
                print(f"Erro CONNECT do cliente {endereco}")
                conexao.sendall(b"ERROR")
                continue

            if valida_login(user, password):
                print(f"Logando o usuário {user} do endereço {endereco}")
                sessao_logada = True
                user_atual = user
                conexao.sendall(b"SUCCESS")
            else:
                print(f"Erro CONNECT do usuário {user} para o cliente {endereco}")
                conexao.sendall(b"ERROR")
                continue

        elif comando_recebido[0].lower() == "pwd":
            print(f"Recebendo PWD do cliente {endereco} e user {user_atual}")
            if not sessao_logada:
                print(f"Cliente {endereco} tentando PWD sem login")
                conexao.sendall(b"ERROR")
                continue

            print(f"Enviando PWD {diretorio_atual} para o cliente {endereco} e user {user_atual}")
            conexao.sendall((diretorio_atual).encode("UTF-8"))

        elif comando_recebido[0].lower() == "chdir":
            print(f"Recebendo CHDIR do cliente {endereco} e user {user_atual}")
            if not sessao_logada:
                print(f"Cliente {endereco} tentando CHDIR sem login")
                conexao.sendall(b"ERROR")
                continue

            if len(comando_recebido) != 2:
                # Caso tenha sido passado mais de dois parâmetros, retorna erro
                print(f"Parâmetros errados do cliente {endereco} e user {user_atual} para o comando CHDIR")
                conexao.sendall(b"ERROR")
                continue

            # voltando um diretório
            if comando_recebido[1] == '..':
                novo_dir = "/".join(diretorio_atual.split("/")[0:-2]) + "/" # Removendo o diretório atual
            else:
                novo_dir = diretorio_atual  + comando_recebido[1] + '/'

            # Verifica se o diretório informado é válido
            if os.path.isdir(diretorio_atual_maquina + novo_dir):
                print(f"Alterando o diretório de {diretorio_atual} para {novo_dir} para o cliente {endereco} e user {user_atual}")
                diretorio_atual = novo_dir
                conexao.sendall(b"SUCCESS")
            else:
                # Caso nao tenha passado um diretorio correto, retorna erro
                print(f"Diretório {novo_dir} informado inválido para o cliente {endereco} e user {user_atual}")
                conexao.sendall(b"ERROR")
                continue

        elif comando_recebido[0].lower() == "getfiles":
            print(f"Recebendo GETFILES do cliente {endereco} e user {user_atual}")
            if not sessao_logada:
                print(f"Cliente {endereco} tentando GETFILES sem login")
                conexao.sendall(b"ERROR")
                continue

            arquivos = get_files(diretorio_atual_maquina + diretorio_atual)
            print(f"Encontrados {str(len(arquivos))} arquivos na solicitação do cliente {endereco} e user {user_atual}")
            conexao.sendall(str(len(arquivos)).encode())
            time.sleep(0.01)
            for item in arquivos:
                time.sleep(0.01)
                print(f"Enviando nome arquivo {item} para o cliente {endereco} e user {user_atual}")
                conexao.sendall(item.encode())

        elif comando_recebido[0].lower() == "getdirs":
            print(f"Recebendo GETDIRS do cliente {endereco} e user {user_atual}")
            if not sessao_logada:
                print(f"Cliente {endereco} tentando GETDIRS sem login")
                conexao.sendall(b"ERROR")
                continue
            diretorios = get_dirs(diretorio_atual_maquina + diretorio_atual)
            print(f"Encontrados {str(len(diretorios))} diretorios na solicitação do cliente {endereco} e user {user_atual}")
            conexao.sendall(str(len(diretorios)).encode())
            time.sleep(0.01)
            for item in diretorios:
                conexao.sendall(item.encode())
                print(f"Enviando nome diretorio {item} para o cliente {endereco} e user {user_atual}")
                time.sleep(0.01)

        elif comando_recebido[0].lower() == "exit":
            print(f"Finalizando conexão com o cliente {endereco} e user {user_atual}")
            break

        else:
            print(f"Comando recebido inválido {mensagem_recebida} do cliente {endereco}")

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
