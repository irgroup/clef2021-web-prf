import json
import os
from urllib.request import Request, urlopen

import time

from core import nlp
from core import web

from core.util import queries, topic_path

from conf import path, settings


if __name__ == '__main__':

    if not os.path.exists(path.DUMP_UWMRGX):
        os.makedirs(path.DUMP_UWMRGX)

    query_dict = queries(topic_path(settings.corpus), title_only=settings.title_only)

    for num, query in query_dict.items():

        meta_info = {}

        if settings.websearch == 'duck':
            results = web.duck(query)
        if settings.websearch == 'google':
            results = web.google(query)[:10]
        if settings.websearch == 'bing':
            results = web.bing(query)[:10]

        count = 0

        complete_text = ''

        for result in results:

            name = result.title
            description = result.snippet

            text = name + " " + description + " "

            trec_words = ['Description:', 'Narrative:', 'Number:']

            if not any(term in description for term in trec_words):

                words = nlp.remove_punctuation(text)

                text_filter = nlp.remove_stop_words(words)

                text_stem = nlp.stem_raw_text(text_filter)

                text_tok = nlp.remove_num(text_stem)

                text = ' '.join(text_tok)

                complete_text += ' ' + text

                meta_info[count] = [result.url, description]

                count += 1

        if not os.path.exists(path.DUMP_UWMRGX + str(num)):
            os.makedirs(path.DUMP_UWMRGX + str(num))

        with open(path.DUMP_UWMRGX + str(num) + '/' + str(num), 'w') as out:
            out.write(complete_text)

        if not os.path.exists(path.META_UWMRGX + 'dump/'):
            os.makedirs(path.META_UWMRGX + 'dump/')

        with open(path.META_UWMRGX + 'dump/' + str(num), 'w') as meta:
            meta.write(json.dumps(meta_info, indent=4, sort_keys=True))

        count += 1
        time.sleep(60)
