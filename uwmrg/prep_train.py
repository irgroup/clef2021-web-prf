import os
from core.util import queries, topic_path
from core.data import prep_train_feat
from conf import path

from conf import settings

if __name__ == '__main__':

    query_dict = queries(topic_path(settings.corpus))

    if not os.path.exists(path.TRAIN_UWMRG):
        os.makedirs(path.TRAIN_UWMRG)

    for num, query in query_dict.items():
        train_feat = path.TRAIN_UWMRG + str(num)
        prep_train_feat(path.VECT_UWMRG, num, path.PARSE_UWMRG, train_feat, path.META_UWMRG)