from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext 
import sys
import requests
import lightningbird
import socket

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

stream = lightningbird.run()

#socket = createSocket() #Insert parameter 
host = socket.gethostname()
port = 9009
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
for twt in stream:
    s.send(str(twt))
s.listen(1)

conf = SparkConf().setAppName("LightningBird")
sc = SparkContext(conf=conf)

ssc = StreamingContext(sc, 5)   #StreamingContext(Spark Context, Seconds between processing stream)
dataStream = ssc.socketTextStream("localhost", 9009)    #Listen for data from TCP source on local host port 9009

ssc.start()
ssc.awaitTermination()
