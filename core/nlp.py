from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import re


def remove_punctuation(raw_text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(raw_text)

    return words


def remove_stop_words(words):
    stop_words = set(stopwords.words('english'))
    text_filter = []
    for w in words:
        if w.lower() not in stop_words:
            text_filter.append(w.lower())

    return text_filter


def stem_raw_text(text_filter):
    stemmer = PorterStemmer()
    text_stem = [stemmer.stem(word) for word in text_filter]

    return text_stem


def remove_num(text_stem):
    return [re.sub(r'\d+', '', stem) for stem in text_stem]