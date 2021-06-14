import os
import core.eval as eval
from conf import path
from core.util import queries, topic_path, qrel_path

from conf import settings


if __name__ == '__main__':

    if not os.path.exists(path.SINGLE_UWMRGX):
        os.makedirs(path.SINGLE_UWMRGX)

    query_dict = queries(topic_path(settings.corpus))

    for num, query in query_dict.items():

        docid_score = path.SCORE_UWMRGX + str(num)

        eval.rank(docid_score, str(num), path.SINGLE_UWMRGX)

    eval.merge_single_topics(path.SINGLE_UWMRGX, path.RUN_UWMRGX)
    eval.evaluate(path.TREC_EVAL, qrel_path(settings.corpus), path.RUN_UWMRGX)
