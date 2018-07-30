from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext 
import sys
import requests
import lightningbird
import socket
import json

'''
def createSocket():
#    Function to create socket
#    Must be on local host and on port 9009

    host = socket.gethostname()
    port = 9009
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    return s
'''  

def main():
    #Acquire twitter stream
    stream = lightningbird.run()

    #Create TCP connection
    host = socket.gethostname()
    port = 9009
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (host, port) )

    #Send data through TCP 
    for line in stream:
        twt = json.loads(line)
        s.send(twt)
    s.listen(1)

'''
    #Set up Spark
    conf = SparkConf().setAppName("LightningBird")
    sc = SparkContext(conf=conf)

    #StreamingContext(Spark Context, Seconds between processing stream)
    ssc = StreamingContext(sc, 5)   

    #Listen for data from TCP source on local host port 9009
    dataStream = ssc.socketTextStream("localhost", 9009)    

    #Start Streaming
    ssc.start()
    ssc.awaitTermination()
'''

if __name__ == '__main__':
    main()
