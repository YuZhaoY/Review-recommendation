from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext


class UserAnalysis(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'UserAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def register_annually(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql("SELECT year(to_date(user_yelping_since)) as year, COUNT(*) FROM yelp.users GROUP BY year(to_date(user_yelping_since))")
        b_df.show()

    def critic(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql(
            "SELECT user_id, user_name, user_review_count FROM yelp.users ORDER BY user_review_count DESC")
        b_df.limit(10).show()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql("SELECT user_yelping_since FROM yelp.users")
        b_df.show()

# XXX 大数据分析代码
    def elite_ratio(self, year):
        hc = HiveContext(self.spark.sparkContext)
        df1 = hc.sql("SELECT COUNT(*) FROM yelp.users WHERE user_elite LIKE '%" + year + "%'")
        df2 = hc.sql("SELECT COUNT(*) FROM yelp.users WHERE LEFT(user_yelping_since, 4) <= '" + year + "'")
        df1.show()
        df2.show()

    def silence_ratio(self, year):
        hc = HiveContext(self.spark.sparkContext)
        # df1 = hc.sql("SELECT COUNT(*) FROM yelp.users WHERE LEFT(user_yelping_since, 4) <= '" + year + "'")
        df1 = hc.sql("SELECT DISTINCT rev_user_id as user_id FROM yelp.review WHERE year(rev_date) <= '2020'")
        df2 = hc.sql("SELECT DISTINCT rev_user_id as user_id FROM yelp.review WHERE year(rev_date) <= '2021'")
        df3 = hc.sql("SELECT DISTINCT rev_user_id as user_id FROM yelp.review WHERE year(rev_date) <= '2022'")
        # df1.show()
        print(df1.count())
        print(df2.count())
        print(df3.count())

    def popularity_user(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql(
            "SELECT user_id, user_name, user_fans FROM yelp.users ORDER BY user_fans DESC")
        b_df.limit(10).show()

    def annually_number(self):
        hc = HiveContext(self.spark.sparkContext)
        b_df = hc.sql(
            "SELECT COUNT(*) FROM yelp.review WHERE ")
        b_df.limit(10).show()
        

if __name__ == '__main__':
    UserAnalysis().silence_ratio("2020")