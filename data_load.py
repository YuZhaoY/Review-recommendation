from pyspark.sql.types import IntegerType
from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from pyspark.sql.functions import udf, monotonically_increasing_id


class FakeDataLoad(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'FakeDataLoad'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()


    def SelectData(self):
        hc = HiveContext(self.spark.sparkContext)
        # df = hc.sql("select rev_user_id as reviewerID,rev_stars as rating, rev_useful as reviewUsefulCount, "
        #               "rev_text as reviewContent, rev_date as date, user_review_count as reviewCount, "
        #               "user_useful as usefulCount, user_cool as coolCount, user_funny as funnyCount,"
        #               "user_compliment_hot as complimentCount, user_fans as fanCount, stars as restaurantRating from "
        #               "yelp.review inner join yelp.users inner join yelp.business where rev_user_id=rev_user_id and business_id=rev_business_id"
        #               " limit 10000")
        df1 = hc.sql(
            "select rev_user_id as reviewerID, rev_business_id as restaurantID, rev_stars as rating, rev_useful as reviewUsefulCount, "
            "rev_text as reviewContent, rev_date as date from yelp.review limit 1000")
        df2 = hc.sql("select user_id as reviewerID, user_review_count as reviewCount, "
                     "user_useful as usefulCount, user_cool as coolCount, user_funny as funnyCount,"
                     "user_compliment_hot as complimentCount, user_fans as fanCount from yelp.users limit 10000")
        df3 = hc.sql("select business_id as restaurantID, stars as restaurantRating from yelp.business limit 10000")
        result = df1.join(df2, on='reviewerID', how='inner').join(df3, on='restaurantID', how='inner')
        result.show()

        result.write.mode('overwrite').json('fake_dataset')
        # result.show()

if __name__ == '__main__':
    FakeDataLoad().SelectData()