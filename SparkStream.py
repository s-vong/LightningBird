from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext 
import sys
import lightningbird

def main():
    #Acquire twitter stream
    stream = lightningbird.run()

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

if __name__ == '__main__':
    main()
