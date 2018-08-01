import twitter_cred
import twitter
import socket
import json

def get_tweets():
    api = twitter.Api(twitter_cred.CONSUMER_KEY, 
        twitter_cred.CONSUMER_SECRET, 
        twitter_cred.ACCESS_TOKEN, 
        twitter_cred.ACCESS_SECRET)

    tag_lists = ['sdcc', 'San Diego']
    response = api.GetStreamFilter(track = tag_lists)
    return response

def create_tcp():
    host = socket.gethostname()
    port = 9009
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (host, port) )
    s.listen(1)
    return s

def send_tweets(response, sock):
    try:
        print("Waiting for TCP connection...")
        conn, addr = sock.accept()
        with conn:
            print("Connected by...  ", addr)
            conn.sendall(b'Hello')
            for line in response:
                twt = json.dumps(line)
                conn.sendall(twt)
    except:
        pass

def run():
    response = get_tweets()
    sock = create_tcp()
    send_tweets(response, sock)
    
if __name__ == '__main__':
    run()
