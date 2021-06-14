from bs4 import BeautifulSoup
import os

from core.util import queries, topic_path

from conf import path, settings
from core import nlp

if __name__ == '__main__':

    if not os.path.exists(path.DUMP_UWMRG):
        os.makedirs(path.DUMP_UWMRG)

    query_dict = queries(topic_path(settings.corpus))

    for num, query in query_dict.items():

        count = 0
        while count < 10:

            with open(path.DUMP_UWMRG + str(num) + '/' + str(count) + '.html', 'r') as input:
                raw = input.read()

            soup = BeautifulSoup(raw, 'lxml')

            for script in soup(["script", "style", "a"]):
                script.decompose()

            text = soup.get_text()

            trec_words = ['Description:', 'Narrative:', 'Number:']

            if not any(term in text for term in trec_words):

                if not os.path.exists(path.PARSE_UWMRG + str(num)):
                    os.makedirs(path.PARSE_UWMRG + str(num))

                words = nlp.remove_punctuation(text)

                text_filter = nlp.remove_stop_words(words)

                text_stem = nlp.stem_raw_text(text_filter)

                text_no_num = nlp.remove_num(text_stem)

                text_tok = [token for token in text_no_num if (2 < len(token) < 20)]

                text = ' '.join(text_tok)

                with open(path.PARSE_UWMRG + str(num) + '/' + str(count), 'w') as out:
                    out.write(text)
                    count += 1