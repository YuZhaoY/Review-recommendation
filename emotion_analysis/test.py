import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib
from sklearn.metrics import accuracy_score
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/bigdata')
with open('dataset.json', encoding='utf-8') as f:
    papers = []
    for line in f.readlines():
        dic = json.loads(line)
        papers.append(dic)

df = pd.DataFrame(papers)
words = []
for i, row in df.iterrows():
    words.append(row['rev_text'])


vect = CountVectorizer() #将文本转换为数值，构成特征向量
X = vect.fit_transform(words)
X = X.toarray()

words_bag = vect.vocabulary_
#print(words_bag)

mlp = joblib.load('saved_model/rfc.pkl')
y_pred = mlp.predict(X)
print(y_pred)
df['predict'] = list(y_pred)
print(df)
df.to_sql('emotion', engine)

print('write to Mysql table successfully!')