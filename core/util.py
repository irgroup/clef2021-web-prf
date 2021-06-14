import os
import re
import pickle

from bs4 import BeautifulSoup

from conf import path


def qrel_path(corpus):
    switcher = {
        'wapo': path.WAPO_QRELS,
        'nyt': path.NYT_QRELS,
        'rob04': path.ROB04_QRELS,
        'rob05': path.ROB05_QRELS
    }
    return switcher.get(corpus)


def corpus_path(corpus):
    switcher = {
        'wapo': path.WAPO_CLEAN,
        'nyt': path.NYT_CLEAN,
        'rob04': path.ROB04_CLEAN,
        'rob05': path.ROB05_CLEAN
    }
    return switcher.get(corpus)


def topic_path(corpus):
    switcher = {
        'wapo': path.WAPO_TOPICS,
        'nyt': path.NYT_TOPICS,
        'rob04': path.ROB04_TOPICS,
        'rob05': path.ROB05_TOPICS
    }
    return switcher.get(corpus)


def directory_list(directory):
    '''This function will return a list of files in a directory.
    :param directory: path to directory
    :return: list with paths to files
    '''
    dirlist = []
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            dirlist.append(os.path.abspath(os.path.join(dirpath, f)))

    return dirlist


def queries(topics, title_only=False):
    # TODO: distinct between query types (title, title+desc, ...)
    query_dict = {}

    with open(topics) as topic_file:
        text = topic_file.read()
        soup = BeautifulSoup(text, 'lxml')

        tops = soup.find_all('top')

        for top in tops:
            num_txt = top.num.text

            num = int(re.findall(r'\d{3}', top.num.text)[0])

            title = top.title.text.strip()

            desc = top.desc.text.strip().replace('Description:\n', '')
            desc = desc.strip().replace('Description:', '')
            desc = desc.strip().replace('\n', '')

            if title_only:
                query = title  # + ' -pdf -doc -docx'
            else:
                query = title + ' ' + desc  # + ' -pdf -doc -docx'

            query_dict.update({num: query})

        return query_dict


def load_vectorizer(vectorizer_pick):
    '''Use this function to load a vectorizer object from a pickle file.
    :param vectorizer_pick: path to file where tfidf-vectorizer are dumped
    :return: -
    '''
    print('Loading tfidf-vectorizer...')
    vectorizer_file = open(vectorizer_pick, 'rb')
    vectorizer = pickle.load(vectorizer_file)

    return vectorizer


def add_closing_tag(i, o):

    with open(i, 'r') as topic:
        lines = topic.readlines()

        for i in range(0, len(lines)):
            if '<title>' in lines[i]:
                lines[i] = '</num>' + lines[i]
            if '<desc>' in lines[i]:
                lines[i] = '</title>' + lines[i]
            if '<narr>' in lines[i]:
                lines[i] = '</desc>' + lines[i]
            if '</top>' in lines[i]:
                lines[i] = '</narr>' + lines[i]

        with open(o, 'w') as out:
            for line in lines:
                out.write(line)
