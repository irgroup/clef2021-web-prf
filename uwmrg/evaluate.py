import os
import core.eval as eval
from core.util import queries, topic_path, qrel_path
from conf import path, settings


if __name__ == '__main__':

    if not os.path.exists(path.SINGLE_UWMRG):
        os.makedirs(path.SINGLE_UWMRG)

    query_dict = queries(topic_path(settings.corpus))

    for num, query in query_dict.items():

        docid_score = path.SCORE_UWMRG + str(num)

        eval.rank(docid_score, str(num), path.SINGLE_UWMRG)

    eval.merge_single_topics(path.SINGLE_UWMRG, path.RUN_UWMRG)
    eval.evaluate(path.TREC_EVAL, qrel_path(settings.corpus), path.RUN_UWMRG)
