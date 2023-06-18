from collections import defaultdict

import pandas as pd

from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext
from itertools import product

class FriendRecommend(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'UserAnalysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def start(self):

        hc = HiveContext(self.spark.sparkContext)
        df = hc.sql("SELECT user_id, user_friends FROM yelp.users limit 1000 ")


        relation_friend = {}
        relation_friend = defaultdict(set)

        for user_id, user_friends in df.collect():
            my_list = user_friends.split(',')
            result = set(my_list)
            relation_friend[user_id] = result
        indirect_friend = {}
        indirect_friend = defaultdict(list)
        for key1, value1 in relation_friend.items():
            for key2, value2 in relation_friend.items():
                if key1 != key2 and key2 not in value1 and len(value1.intersection(value2)) >= 200:
                    indirect_friend[key1].append(key2)

        items = pd.DataFrame.from_dict(indirect_friend, orient='index')
        frame2 = items.reset_index()
        frame3 = frame2.rename(columns={'index': 'user_id'})
        tmp=frame3.set_index(['user_id']).stack()
        tmp.index.names=['user_id', 'recommend']
        # df=hc.createDataFrame(counts.keys(), counts.values())

        tmp.to_csv('friend_recommend.csv', index=True)
if __name__ == '__main__':
    FriendRecommend().start()