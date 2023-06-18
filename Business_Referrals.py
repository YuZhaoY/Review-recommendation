from collections import defaultdict
import pandas as pd
from SparkSessionBase import SparkSessionBase
from pyspark import HiveContext

def find_new_frequent_items(dic,frequent_of_k,min_sup):

    curr_set = []
    for key1 in frequent_of_k:
        item1 = set()
        for it1 in key1:
            item1.add(it1)
        for key2 in frequent_of_k:
            item2 = set()
            for it2 in key2:
                item2.add(it2)
            set1 = item1.union(item2)
            set2 = item1.intersection(item2)
            if len(set1.difference(set2)) == 2:
                count = 0
                for num in range(0, 5):
                    if set1.issubset(dic[num]):
                        count += 1
                    if count >= min_sup:
                        curr_set.append(frozenset(set1))
                        break
    return dict((item, "fq")for item in curr_set)


class BusinessReferrals(SparkSessionBase):
    SPARK_URL = "local"
    SPARK_APP_NAME = 'business_analysis'
    ENABLE_HIVE_SUPPORT = True

    def __init__(self):
        self.spark = self._create_spark_session()

    def Recommend(self):
        import re
        hc = HiveContext(self.spark.sparkContext)
        data_length = 2000
        result = hc.sql("select attributes from yelp.business where stars>=4 limit 2000")
        dic = {}
        dic = defaultdict(set)
        s=set()
        for i in range(0, data_length):
            temp = str(result.collect()[i])
            temp_list = re.findall(r'"(.+?)"', temp)
            length = len(temp_list)
            for num in range(0, length, 2):
                value = temp_list[num]+":"+temp_list[num+1]
                s.add(value)
                dic[i].add(value)
        frequent_itemsets = {}
        min_sup = 100
        frequent_itemsets[1] = dict((frozenset((item,)), "fq")for item in s)

        for k in range(2, 20):
            curr_set=find_new_frequent_items(dic, frequent_itemsets[k-1], min_sup)
            if len(curr_set) == 0:
                print("{}项生成的备选项集长度为0，不再进行生成".format(k))
                break
            else:
                print("准备进行{}项生成备选项集".format(k))
                frequent_itemsets[k] = curr_set
                for item in frequent_itemsets[k]:
                    print(item)
        del frequent_itemsets[1]
        items=pd.DataFrame.from_dict(frequent_itemsets[k-1], orient='index', columns=['fq'])
        frame2=items.reset_index()
        frame3= frame2.rename(columns={'index': 'items'})
        frame3=frame3.drop('fq', axis=1)
        frame3.to_csv('frequent.csv', index=False)



if __name__ == '__main__':
    BusinessReferrals().Recommend()


















