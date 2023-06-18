import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from datetime import datetime
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, pairwise_distances
from sklearn.metrics import confusion_matrix
from collections import OrderedDict
import joblib
pd.options.mode.chained_assignment = None
import json

def load_data():
    print("Loading Data from Database")
    with open('fake_dataset.json', encoding='utf-8') as f:
        papers = []
        for line in f.readlines():
            dic = json.loads(line)
            papers.append(dic)

    df = pd.DataFrame(papers)
    print("Data Load Complete")
    #pd.set_option('display.max_columns', 1000)
    #print(df)
    return df


def data_cleaning(df):
    print("Cleaning Data")
    # Removing \n from date field
    for i in range(len(df['date'])):
        if df['date'][i][0] == '\n':
            df['date'][i] = df['date'][i][1:]

    # Making yelpJoinDate Format Uniform
    # df['yelpJoinDate'] = df['yelpJoinDate'].apply(
    #     lambda x: datetime.strftime(datetime.strptime(x, '%B %Y'), '01/%m/%Y'))

    # Removing emtpy cells
    if len(np.where(pd.isnull(df))) > 2:
        # TODO
        pass

    # Pre-processing Text Reviews
    # Remove Stop Words
    stop = stopwords.words('english')
    df['reviewContent'] = df['reviewContent'].apply(
        lambda x: ' '.join(word for word in x.split() if word not in stop))

    # Remove Punctuations
    tokenizer = RegexpTokenizer(r'\w+')
    df['reviewContent'] = df['reviewContent'].apply(
        lambda x: ' '.join(word for word in tokenizer.tokenize(x)))

    # Lowercase Words
    df['reviewContent'] = df['reviewContent'].apply(
        lambda x: x.lower())
    print("Data Cleaning Complete")
    #pd.set_option('display.max_columns', 1000)
    #print(df)
    return df


def feature_engineering(df):
    print("Feature Engineering: Creating New Features")
    # Maximum Number of Reviews per day per reviewer
    mnr_df1 = df[['reviewerID', 'date']].copy()
    mnr_df2 = mnr_df1.groupby(by=['date', 'reviewerID']).size().reset_index(name='mnr')
    mnr_df2['mnr'] = mnr_df2['mnr'] / mnr_df2['mnr'].max()
    df = df.merge(mnr_df2, on=['reviewerID', 'date'], how='inner')

    # Review Length
    df['rl'] = df['reviewContent'].apply(
        lambda x: len(x.split()))

    # Review Deviation
    df['rd'] = abs(df['rating'] - df['restaurantRating']) / 4

    # Maximum cosine similarity
    review_data = df

    res = OrderedDict()

    # Iterate over data and create groups of reviewers
    for row in review_data.iterrows():
        if row[1].reviewerID in res:
            res[row[1].reviewerID].append(row[1].reviewContent)
        else:
            res[row[1].reviewerID] = [row[1].reviewContent]

    individual_reviewer = [{'reviewerID': k, 'reviewContent': v} for k, v in res.items()]
    df2 = dict()
    df2['reviewerID'] = pd.Series([])
    df2['Maximum Content Similarity'] = pd.Series([])
    vector = TfidfVectorizer(min_df=0)
    count = -1
    for reviewer_data in individual_reviewer:
        count = count + 1
        # Handle Null/single review gracefully -24-Apr-2019
        try:
            tfidf = vector.fit_transform(reviewer_data['reviewContent'])
        except:
            pass
        cosine = 1 - pairwise_distances(tfidf, metric='cosine')

        np.fill_diagonal(cosine, -np.inf)
        max = cosine.max()

        # To handle reviewier with just 1 review
        if max == -np.inf:
            max = 0
        df2['reviewerID'][count] = reviewer_data['reviewerID']
        df2['Maximum Content Similarity'][count] = max

    df3 = pd.DataFrame(df2, columns=['reviewerID', 'Maximum Content Similarity'])

    # left outer join on original datamatrix and cosine dataframe -24-Apr-2019
    df = pd.merge(review_data, df3, on="reviewerID", how="left")

    df.drop(index=np.where(pd.isnull(df))[0], axis=0, inplace=True)
    print("Feature Engineering Complete")
    pd.set_option('display.max_columns', 1000)
    print(df)
    return df


def under_sampling(df):
    print("Under-Sampling Data")
    # Count of Reviews
    # print("Authentic", len(df[(df['flagged'] == 'N')]))
    # print("Fake", len(df[(df['flagged'] == 'Y')]))

    sample_size = len(df[(df['flagged'] == 'Y')])

    authentic_reviews_df = df[df['flagged'] == 'N']
    fake_reviews_df = df[df['flagged'] == 'Y']

    authentic_reviews_us_df = authentic_reviews_df.sample(sample_size)
    under_sampled_df = pd.concat([authentic_reviews_us_df, fake_reviews_df], axis=0)

    # print("Under-Sampled Fake", len(under_sampled_df[(under_sampled_df['flagged'] == 'Y')]))
    # print("Under-Sampled Authentic", len(under_sampled_df[(under_sampled_df['flagged'] == 'N')]))

    # Graph of Data Distribution
    # fig, ax = plt.subplots(figsize=(6, 4))
    # sns.countplot(x='flagged', data=under_sampled_df)
    # plt.title("Count of Reviews")
    # plt.show()
    print("Under-Sampling Complete")
    return under_sampled_df


def semi_supervised_test(df, model, algorithm, threshold=0.8, iterations=40):
    df = df.copy()
    print("Testing "+algorithm+" Model")
    df.drop(['reviewerID', 'restaurantID', 'date', 'reviewContent', 'restaurantRating'], axis=1, inplace=True)
    pd.set_option('display.max_columns', 1000)
    print(df)

    model = joblib.load('saved_model/rfc.pkl')
    predicted_labels = model.predict(df)
    print(predicted_labels)
    # print('Best Params : ', grid_clf_acc.best_params_)


def main():
    start_time = time()
    df = load_data()
    df = data_cleaning(df)
    df = feature_engineering(df)
    rf = RandomForestClassifier(random_state=42, criterion='entropy', max_depth=14, max_features='auto',
                                n_estimators=500)
    semi_supervised_test(df, model=rf, threshold=0.7, iterations=15, algorithm='Random Forest')
    end_time = time()
    print("Time taken : ", end_time - start_time)


if __name__ == '__main__':
    main()