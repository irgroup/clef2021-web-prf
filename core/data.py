import json
import functools
import shutil
from multiprocessing import Pool, cpu_count
from bs4 import BeautifulSoup

import core.nlp as nlp
from core.util import load_vectorizer, directory_list

from sklearn.feature_extraction.text import TfidfVectorizer


import os
import time
import shelve

from tqdm import tqdm

from sklearn.datasets import dump_svmlight_file
from scipy.sparse import vstack, csr_matrix

import numpy as np

import pickle

from conf import settings


def _extract_times(file, extraction_dir):
    os.system("tar -xzf " + str(file) + " -C " + extraction_dir)


def _parse_times(file, raw_text_dir):

    markup = open(file, 'r')
    try:
        text = markup.read()
    except Exception as e:
        print("BS4 cannot read file: " + file)

    soup = BeautifulSoup(text, "lxml")

    raw_text = soup.text

    if file[-11:] == '0000000.xml':  # consider special case for first document
        write_name = '0'
    else:
        write_name = file[-11:-4].lstrip("0")

    dst = raw_text_dir + write_name
    with open(dst, 'w') as output:
        output.write(raw_text)


def raw_text_from_times(times_data, extraction_dir, raw_text_dir):
    '''This function will decompress NYT files and write single files containing texts of the documents.
    :param times_data: path to compressed files from New York Times corpus
    :param extraction_dir: path for temporal directory; this folder will be deleted after successful execution
    :param raw_text_dir: path to raw text-docs from New York Times corpus
    :return: -
    '''

    if not os.path.exists(extraction_dir):
        os.makedirs(extraction_dir)

    # cores = cpu_count()
    cores = settings.num_cpu
    p = Pool(cores)

    # Uncompress files
    print("Extracting files")

    full_path = []
    for path, subdirs, files in os.walk(times_data):

        extensions = tuple([".tgz"])
        files = [fi for fi in files if fi.endswith(extensions)]
        for fi in files:
                full_path.append(os.path.join(path, fi))

    p.map(functools.partial(_extract_times, extraction_dir=extraction_dir), full_path)

    # Write raw text content
    print("Extracting raw text")

    full_path = []
    for path, subdirs, files in os.walk(extraction_dir):

        extensions = tuple([".xml"])
        files = [fi for fi in files if fi.endswith(extensions)]
        for fi in files:
                full_path.append(os.path.join(path, fi))

    p.map(functools.partial(_parse_times, raw_text_dir=raw_text_dir), full_path)

    shutil.rmtree(extraction_dir, ignore_errors=True)


def _parse_trec(full_path_file, tmp, dir_raw_txt):

    skip_list = [
        'credtd.z',
        'crhdtd.z',
        'fr94dtd.z',
        'ftdtd.z',
        'readfrcg.z',
        'readmeft.z',
        'readchg.z',
        'readmefr.z'
    ]

    name = os.path.basename(os.path.normpath(full_path_file))

    if name not in skip_list:

        if name.endswith(tuple([".0z", ".1z", ".2z"])):
            end = '_' + os.path.splitext(name)[1][1]
            doc_path_tmp = tmp + name[:-3] + end
            ending = name[-3:]
            os.system("gzip -d -k -S " + ending + " " + full_path_file)
            os.system("mv " + full_path_file[:-3] + " " + doc_path_tmp)
        if name.endswith(".z"):
            doc_path_tmp = tmp + name[:-2]
            os.system("gzip -d -k " + full_path_file)
            os.system("mv " + full_path_file[:-2] + " " + doc_path_tmp)
        if name.endswith(".gz"):
            doc_path_tmp = tmp + name[:-3]
            os.system("gzip -d -k " + full_path_file)
            os.system("mv " + full_path_file[:-3] + " " + doc_path_tmp)

        markup = open(doc_path_tmp, 'r', encoding="ISO-8859-1")
        try:
            text = markup.read()
        except Exception as e:
            print("BS4 cannot read file: " + doc_path_tmp)

        soup = BeautifulSoup(text, "lxml")
        findings = soup.find_all("doc")

        for finding in findings:
            try:
                # .split() is necessary to remove whitespaces in file names
                file_name = finding.find("docno").contents[0].split()[0]
                output = open(tmp + file_name, "w")
                output.write(str(finding))
                output.close()
            except Exception as e:
                print("Cannot extract document: " + file_name)

            try:
                file = open(tmp + file_name, 'r')
                text = file.read()
                soup = BeautifulSoup(text, "lxml")

                docno = soup.find("docno").contents[0].split()[0]

                completetext = ''

                if soup.find('headline') is not None:
                    completetext += soup.find('headline').text

                if soup.find('text') is not None:

                    try:
                        if len(soup.find('text').contents) == 1:
                            completetext = soup.find("text").text

                        else:  # else-case for documents from la-times
                            for content in soup.find('text').contents:
                                try:

                                    raw_txt = BeautifulSoup(str(content), "lxml")
                                    completetext += raw_txt.text
                                except Exception as e:
                                    pass

                    except Exception as e:
                        print("Could not write raw text for file: ", tmp + name[:-2])

                if soup.find('graphic') is not None:
                    completetext += soup.find('graphic').text

                if soup.find('dateline') is not None:
                    completetext += soup.find('dateline').text

                if soup.find('correction') is not None:
                    completetext += soup.find('correction').text

                if completetext != '':
                    with open(dir_raw_txt + docno, "w") as output:
                        output.write(completetext)

                else:
                    print('No text in file found: ' + docno)

            except Exception as e:
                print("Could not open file with name: ", name[:-2])


def raw_text_from_trec(trec_data, tmp, dir_raw_txt):
    '''This function will decompress TREC files and write single files containing texts of the documents.
    :param trec_data: path to compressed files of TREC disks 4 and 5
    :param tmp: path to temporal directory for uncompressed files, will be deleted afterwards
    :param dir_raw_txt: path to directory where single raw text document files will be written
    :return: -
    '''
    print("Extracting documents from compressed TREC files.")

    if not os.path.exists(tmp):
        os.makedirs(tmp)

    if not os.path.exists(dir_raw_txt):
        os.makedirs(dir_raw_txt)

    # cores = cpu_count()
    cores = settings.num_cpu
    p = Pool(cores)

    exclude = set(['cr'])

    full_path = []
    for path, subdirs, files in os.walk(trec_data):

        subdirs[:] = [s for s in subdirs if s not in exclude]

        extensions = tuple([".z", ".0z", ".1z", ".2z", ".gz"])
        files = [fi for fi in files if fi.endswith(extensions)]
        for fi in files:
            full_path.append(os.path.join(path, fi))

    p.map(functools.partial(_parse_trec, tmp=tmp, dir_raw_txt=dir_raw_txt), full_path)

    shutil.rmtree(tmp, ignore_errors=True)


def raw_text_from_wapo(wapo_jl, wapo_raw):
    '''This function will read from the JSON lines file and write single files containing texts of the documents.
    :param wapo_jl: path to json lines file of Washington Post corpus
    :param wapo_raw: path to raw text-docs from Washington Post corpus
    :return: -
    '''
    if not os.path.exists(wapo_raw):
        os.makedirs(wapo_raw)

    with open(wapo_jl, 'r') as f:
        for line in f:
            obj = json.loads(line)
            with open(wapo_raw + obj['id'], "w") as output:
                text = ""
                for content in obj['contents']:
                    try:
                        con = content.get('content')
                        if con is not None:
                            try:
                                soup = BeautifulSoup(con, 'lxml')
                                text += soup.text
                                text += '\n'
                            except Exception as e:
                                pass # soup may not have text
                    except Exception as e:
                        print("Beautifulsoup cannot get content for: ", obj['id'])

                if text != '':
                    output.write(text)
                else:
                    print("No text found...")


def _clean(name, input, output, wapo):
    if wapo:
        raw_text = open(input + name, 'r').read()
    else:
        raw_text = open(input + name, 'r', encoding="ISO-8859-1").read()
    words = nlp.remove_punctuation(raw_text)
    text_filter = nlp.remove_stop_words(words)
    text_stem = nlp.stem_raw_text(text_filter)
    text = nlp.remove_num(text_stem)

    with open(output + name, 'w') as output:
        for content in text:
            output.write(content + " ")


def clean_raw_text(corpus_raw, corpus_clean, wapo=False):
    '''Use this function for the removal of punctuation, stop words and for stemming words.
    :param corpus_raw: path to raw text-docs from corpus
    :param corpus_clean: path to cleaned text-docs from corpus
    :param wapo: boolean indicating whether the Washington Post corpus will be processed
    :return: -
    '''
    print("Starting parallel text cleaning.")
    # cores = cpu_count()
    cores = settings.num_cpu
    p = Pool(cores)
    p.map(functools.partial(_clean, input=corpus_raw, output=corpus_clean, wapo=wapo), os.listdir(corpus_raw))


def prepare_corpus_feature(vectorizer_pick, corpus, corpus_feat):
    '''Use this function to precompute tfidf-features from single documents of corpus.
    :param vectorizer_pick: path to dumped tfidf-vectorizer
    :param corpus: path to corpus with (cleaned) text document files
    :param corpus_feat: path to shelve where tf-idf-features are dumped
    :return: -
    '''

    # Load tfidf-vectorizer
    vectorizer = load_vectorizer(vectorizer_pick)

    # Prediciton
    print('Retrieving tfidf-features for corpus...')
    start_time = time.time()
    id_and_tfidf = shelve.open(corpus_feat)

    for path, subdirs, files in os.walk(corpus):

        t = tqdm(total=len(files))
        for file in files:
            docpath = path + file
            doc_tfidf = vectorizer.transform([docpath], copy=True)
            id_and_tfidf[file] = doc_tfidf
            t.update()

    t.close()
    id_and_tfidf.close()

    print('Took ', time.time() - start_time, ' seconds.')


def prep_train_feat(vectorizer_pick, topic, corpus, train_feat, meta_path):
    '''This function will prepare features in svm-light format for the training of the logistic regression model.
    Training will be done on a specified topic with documents from a selected corpus.
    :param vectorizer_pick: path to file where tfidf-vectorizer will be dumped
    :param qrel: path to qrel file from which tfidf-features are picked
    :param topic: topic number
    :param training_corpus: path to corpus from which tfidf-features are computed
    :param train_feat: path to svmlight-file
    :return: the number of tfidf-features has to be returned in order to hand it over in a subsequent step
    '''
    print("Preparing training features.")
    vectorizer = load_vectorizer(vectorizer_pick)

    y = []
    tfidf = csr_matrix([])

    init = 1

    for file in directory_list(corpus):

        try:
            doc_tfidf = vectorizer.transform([file])
            if init == 1:
                tfidf = vstack([doc_tfidf])
                with open(meta_path, 'w') as meta:
                    meta.write(json.dumps({'feature-length': tfidf.shape[1]}))
                init = 0
            else:
                tfidf = vstack([tfidf, doc_tfidf])

            if str(topic) in file.split('/'):
                y.append(1)
            else:
                y.append(0)
        except Exception as e:
            print("Could not convert text to numeric.")

    dump_svmlight_file(tfidf, np.array(y), train_feat, multilabel=False)


def dump_tfidf_vectorizer(vectorizer_pick, union):
    '''Use this function to pickle a vectorizer object. The tfidf-vectorizer object will be made from
    files of a specified directory.
    :param vectorizer_pick: path to file where pickled vectorizer will be written
    :param union: path to directory of union corpus
    :return: -
    '''

    print('Dumping tfidf-vectorizer')
    union_list = directory_list(union)
    vectorizer = TfidfVectorizer(input='filename',
                                 sublinear_tf=settings.sublinear_tf,
                                 analyzer=settings.analyzer,
                                 ngram_range=settings.ngram_range,
                                 max_df=settings.max_df,
                                 min_df=settings.min_df,
                                 max_features=settings.max_features,
                                 binary=settings.binary,
                                 norm=settings.norm,
                                 use_idf=settings.use_idf,
                                 smooth_idf=settings.smooth_idf
                                 )
    start_time = time.time()
    vectorizer.fit(union_list)
    print("Time needed for making tfidf-matrix: ", str(time.time() - start_time))

    with open(vectorizer_pick, 'wb') as dump:
        pickle.dump(vectorizer, dump)
