import tweepy
import pika
import sys
from config import * 

# criando uma fila no rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = connection.channel()

def main():
    # definindo o auth do twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # cliente do tweepy
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    
    # declarando a fila "tweets"
    channel.queue_declare(queue=QUEUE)

    query = ' OR '.join(TOPICS)

    # buscando os tweets com os tópicos
    response = client.search_recent_tweets(query=query, max_results=100)

    # publicando os tweets na fila
    for tweet in response.data:
        print(tweet.text)
        channel.exchange_declare(exchange="tweets", exchange_type='direct')
        channel.basic_publish(exchange='', routing_key="tweets", body= tweet.text)
    
    connection.close()
    


if __name__ == "__main__":
    main()