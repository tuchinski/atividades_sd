import pika
import sys
from config import * 

def main():

    # Verificando se o usuário digitou o assunto que quer acompanhar
    try:
        topico_escolhido = sys.argv[1]
    except IndexError:
        print("informar o tópico a ser escolhido: python3 cliente.py <nome_topico>")
        exit(1)
    
    # Validando se o assunto digitado está dentro dos topicos pré-definidos
    if topico_escolhido not in TOPICS:
        print("Tópico não esta na lista")
        print("Topicos disponiveis", TOPICS)
        exit(1)

    # Criando conexão com o rabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Cria uma fila exclusiva para o cliente
    queue = channel.queue_declare(queue="", exclusive=True)
    nome_queue = queue.method.queue

    # Binda a queue na exchange, usando como routing_key o topico escolhido
    channel.queue_bind(nome_queue, "exchange_twitter", topico_escolhido)

    print('Esperando novas informações na fila.')

    def callback(ch, method, properties, body):
        """
        Método de callback que imprime o tweet da fila
        """
        data = body.decode()
        print(data)
        print("------------------------------------------------------")


    # Consumindo a lista desejada
    channel.basic_consume(queue=nome_queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Encerrado")