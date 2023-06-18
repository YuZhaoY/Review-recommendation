from datetime import datetime, timedelta
from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from JDBC import JDBC

prop = JDBC.prop
url = JDBC.url

class StarsAnalysis(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'UserAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def recent_weekstars(self,date):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql("select rev_business_id, rev_date, rev_stars from yelp.review where  limit 10000")
        date1=datetime.strptime(date, "%Y-%m-%d")
        df=b_df.select('rev_business_id', 'rev_date', 'rev_stars').where(
            (b_df['rev_date'] > date1-timedelta(7)) & (b_df['rev_date'] <= date1)).orderBy('rev_business_id')
        df.write.jdbc(url, 'recent_weekstars', 'overwrite', prop)

if __name__ == '__main__':
    date='2018-04-15'
    StarsAnalysis().recent_weekstars(date)