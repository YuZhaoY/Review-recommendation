from pyspark.sql.types import IntegerType
from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from pyspark.sql.functions import udf, monotonically_increasing_id


class SparkTest(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'SparkTest'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    @staticmethod
    def conversion(stars):
        if stars == 1 or stars == 2:
            return 0
        if stars == 3:
            return 1
        if stars == 4 or stars == 5:
            return 2


    def SelectData(self):
        hc = HiveContext(self.spark.sparkContext)
        func_udf = udf(self.conversion, IntegerType())
        b_df = hc.sql("select rev_text,rev_stars from yelp.review limit 10000")
        df2 = b_df.withColumn("ID", monotonically_increasing_id())
        result = df2.withColumn('rev_class', func_udf(b_df.rev_stars))
        result.write.mode('overwrite').json('output')
        result.show()

if __name__ == '__main__':
    SparkTest().SelectData()