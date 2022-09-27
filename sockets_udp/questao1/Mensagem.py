class Mensagem:
    def __init__(self, bytes_mensagem):

        self.tipo_mensagem = bytes_mensagem.decode()[0]

        self.tam_nickname = bytes_mensagem[1]
    
        self.nickname = bytes_mensagem[2:self.tam_nickname+2].decode()
    
        self.tam_msg = bytes_mensagem[self.tam_nickname+2]
    
        self.msg_recebida = bytes_mensagem[self.tam_nickname+3:self.tam_nickname+3 + self.tam_msg].decode()

        
    def __str__(self):
        return f" tipo_mensagem = {self.tipo_mensagem}\ntam_nickname = {self.tam_nickname}\nnickname = {self.nickname}\ntam_msg = {self.tam_msg}\nmsg_recebida {self.msg_recebida}"