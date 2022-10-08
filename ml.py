import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
# pip install pandas
# pip install sklearn



accounter_df = pd.read_csv(f'AC_important.csv')

gendir_df = pd.read_csv(f'GD_important.csv')


def learning(df):
    df = df.dropna()
    X = df['human_text']
    y = df['rating']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    sgd_ppl_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('sgd_clf', SGDClassifier(random_state=42))])
    knb_ppl_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('knb_clf', KNeighborsClassifier(n_neighbors=10))])
    sgd_ppl_clf.fit(X_train, y_train)
    knb_ppl_clf.fit(X_train, y_train)
    return sgd_ppl_clf


model_accounter = learning(accounter_df)
model_gendir = learning(gendir_df)


def prediction_for_acc(text_news):
    ans = model_accounter.predict(text_news)
    return ans


def prediction_for_gd(text_news):
    ans = model_gendir.predict(text_news)
    return ans
