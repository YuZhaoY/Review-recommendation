# encoding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

df = pd.read_csv("test.csv", encoding='utf-8')
df=df.head(5000)
x = df[["text"]]

words = []
stop_words = open("stop_words.txt", "r", encoding='utf-8', errors='ignore').read()

for row in x.values:
    txt = str(row).lower()
    for ch in '!"#$&()*+,-./\:;<=>?@[\\]^_{|}·~‘’1234567890':
        txt = txt.replace(ch, "")
    word = txt.split()
    for ch in word:
        if ch in stop_words:
            word.remove(ch)
    result = '  '.join(word)
    words.append(result)


from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()  # 将文本转换为数值，构成特征向量
X = vect.fit_transform(words)
X = X.toarray()

words_bag = vect.vocabulary_

pd.DataFrame(X)  # 为了更好地查看X,将其转换成DataFrame

from sklearn.cluster import KMeans
SSE = []
for i in range(100, 900, 100):
    kmeans=KMeans(n_clusters=i, random_state=123)
    kmeans.fit(X)
    SSE.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(100, 900, 100), SSE, linewidth=2, linestyle='-')
plt.show()
# estimator = KMeans(n_clusters=500, max_iter=400)
# estimator.fit(X)
# label_pred = estimator.labels_  # 获取聚类标签
# centroids = estimator.cluster_centers_  # 获取聚类中心
# inertia = estimator.inertia_  # 获取聚类准则的总和