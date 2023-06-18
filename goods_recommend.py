from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.feature import StringIndexer, IndexToString
from pyspark.sql.functions import *
from JDBC import JDBC
from pandas import pandas as pd
prop = JDBC.prop
url = JDBC.url

class FriendRecommend(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'UserAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):
        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT rev_user_id, rev_business_id, rev_stars FROM yelp.review LIMIT 10000")
        indexer1 = StringIndexer(inputCol="rev_user_id", outputCol="user")  # 构建StringIndexer对象，设定输入列和输出列
        indexer2 = StringIndexer(inputCol="rev_business_id", outputCol="business")

        model1 = indexer1.fit(df)  # 构建model模型
        indexed1 = model1.transform(df)  # 使用模型转换数据，将商店名转换为数值，可以进行度量
        model2 = indexer2.fit(indexed1)
        indexed2 = model2.transform(indexed1)
        #indexed2.show(10)

        train, test = indexed2.randomSplit([0.75, 0.25])                                             # 划分训练数据和测试数据

        rec = ALS(maxIter=10, regParam=0.01, userCol='user', itemCol='business', ratingCol='rev_stars', nonnegative=True, coldStartStrategy="drop")

        rec_model = rec.fit(train)                     # 使用模型训练数据

        predicted_ratings = rec_model.transform(test)  # 应用于测试数据

        predicted_ratings.printSchema()

        predicted_ratings.orderBy(rand()).show(10)   # 参看应用模型预测的数据

        # evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
        #                                predictionCol="prediction")

        # rmse = evaluator.evaluate(predicted_ratings)
        # print("Root-mean-square error = " + str(rmse))

        # Generate top 10 movie recommendations for each user
        userRecs = rec_model.recommendForAllUsers(10)
        userRecs.withColumn("recommendations", col("recommendations").cast('string'))
        user_df = userRecs.join(indexed2, on="user", how="inner")
        user_df_panda = user_df.toPandas()
        print(user_df_panda)
        user_df_panda.to_csv("userRecs.csv")
        # Generate top 10 user recommendations for each good
        goodsRecs = rec_model.recommendForAllItems(10)
        good_df = goodsRecs.join(indexed2, on="business", how="inner")
        good_df_panda = good_df.toPandas()
        print(good_df_panda)
        good_df_panda.to_csv("goodsRecs.csv")


        #predicted_ratings.write.jdbc(url, 'goods_recommend', 'overwrite', prop)
        #userRecs.write.mode('overwrite').csv('userRecs')
        #goodsRecs.write.mode('overwrite').csv('goodsRecs')

if __name__ == '__main__':
    FriendRecommend().start()