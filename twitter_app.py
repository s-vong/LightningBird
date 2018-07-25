import socket
import sys
import requests
from requests_oauthlib import OAuth1 
import json
import twitter_cred

my_auth = OAuth1(twitter_cred.CONSUMER_KEY, twitter_cred.CONSUMER_SECRET, twitter_cred.ACCESS_TOKEN, twitter_cred.ACCESS_SECRET)

def get_tweets():
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('locations', '-130, -20, 100, 50'), ('track', '#')]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response

def send_tweets(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet text: " + tweet_text)
            print("---------------------------------")
            tcp_connection.send(tweet_text + '\n')
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)

TCP_IP = "localhost"
TCP_PORT = 9009
conn = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
'''
print("Waiting for TCP connection...")

conn = s.accept()
print("Connected... Starting acquiring tweets.")

resp = get_tweets()
send_tweets(resp, conn)
'''
