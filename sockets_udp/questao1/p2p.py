import socket
from threading import Thread
from Mensagem import Mensagem

# host e porta do servidor p2p
porta = 5678
host = "0.0.0.0"

outro_server = ("192.168.1.15", 5678)
apelido_definido = "teste"

# tipos de mensagem
# 1: mensagem normal
# 2: emoji
# 3: URL
# 4: ECHO (envia e recebe a mesma mensagem para indicar que usuário está ativo).

# variavel que guarda se o cliente quem fez o echo request 
make_echo_request = False

def trata_pacote_recebido(sock: socket.socket, apelido: str):
    while True: 
        bytes_recebido, endereco = sock.recvfrom(1024)
        msg_recebida = Mensagem(bytes_recebido)
        print(msg_recebida)

        print(f"\n\nChegou algo do endereco {endereco}")
            
        # define o tipo de mensagem recebida
        if msg_recebida.tipo_mensagem == "1":
            # mensagem normal
            recebe_mensagem_normal(bytes_recebido, endereco)
        elif msg_recebida.tipo_mensagem == "2":
            # emoji
            pass
        elif msg_recebida.tipo_mensagem == "3":
            # URL
            pass
        elif msg_recebida.tipo_mensagem == "4":
            # ECHO
            recebe_echo(msg_recebida, endereco, apelido, sock)
            pass

def recebe_mensagem_normal(bytes_recebidos: bytes, endereco: tuple):
    
    tam_nickname = bytes_recebidos[1]
    
    nickname = bytes_recebidos[2:tam_nickname+2].decode()
    
    
    tam_msg = bytes_recebidos[tam_nickname+2]
    
    msg_recebida = bytes_recebidos[tam_nickname+3:tam_nickname+3 + tam_msg].decode()

    print(f"[{nickname}] - {msg_recebida}")

def recebe_echo(msg_recebida: Mensagem, endereco: tuple, apelido: str, sock: socket.socket):
    global make_echo_request

    print(f"Recebendo echo de {msg_recebida.nickname} - endereco: {endereco}")
    
    if make_echo_request == False:
        print(f"enviando echo para {msg_recebida.nickname} - endereco: {endereco}")

        msg_echo_retorno = Mensagem(monta_packet_mensagem("4", apelido, ""))
        sock.sendto(msg_echo_retorno.bytes_mensagem, endereco)
    
    make_echo_request = False
    

def monta_packet_mensagem(tipo_mensagem: str, apelido: str, mensagem: str) -> bytes:
    '''
    Monta a mensagem a ser enviada
    '''
    # adicionando tipo msg
    bytes_mensagem = tipo_mensagem.encode()

    # adicionando tamanho do nickname
    bytes_mensagem = bytes_mensagem + len(apelido).to_bytes(1, "big")

    # adicionado o nickname
    bytes_mensagem = bytes_mensagem + apelido.encode()

    # adicionando tamanho msg
    bytes_mensagem = bytes_mensagem + len(mensagem).to_bytes(1, "big")

    # adicionando a mensagem
    bytes_mensagem = bytes_mensagem + mensagem.encode()

    return bytes_mensagem


def envia_mensagem_normal(sock: socket.socket, apelido: str):
    msg_enviar = input("Digite a msg que deseja enviar: ")

    bytes_msg  = monta_packet_mensagem("1", apelido, msg_enviar)
    sock.sendto(bytes_msg, outro_server)
    
def envia_mensagem_echo(sock: socket.socket, apelido):
    global make_echo_request

    make_echo_request = True
    sock.sendto(monta_packet_mensagem("4", apelido, ""), outro_server)

def envia_mensagens(sock: socket.socket, apelido: str):
    while True:
        tipo_msg = input("Digite o tipo de mensagem que quer enviar: ")

        if tipo_msg == "1":
            # mensagem normal
            envia_mensagem_normal(sock, apelido)
            pass
        elif tipo_msg == "2":
            # emoji
            pass
        elif tipo_msg == "3":
            # URL
            pass
        elif tipo_msg == "4":
            envia_mensagem_echo(sock, apelido)
            pass
        else:
            print("tipo de msg inválido")



def main():
    print("Iniciando o server p2p")
    apelido_definido = input("Digite seu apelido: ")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # desocupa a porta assim que o server é finalizado
        s.bind((host, porta))

        t1 = Thread(target=trata_pacote_recebido, args=(s,apelido_definido,))
        t2 = Thread(target=envia_mensagens, args=(s,apelido_definido, ))

        t1.start()
        t2.start()
        t1.join()
        t2.join()
        


    



if __name__ == "__main__":
    main()