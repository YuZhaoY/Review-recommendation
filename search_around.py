import math
from pyspark.sql.functions import udf, lit, col
from pyspark.sql.types import FloatType

from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from JDBC import JDBC

prop = JDBC.prop
url = JDBC.url

class SearchAround(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'SearchAround'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    @staticmethod
    def haversine(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return c * 6367 * 1000

    def start(self, lon, lat):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT * FROM yelp.business")
        func_udf = udf(self.haversine, FloatType())
        df1 = df.withColumn("distance_to_business", func_udf(lit(lon), lit(lat), df['longitude'], df['latitude']))
        df2 = df1.orderBy("distance_to_business").limit(50)
        df2.write.jdbc(url, 'nearby_search', 'overwrite', prop)
        df2.show()

if __name__ == '__main__':
    SearchAround().start(-74.7, 40.2)



