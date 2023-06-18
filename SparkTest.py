import pandas as pd

from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from JDBC import JDBC

class SparkTest(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'SparkTest'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql("select rev_text from yelp.review limit 10000")
        txt = b_df.collect().__str__()
        txt = txt.lower()
        for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’1234567890':
            txt = txt.replace(ch, "")
        words = txt.split()
        counts = {}
        stop_words = open("stop_words.txt", "r", encoding='utf-8', errors='ignore').read()
        for word in words:
            if (word not in stop_words):
                counts[word] = counts.get(word, 0) + 1

        items = pd.DataFrame.from_dict(counts, orient='index', columns=['counts'])
        frame2 = items.reset_index()
        frame3 = frame2.rename(columns={'index': 'word'})
        # df=hc.createDataFrame(counts.keys(), counts.values())

        frame3.to_csv('wordcount.csv', index=False)
        print(111111111111111111111111111111111111111)

        # b_df = hc.sql("SELECT name FROM yelp.business limit 20")
        # b_df.show()
        # prop = JDBC.prop
        # url = JDBC.url
        # b_df.write.jdbc(url, 'test', 'append', prop)


# XXX 大数据分析代码


if __name__ == '__main__':
    SparkTest().start()