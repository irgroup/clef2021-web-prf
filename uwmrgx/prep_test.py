from conf import path, settings
from core.data import prepare_corpus_feature
from core.util import corpus_path

if __name__ == '__main__':
    prepare_corpus_feature(path.VECT_UWMRGX, corpus_path(settings.corpus), path.FEAT_UWMRGX)
