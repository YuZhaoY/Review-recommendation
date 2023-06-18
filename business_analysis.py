from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from JDBC import JDBC

prop = JDBC.prop
url = JDBC.url

class BusinessAnalysis(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'business_analysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def most_business(self):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql(
            "SELECT name, COUNT(name) as name_count, AVG(stars) as avg_stars "
            "FROM yelp.business "
            "GROUP BY name "
            "ORDER BY name_count DESC "
            "LIMIT 20")
        result.show()

        result.write.jdbc(url, 'most_business', 'overwrite', prop)

    def city_best_business(self, str):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("select business_id, name, city, stars from yelp.business where city like '%"+str+"%' "
                        "order by stars desc limit 10")
        result.write.jdbc(url, 'city_best_business', 'overwrite', prop)


    def most_category(self):
        hc = HiveContext(self.spark.sparkContext)
        result=hc.sql("SELECT name,(LENGTH(categories) - LENGTH(REPLACE(categories, ',', '')) + 1) as category_count "
                      "FROM yelp.business "
                      "ORDER BY category_count DESC "
                      "LIMIT 10")
        result.show()

        result.write.jdbc(url, 'most_category', 'overwrite', prop)

    def categories_number(self, str):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("SELECT count(*) as categories_number "
                        "FROM(select * from yelp.business where categories LIKE '%"+str+"%') "
                        )
        result.write.jdbc(url, 'categories_number', 'append', prop)
        result.show()

    def categories_stars(self, str):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("select business_id, avg(stars) as avg_stars from yelp.business where categories LIKE '%"+str+"%' "
                        "group by business_id "
                        "order by avg_stars desc "
                        "limit 10")
        result.write.jdbc(url, 'categories_stars2', 'overwrite', prop)

    def review_number(self,str):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("select name, SUM(review_count) as review_num, count(stars=1 or NULL) as s1, count(stars=1.5 or NULL) as s11, count(stars=2 or NULL) as s2, count(stars=2.5 or NULL) as s22, count(stars=3 or NULL) as s3, count(stars=3.5 or NULL) as s33, count(stars=4 or NULL) as s4, count(stars=4.5 or NULL) as s44, count(stars=5 or NULL) as s5 from yelp.business where categories LIKE '%"+str+"%' Group By name order by review_num desc limit 20")
        result.write.jdbc(url, 'review_number1', 'overwrite', prop)
        result.show()

    def most_Fivestar(self):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("select name, count(*) as fivestar_num from yelp.business "
                      "where stars=5 Group By name order by fivestar_num desc limit 20")
        result.write.jdbc(url, 'most_Fivestar', 'overwrite', prop)
        result.show()

    def most_Negativestar(self):
        hc = HiveContext(self.spark.sparkContext)
        result = hc.sql("select name, count(*) as Negative_num from yelp.business "
                      "where stars<=2 Group By name order by fivestar_num desc limit 20")
        result.write.jdbc(url, 'most_Negative_star', 'overwrite', prop)
        result.show()

if __name__ == '__main__':
    str = 'Affton'
    BusinessAnalysis().city_best_business(str)
    # BusinessAnalysis().most_Negativestar()
    # BusinessAnalysis().most_category()

    # BusinessAnalysis().categories_stars(str)
    # BusinessAnalysis().categories_number(str)
    # BusinessAnalysis().review_number(str)
    # BusinessAnalysis().most_Fivestar()
    print("end")































