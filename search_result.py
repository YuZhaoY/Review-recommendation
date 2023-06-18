from pyspark.sql.functions import udf, lit
from pyspark.sql.types import FloatType

from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext


class SearchResult(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'SearchResult'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def sort(self, opt, order):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT business_id, name, address, city, stars, review_count, is_open, attributes, categories, "
                    "hours FROM yelp.business ORDER BY " + opt + " " + order)
        df.show()

    def conditional_filtration(self, opt, compare, value):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT business_id, name, address, city, stars, review_count, is_open, attributes, categories, "
                    "hours FROM yelp.business WHERE" + opt + compare + value)
        df.show()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT business_id, name, longitude, latitude FROM yelp.business")
        df.show()


if __name__ == '__main__':
    SearchResult().sort('stars', 'DESC')