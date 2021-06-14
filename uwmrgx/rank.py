import os
import json
import time

from core.util import queries, topic_path
from core.clf import score

from conf import path, settings

if __name__ == '__main__':

    if not os.path.exists(path.SCORE_UWMRGX):
        os.makedirs(path.SCORE_UWMRGX)

    n_feat = 0
    with open(path.META_UWMRGX, 'r') as meta:
        text = meta.read()
        n_feat = json.loads(text)['feature-length']

    query_dict = queries(topic_path(settings.corpus))

    start_time = time.time()
    score(path.SCORE_UWMRGX, query_dict, n_feat, path.FEAT_UWMRGX, path.TRAIN_UWMRGX, path.SCORE_UWMRGX)
    print('Took ', time.time() - start_time, ' seconds.')


