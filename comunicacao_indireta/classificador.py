import pika
from config import *


def main():
    # conexao com o rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    canal = connection.channel()

     # declara a lista tweets
    canal.queue_declare(queue="tweets")


    def callback(ch, method, properties, body):
            # Convertendo o texto para string
            data = body.decode()

            # iterando dentro dos topicos desejados
            for topic in TOPICS:

                # Validando se o tweet pertence ao topico
                if topic in data.lower():
                    print("Topico: ", topic)

                    # Fila de comunicacao entre o classificador e cliente
                    canal.exchange_declare(exchange="direct_logs", exchange_type='direct')
                    # Enviando o tweet pra fila correta
                    canal.basic_publish(exchange="direct_logs", routing_key=str(topic), body=body)

    # consumindo os dados da fila "tweets"
    canal.basic_consume(queue="tweets", on_message_callback=callback, auto_ack=True)

    # inicia o consumo da fila
    canal.start_consuming()

if __name__ == "__main__":
    main()