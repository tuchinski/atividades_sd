class Mensagem:
    def __init__(self, bytes_mensagem):

        self.bytes_mensagem = bytes_mensagem

        self.tipo_mensagem = bytes_mensagem.decode()[0]

        self.tam_nickname = bytes_mensagem[1]
    
        self.nickname = bytes_mensagem[2:self.tam_nickname+2].decode()
    
        self.tam_msg = bytes_mensagem[self.tam_nickname+2]
    
        self.msg_recebida = bytes_mensagem[self.tam_nickname+3:self.tam_nickname+3 + self.tam_msg].decode()

    def __str__(self):
        return f" tipo_mensagem = {self.tipo_mensagem}\ntam_nickname = {self.tam_nickname}\nnickname = {self.nickname}\ntam_msg = {self.tam_msg}\nmsg_recebida {self.msg_recebida}"

    def imprime_mensagem(self):
        nome_tipo_mensagem = ""
        if self.tipo_mensagem == "1":
            nome_tipo_mensagem = "NORMAL"
        elif self.tipo_mensagem == "2":
            nome_tipo_mensagem = "EMOJI"
        elif self.tipo_mensagem == "3":
            nome_tipo_mensagem = "URL"
        elif self.tipo_mensagem == "4":
            nome_tipo_mensagem = "ECHO"
        print(f"Mensagem {nome_tipo_mensagem} de {self.nickname} - {self.msg_recebida}")