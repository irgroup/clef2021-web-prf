import os
import json

from core.util import queries, topic_path
from core.clf import score

from conf import path, settings

if __name__ == '__main__':

    if not os.path.exists(path.SCORE_UWMRG):
        os.makedirs(path.SCORE_UWMRG)

    n_feat = 0
    with open(path.META_UWMRG, 'r') as meta:
        text = meta.read()
        n_feat = json.loads(text)['feature-length']

    query_dict = queries(topic_path(settings.corpus))

    score(path.SCORE_UWMRG, query_dict, n_feat, path.FEAT_UWMRG, path.TRAIN_UWMRG, path.SCORE_UWMRG)


