import os
from conf import path
from core.util import queries, topic_path
from core.data import prep_train_feat

from conf import settings


if __name__ == '__main__':

    query_dict = queries(topic_path(settings.corpus))

    if not os.path.exists(path.TRAIN_UWMRGX):
        os.makedirs(path.TRAIN_UWMRGX)

    for num, query in query_dict.items():

        train_feat = path.TRAIN_UWMRGX + str(num)

        prep_train_feat(path.VECT_UWMRGX, num, path.DUMP_UWMRGX, train_feat, path.META_UWMRGX)
