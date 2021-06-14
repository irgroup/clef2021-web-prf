import collections
import subprocess
import pandas as pd
from io import StringIO

from core.util import directory_list


def rank(docid_score, topic, path_single_runs):
    ''' This function will rank entries of a given file with doc-ids and corresponding scores.
    Afterwards a run file with the 10,000 first entries will be written for the specified topic.
    :param docid_score: path to directory where scores of a topic run will be written
    :param topic: topic number
    :param path_single_runs: path to directory where resulting single runs will be written
    :return: -
    '''
    print('Producing run...')

    run_file_name = path_single_runs + str(topic)

    scores = pd.read_csv(docid_score, delimiter='\s+', names=['docid', 'scores'])
    score_dict = {row[0]: row[1] for row in scores.values}
    sort = sorted(score_dict.items(), key=lambda kv: kv[1])
    sorted_dict = collections.OrderedDict(sort)
    run = ''

    for i in range(0, 10000):  # Grossman et al. use the first 10,000 entries to produce their runs

        doc_and_score = sorted_dict.popitem()
        docid = doc_and_score[0]

        if isinstance(docid, float):
            docid = str(int(docid))
        else:
            docid = str(docid)

        score = doc_and_score[1]
        run += str(topic) + " " + "Q0" + " " + docid + " " + str(i) + " " + str(score) + " " + "IRC" + "\n"

    with open(run_file_name, "w") as output:
        output.write(run)


def merge_single_topics(dir_single_runs, run_complete):
    '''This function will merge runs from single topics to one single run file.
    :param dir_single_runs: path to directory where resulting single runs will be written
    :param run_complete: path to directory where resulting complete run will be written
    :return: -
    '''
    files = directory_list(dir_single_runs)

    with open(run_complete, 'w') as outfile:
        for file in files:
            with open(file) as infile:
                for line in infile:
                    outfile.write(line)


def evaluate(trec_eval, corpus_qrel, run_file_name):
    '''This function will call trec_eval.
    :param trec_eval: path to compiled trec_eval
    :param corpus_qrel: path to qrel-file
    :param run_file_name: path to run file
    :return: -
    '''
    print("Evaluate run...")
    output = subprocess.run([trec_eval + ' ' + corpus_qrel + ' ' + run_file_name], shell=True)
    print(output)


def trec_eval_to_dict(trec_eval_output, topics=None):
    '''This function will parse the trec_eval output (taken from a subprocess call) to a python dictionary.
    :param trec_eval_output: output taken from subprocess call
    :param topics: list with topics which should be considered
    :return: dictionary with trec_eval results
    '''
    output_text = StringIO(str(trec_eval_output.stdout, 'utf-8'))

    df = pd.read_csv(output_text, sep='\t', names=['measure', 'topic', 'value'])

    if topics is None:
        topics = df['topic'].unique()

    trec_eval_result = {}

    for topic in topics:

        tmp_dict = {}

        topic_result = df.loc[df['topic'] == str(topic)]

        for i in range(0, len(topic_result)):
            measure = topic_result.iloc[i, 0].split()[0]
            value = topic_result.iloc[i, 2]
            tmp_dict[measure] = value

        trec_eval_result[str(topic)] = tmp_dict

    return trec_eval_result


def inter_topic(qrel_files):
    '''This function will find intersecting topics between two or more qrel files.
    :param qrel_files: list containing path to two or more qrel-files
    :return: list with intersecting topics
    '''
    qrel_ids = []

    for file in qrel_files:
        qrel = pd.read_csv(file, delimiter='\s+')
        unique = qrel.iloc[:, 0].unique()
        id = pd.Index(unique)
        qrel_ids.append(id)

    if len(qrel_ids) != 0:
        inter = qrel_ids[0]

        for i in range(1, len(qrel_ids)):
            inter = inter.intersection(qrel_ids[i])

        return inter

    else:
        print("No topics found ...")
        return None