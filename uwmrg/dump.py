import os
import time
import json

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from core import web
from core.util import queries, topic_path
from conf import path, settings


if __name__ == '__main__':

    if not os.path.exists(path.DUMP_UWMRG):
        os.makedirs(path.DUMP_UWMRG)

    query_dict = queries(topic_path(settings.corpus), title_only=settings.title_only)

    for num, query in query_dict.items():

        if settings.websearch == 'duck':
            results = web.duck(query)
            urls = [result.url for result in results]
        if settings.websearch == 'google':
            results = web.google(query)
            urls = [result.url for result in results]
        if settings.websearch == 'bing':
            results = web.bing(query)
            urls = [result.url for result in results]

        meta_info = {}

        count = 0
        for url in urls:

            if url is not None and count < 10:

                head = {'User-Agent': 'Mozilla/5.0'}

                req = Request(url, headers=head)

                try:
                    page = urlopen(req, timeout=2)

                    soup = BeautifulSoup(page, 'lxml')

                    if not os.path.exists(path.DUMP_UWMRG + str(num)):
                        os.makedirs(path.DUMP_UWMRG + str(num))

                    with open(path.DUMP_UWMRG + str(num) + '/' + str(count) + '.html', 'w') as out:
                        out.write(str(soup))
                        meta_info[count] = url
                        count += 1

                except Exception as e:
                    print('Could not dump page...')

        with open(path.DUMP_UWMRG + str(num) + '/meta', 'w') as meta:
            meta.write(json.dumps(meta_info, indent=4, sort_keys=True))

        time.sleep(60)
