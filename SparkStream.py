from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext 
import sys
import lightningbird

def main():
    #Set up Spark
    conf = SparkConf().setAppName("LightningBird")
    sc = SparkContext(conf=conf)

    #StreamingContext(Spark Context, Seconds between processing stream)
    ssc = StreamingContext(sc, 5)   

    #Listen for data from TCP source on local host port 9009
    dataStream = ssc.socketTextStream("laptop", 9009)    

    #Processing
    wordscnt = dataStream.flatmap(dataStream.split(" ")).count()
    print(wordscnt)

    #Start Streaming
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    main()
