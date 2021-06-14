import os
import shelve
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_svmlight_file

from multiprocessing import Pool, cpu_count
import functools

from conf import settings


def train(train_feat, topic, n_feat, model_type='logreg-scikit'):
    '''Use this function to train a logistic regression model with the help of a provided svm-light file.
    :param train_feat: the previously derived tfidf training features (svm-light formatted)
    :param topic: topic number
    :param n_feat: number of features (returned by prep_train_feat())
    :param model_type: define type of model, choose from 'logreg-scikit', 'logreg-sofia' and 'svm-scikit'
    :return: model which results from the training
    '''
    x_train, y_train = load_svmlight_file(train_feat, n_features=n_feat)

    if model_type == 'logreg-scikit':
        model = LogisticRegression(max_iter=settings.max_iter,
                                   solver=settings.logreg_solver,
                                   C=settings.C,
                                   tol=settings.tol)
        model.fit(x_train, y_train)

    return model


def predict(model, corpus_feat, corpus_score):
    '''Use this function to predict the tfidf-features from a corpus.
    :param model: the previously trained logistic regression model
    :param corpus_feat: the tfidf-features of a corpus stored in a shelve
    :param corpus_score: path to directory where scores of a topic run will be written
    :return: -
    '''

    id_and_tfidf = shelve.open(corpus_feat)

    file = open(corpus_score, 'w')

    for key in id_and_tfidf:
        doc_tfidf = id_and_tfidf[key]
        score = model.predict_proba(doc_tfidf)[0][1]
        file.write(key + " " + str(score) + "\n")

    id_and_tfidf.close()
    file.close()


def _parallel_train_predict(num, n_feat, corpus_feat, train_path, score_path):

    train_feat = train_path + str(num)
    clf = train(train_feat, num, n_feat, model_type=settings.model_type)
    corpus_score = score_path + str(num)
    predict(clf, corpus_feat, corpus_score)


def score(score_dir, query_dict, n_feat, corpus_feat, train_path, score_path):

    if not os.path.exists(score_dir):
        os.makedirs(score_dir)

    # cores = cpu_count()
    cores = settings.num_cpu
    p = Pool(cores)
    p.map(functools.partial(_parallel_train_predict,
                            n_feat=n_feat,
                            corpus_feat=corpus_feat,
                            train_path=train_path,
                            score_path=score_path),
          query_dict.keys())
