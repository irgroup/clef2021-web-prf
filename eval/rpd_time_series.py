from repro_eval.Evaluator import RpdEvaluator
import os
import json
from rbo import rbo
import pandas as pd
import numpy as np
import pytrec_eval
from repro_eval.util import trim
from matplotlib import pyplot as plt
import seaborn as sns

sns.set()
sns.set_style('ticks')
palette = sns.color_palette("GnBu_d")
# palette = sns.color_palette(sns.color_palette("coolwarm", 7))
sns.set_palette(palette)
colors = sns.color_palette()


def main():


    urls = {}

    REF = '20200607'

    dates = ['20200607',
             '20200609',
             '20200611',
             '20200613',
             '20200615',
             '20200617',
             '20200619']

    for date in dates:

        folder_path = os.path.join('./data/runs/time-series/', date, 'scrape/uwmrg_ddg/dump')
        topic_dirs = [p[0] for p in os.walk(folder_path) if p[0] != folder_path]

        topic_dict = {}
        for td in topic_dirs:
            topic = os.path.basename(td)
            with open(os.path.join(td, 'meta')) as json_in:
                meta = json.loads(json_in.read())
                topic_dict[topic] = list(meta.values())

        urls[date] = topic_dict


    rbos = {}
    rbos_avg = {}

    for d, t in urls.items():
        tmp = {}
        for topic, u in t.items():

            tmp[topic] = rbo(u, urls[REF][topic], p=0.9).ext

        rbos[d] = tmp


    for d, topic_rbos in rbos.items():
        rbos_avg[d] = np.array(list(topic_rbos.values())).mean()



    ######### GOOGLE

    urls = {}

    REF = '20200607'

    dates = ['20200607',
             '20200609',
             '20200611',
             '20200613',
             '20200615',
             '20200617',
             '20200619']

    for date in dates:

        folder_path = os.path.join('./data/runs/time-series/', date, 'scrape/uwmrg_google/dump')
        topic_dirs = [p[0] for p in os.walk(folder_path) if p[0] != folder_path]

        topic_dict = {}
        for td in topic_dirs:
            topic = os.path.basename(td)
            with open(os.path.join(td, 'meta')) as json_in:
                meta = json.loads(json_in.read())
                topic_dict[topic] = list(meta.values())

        urls[date] = topic_dict


    rbos = {}
    rbos_avg_google = {}

    for d, t in urls.items():
        tmp = {}
        for topic, u in t.items():

            tmp[topic] = rbo(u, urls[REF][topic], p=0.9).ext

        rbos[d] = tmp


    for d, topic_rbos in rbos.items():
        rbos_avg_google[d] = np.array(list(topic_rbos.values())).mean()


    ########### RMSE, RBO, NDCG




    QREL = './data/qrels/core18.txt'
    ORIG_B = './data/runs/orig/uwmrg'
    # ORIG_A = './data/runs/orig/uwmrg'

    runs = {
        '20200607_umwrg_google': {
            'path': './data/runs/time-series/20200607/run/uwmrg_google/uwmrg'},
        '20200607_umwrg_ddg': {
            'path': './data/runs/time-series/20200607/run/uwmrg_ddg/uwmrg'},
        '20200609_umwrg_google': {
            'path': './data/runs/time-series/20200609/run/uwmrg_google/uwmrg'},
        '20200609_umwrg_ddg': {
            'path': './data/runs/time-series/20200609/run/uwmrg_ddg/uwmrg'},
        '20200611_umwrg_google': {
            'path': './data/runs/time-series/20200611/run/uwmrg_google/uwmrg'},
        '20200611_umwrg_ddg': {
            'path': './data/runs/time-series/20200611/run/uwmrg_ddg/uwmrg'},
        '20200613_umwrg_google': {
            'path': './data/runs/time-series/20200613/run/uwmrg_google/uwmrg'},
        '20200613_umwrg_ddg': {
            'path': './data/runs/time-series/20200613/run/uwmrg_ddg/uwmrg'},
        '20200615_umwrg_google': {
            'path': './data/runs/time-series/20200615/run/uwmrg_google/uwmrg'},
        '20200615_umwrg_ddg': {
            'path': './data/runs/time-series/20200615/run/uwmrg_ddg/uwmrg'},
        '20200617_umwrg_google': {
            'path': './data/runs/time-series/20200617/run/uwmrg_google/uwmrg'},
        '20200617_umwrg_ddg': {
            'path': './data/runs/time-series/20200617/run/uwmrg_ddg/uwmrg'},
        '20200619_umwrg_google': {
            'path': './data/runs/time-series/20200619/run/uwmrg_google/uwmrg'},
        '20200619_umwrg_ddg': {
            'path': './data/runs/time-series/20200619/run/uwmrg_ddg/uwmrg'},

        '20200607_umwrgx_google': {
            'path': './data/runs/time-series/20200607/run/uwmrgx_google/uwmrgx'},
        '20200607_umwrgx_ddg': {
            'path': './data/runs/time-series/20200607/run/uwmrgx_ddg/uwmrgx'},
        '20200609_umwrgx_google': {
            'path': './data/runs/time-series/20200609/run/uwmrgx_google/uwmrgx'},
        '20200609_umwrgx_ddg': {
            'path': './data/runs/time-series/20200609/run/uwmrgx_ddg/uwmrgx'},
        '20200611_umwrgx_google': {
            'path': './data/runs/time-series/20200611/run/uwmrgx_google/uwmrgx'},
        '20200611_umwrgx_ddg': {
            'path': './data/runs/time-series/20200611/run/uwmrgx_ddg/uwmrgx'},
        '20200613_umwrgx_google': {
            'path': './data/runs/time-series/20200613/run/uwmrgx_google/uwmrgx'},
        '20200613_umwrgx_ddg': {
            'path': './data/runs/time-series/20200613/run/uwmrgx_ddg/uwmrgx'},
        '20200615_umwrgx_google': {
            'path': './data/runs/time-series/20200615/run/uwmrgx_google/uwmrgx'},
        '20200615_umwrgx_ddg': {
            'path': './data/runs/time-series/20200615/run/uwmrgx_ddg/uwmrgx'},
        '20200617_umwrgx_google': {
            'path': './data/runs/time-series/20200617/run/uwmrgx_google/uwmrgx'},
        '20200617_umwrgx_ddg': {
            'path': './data/runs/time-series/20200617/run/uwmrgx_ddg/uwmrgx'},
        '20200619_umwrgx_google': {
            'path': './data/runs/time-series/20200619/run/uwmrgx_google/uwmrgx'},
        '20200619_umwrgx_ddg': {
            'path': './data/runs/time-series/20200619/run/uwmrgx_ddg/uwmrgx'},
    }

    for run_name, info in runs.items():
        rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                                run_b_orig_path=ORIG_B,
                                run_a_orig_path=None,
                                run_b_rep_path=None,
                                run_a_rep_path=None)

        rpd_eval.trim()
        rpd_eval.evaluate()

        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            trim(info['run'])
            info['scores'] = rpd_eval.evaluate(info['run'])
            info['rmse'] = rpd_eval.rmse(run_b_score=info['scores'])
            info['ndcg_avg'] = np.array([scores['ndcg'] for top_num, scores in info['scores'].items()]).mean()
            info['ndcg_rmse'] = info['rmse']['baseline']['ndcg']

    pass


    rmse_ddg = {
        '2020-06-07': runs.get('20200607_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-09': runs.get('20200609_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-11': runs.get('20200611_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-13': runs.get('20200613_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-15': runs.get('20200615_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-17': runs.get('20200617_umwrg_ddg').get('ndcg_rmse'),
        '2020-06-19': runs.get('20200619_umwrg_ddg').get('ndcg_rmse'),
    }

    ndcg_ddg = {
        '2020-06-07': runs.get('20200607_umwrg_ddg').get('ndcg_avg'),
        '2020-06-09': runs.get('20200609_umwrg_ddg').get('ndcg_avg'),
        '2020-06-11': runs.get('20200611_umwrg_ddg').get('ndcg_avg'),
        '2020-06-13': runs.get('20200613_umwrg_ddg').get('ndcg_avg'),
        '2020-06-15': runs.get('20200615_umwrg_ddg').get('ndcg_avg'),
        '2020-06-17': runs.get('20200617_umwrg_ddg').get('ndcg_avg'),
        '2020-06-19': runs.get('20200619_umwrg_ddg').get('ndcg_avg'),
    }

    rmse_google = {
        '2020-06-07': runs.get('20200607_umwrg_google').get('ndcg_rmse'),
        '2020-06-09': runs.get('20200609_umwrg_google').get('ndcg_rmse'),
        '2020-06-11': runs.get('20200611_umwrg_google').get('ndcg_rmse'),
        '2020-06-13': runs.get('20200613_umwrg_google').get('ndcg_rmse'),
        '2020-06-15': runs.get('20200615_umwrg_google').get('ndcg_rmse'),
        '2020-06-17': runs.get('20200617_umwrg_google').get('ndcg_rmse'),
        '2020-06-19': runs.get('20200619_umwrg_google').get('ndcg_rmse'),
    }

    ndcg_google = {
        '2020-06-07': runs.get('20200607_umwrg_google').get('ndcg_avg'),
        '2020-06-09': runs.get('20200609_umwrg_google').get('ndcg_avg'),
        '2020-06-11': runs.get('20200611_umwrg_google').get('ndcg_avg'),
        '2020-06-13': runs.get('20200613_umwrg_google').get('ndcg_avg'),
        '2020-06-15': runs.get('20200615_umwrg_google').get('ndcg_avg'),
        '2020-06-17': runs.get('20200617_umwrg_google').get('ndcg_avg'),
        '2020-06-19': runs.get('20200619_umwrg_google').get('ndcg_avg'),
    }

    rmse_ddg_x = {
        '2020-06-07': runs.get('20200607_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-09': runs.get('20200609_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-11': runs.get('20200611_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-13': runs.get('20200613_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-15': runs.get('20200615_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-17': runs.get('20200617_umwrgx_ddg').get('ndcg_rmse'),
        '2020-06-19': runs.get('20200619_umwrgx_ddg').get('ndcg_rmse'),
    }

    ndcg_ddg_x = {
        '2020-06-07': runs.get('20200607_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-09': runs.get('20200609_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-11': runs.get('20200611_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-13': runs.get('20200613_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-15': runs.get('20200615_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-17': runs.get('20200617_umwrgx_ddg').get('ndcg_avg'),
        '2020-06-19': runs.get('20200619_umwrgx_ddg').get('ndcg_avg'),
    }

    rmse_google_x = {
        '2020-06-07': runs.get('20200607_umwrgx_google').get('ndcg_rmse'),
        '2020-06-09': runs.get('20200609_umwrgx_google').get('ndcg_rmse'),
        '2020-06-11': runs.get('20200611_umwrgx_google').get('ndcg_rmse'),
        '2020-06-13': runs.get('20200613_umwrgx_google').get('ndcg_rmse'),
        '2020-06-15': runs.get('20200615_umwrgx_google').get('ndcg_rmse'),
        '2020-06-17': runs.get('20200617_umwrgx_google').get('ndcg_rmse'),
        '2020-06-19': runs.get('20200619_umwrgx_google').get('ndcg_rmse'),
    }

    ndcg_google_x = {
        '2020-06-07': runs.get('20200607_umwrgx_google').get('ndcg_avg'),
        '2020-06-09': runs.get('20200609_umwrgx_google').get('ndcg_avg'),
        '2020-06-11': runs.get('20200611_umwrgx_google').get('ndcg_avg'),
        '2020-06-13': runs.get('20200613_umwrgx_google').get('ndcg_avg'),
        '2020-06-15': runs.get('20200615_umwrgx_google').get('ndcg_avg'),
        '2020-06-17': runs.get('20200617_umwrgx_google').get('ndcg_avg'),
        '2020-06-19': runs.get('20200619_umwrgx_google').get('ndcg_avg'),
    }

    df = pd.DataFrame(data={
        'RBO (uwmrg, Google)': list(rbos_avg_google.values()),
        'RBO (uwmrg, DDG)': list(rbos_avg.values()),
        'RMSE (uwmrg, Google)': list(rmse_google.values()),
        'nDCG (uwmrg, Google)': list(ndcg_google.values()),
        'RMSE (uwmrg, DDG)': list(rmse_ddg.values()),
        'nDCG (uwmrg, DDG)': list(ndcg_ddg.values()),
        'RMSE (uwmrgx, Google)': list(rmse_google_x.values()),
        'nDCG (uwmrgx, Google)': list(ndcg_google_x.values()),
        'RMSE (uwmrgx, DDG)': list(rmse_ddg_x.values()),
        'nDCG (uwmrgx, DDG)': list(ndcg_ddg_x.values()),
        },
        index=rmse_ddg.keys())

    ax = df[['RBO (uwmrg, Google)', 'RBO (uwmrg, DDG)', 'RMSE (uwmrg, Google)', 'RMSE (uwmrg, DDG)', 'RMSE (uwmrgx, Google)', 'RMSE (uwmrgx, DDG)']].plot(linestyle='-', linewidth=3.0, figsize=(12, 5))
    df[['nDCG (uwmrg, Google)', 'nDCG (uwmrg, DDG)', 'nDCG (uwmrgx, Google)', 'nDCG (uwmrgx, DDG)']].plot.bar(ax=ax, color=['grey', 'dimgrey', 'slategrey', 'lightsteelblue'])

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_title('RBO of URLs in Comparison to RMSE and Absolute Scores of nDCG')
    ax.set_xlabel('Date')
    ax.set_ylabel('Score')
    ax.get_figure().savefig('./data/plots/time_series.pdf', format='pdf', bbox_inches='tight')
    plt.show()

    pass


if __name__ == '__main__':
    main()
