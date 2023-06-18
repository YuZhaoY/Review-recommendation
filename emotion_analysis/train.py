import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib
from sklearn.metrics import accuracy_score


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

y = df['rev_class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
print("开始训练")
mlp = MLPClassifier()
mlp.fit(X_train, y_train)
joblib.dump(mlp, 'saved_model/rfc.pkl')

#mlp = joblib.load('saved_model/rfc.pkl')
y_pred = mlp.predict(X_test)
print(y_pred)
a = pd.DataFrame()  #创建一个空的DataFrame
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
print(a)#查看我们创建的DataFrame
# score = accuracy_score(y_pred, y_test)
#
# print(score)