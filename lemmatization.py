import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy2


def human_to_computer(s):
    s = s.lower().replace(u'\xa0', u' ')
    tokens_s = word_tokenize(s)

    stop_words = set(stopwords.words('russian'))
    tokens = [w for w in tokens_s if not w in stop_words]

    morph = pymorphy2.MorphAnalyzer()
    s = []
    for word in tokens:
        p = morph.parse(word)[0]
        s.append(p.normal_form)
    return s
