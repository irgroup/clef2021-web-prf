from conf import path
from core.data import dump_tfidf_vectorizer

if __name__ == '__main__':

    dump_tfidf_vectorizer(path.VECT_UWMRG, path.PARSE_UWMRG)
