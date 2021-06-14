import os
import json
from rbo import rbo
import numpy as np
import seaborn as sns
from scipy import stats

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

    intersections = {}
    intersections_avg_google = {}

    for d, t in urls.items():
        tmp = {}
        tmp_intersections = {}
        for topic, u in t.items():

            tmp[topic] = rbo(u, urls[REF][topic], p=0.9).ext
            tmp_intersections[topic] = len(set(u).intersection(set(urls[REF][topic])))

        rbos[d] = tmp
        intersections[d] = tmp_intersections

    for d, topic_rbos in rbos.items():
        rbos_avg_google[d] = np.array(list(topic_rbos.values())).mean()

    for d, topics in intersections.items():
        intersections_avg_google[d] = np.array(list(topics.values())).mean()

    corr, p = stats.pearsonr(list(rbos_avg_google.values()), list(intersections_avg_google.values()))

    print("Pearson correlation between RBO and number of intersecting URLS with r={:.4f} and p={:.4f}".format(corr, p))


if __name__ == '__main__':
    main()
