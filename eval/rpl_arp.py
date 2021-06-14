import pytrec_eval
from repro_eval.Evaluator import RplEvaluator
from repro_eval.util import arp, arp_scores
from repro_eval.util import trim
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
sns.set_style('ticks')
# palette = sns.color_palette("GnBu_d")
# palette = sns.color_palette("Paired")
# sns.set_palette(palette)
colors = sns.color_palette()

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'

runs = {
    'uwmrgx_c18_d_t':
        {'path': './data/runs/uwmrgx_core18_ddg_title/uwmrgx',
         'qrel': './data/qrels/core18.txt'},
    'uwmrgx_c18_d_td':
        {'path': './data/runs/uwmrgx_core18_ddg_title_desc/uwmrgx',
         'qrel': './data/qrels/core18.txt'},
    'uwmrgx_c18_g_t':
        {'path': './data/runs/uwmrgx_core18_google_title/uwmrgx',
         'qrel': './data/qrels/core18.txt'},
    'uwmrgx_c18_g_td':
        {'path': './data/runs/uwmrgx_core18_google_title_desc/uwmrgx',
         'qrel': './data/qrels/core18.txt'},
    'uwmrg_c18_d_t':
        {'path': './data/runs/uwmrg_core18_ddg_title/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'uwmrg_c18_d_td':
        {'path': './data/runs/uwmrg_core18_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'uwmrg_c18_g_t':
        {'path': './data/runs/uwmrg_core18_google_title/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'uwmrg_c18_g_td':
        {'path': './data/runs/uwmrg_core18_google_title_desc/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'uwmrgx_c17_d_t':
        {'path': './data/runs/uwmrgx_core17_ddg_title/uwmrgx',
         'qrel': './data/qrels/core17.txt'},
    'uwmrgx_c17_d_td':
        {'path': './data/runs/uwmrgx_core17_ddg_title_desc/uwmrgx',
         'qrel': './data/qrels/core17.txt'},
    'uwmrgx_c17_g_t':
        {'path': './data/runs/uwmrgx_core17_google_title/uwmrgx',
         'qrel': './data/qrels/core17.txt'},
    'uwmrgx_c17_g_td':
        {'path': './data/runs/uwmrgx_core17_google_title_desc/uwmrgx',
         'qrel': './data/qrels/core17.txt'},
    'uwmrg_c17_d_t':
        {'path': './data/runs/uwmrg_core17_ddg_title/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'uwmrg_c17_d_td':
        {'path': './data/runs/uwmrg_core17_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'uwmrg_c17_g_t':
        {'path': './data/runs/uwmrg_core17_google_title/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'uwmrg_c17_g_td':
        {'path': './data/runs/uwmrg_core17_google_title_desc/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'uwmrgx_r5_d_t':
        {'path': './data/runs/uwmrgx_rob05_ddg_title/uwmrgx',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrgx_r5_d_td':
        {'path': './data/runs/uwmrgx_rob05_ddg_title_desc/uwmrgx',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrgx_r5_g_t':
        {'path': './data/runs/uwmrgx_rob05_google_title/uwmrgx',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrgx_r5_g_td':
        {'path': './data/runs/uwmrgx_rob05_google_title_desc/uwmrgx',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrg_r5_d_t':
        {'path': './data/runs/uwmrg_rob05_ddg_title/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrg_r5_d_td':
        {'path': './data/runs/uwmrg_rob05_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrg_r5_g_t':
        {'path': './data/runs/uwmrg_rob05_google_title/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrg_r5_g_td':
        {'path': './data/runs/uwmrg_rob05_google_title_desc/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'uwmrgx_r4_d_t':
        {'path': './data/runs/uwmrgx_rob04_ddg_title/uwmrgx',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrgx_r4_d_td':
        {'path': './data/runs/uwmrgx_rob04_ddg_title_desc/uwmrgx',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrgx_r4_g_t':
        {'path': './data/runs/uwmrgx_rob04_google_title/uwmrgx',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrgx_r4_g_td':
        {'path': './data/runs/uwmrgx_rob04_google_title_desc/uwmrgx',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrg_r4_d_t':
        {'path': './data/runs/uwmrg_rob04_ddg_title/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrg_r4_d_td':
        {'path': './data/runs/uwmrg_rob04_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrg_r4_g_t':
        {'path': './data/runs/uwmrg_rob04_google_title/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'uwmrg_r4_g_td':
        {'path': './data/runs/uwmrg_rob04_google_title_desc/uwmrg',
         'qrel': './data/qrels/robust04.txt'}
}


def average_retrieval_performance(baseline_scores, replicated_scores: dict, measures: list, xlabel: str, ylabel: str, outfile: str):
    replicated_scores_arp = [arp_scores(topic_scores) for idx, topic_scores in replicated_scores.items()]
    baseline_scores_arp = arp_scores(baseline_scores)
    index = list(replicated_scores.keys())
    df_content = {}
    for measure in measures:
        df_content[measure] = [scores.get(measure) for scores in replicated_scores_arp]
    df = pd.DataFrame(df_content, index=index)

    ax = df.plot.bar(rot=90, figsize=(12, 4))
    for num, measure in enumerate(measures):
        orig_val = baseline_scores_arp.get(measure)
        ax.hlines(orig_val, -.5, 15.5, linestyles='dashed', color=colors[num])
        ax.annotate(' ', (num, orig_val), color=colors[num])
        ax.set_ylim(0.0, 0.7)

    # legend_content = [measure + ' (GC)' for measure in measures] + [measure + ' (rpd/rpl)' for measure in measures]
    legend_content = [measure + ' (GC)' for measure in ['P@10', 'nDCG', 'AP']] + ['P@10', 'nDCG', 'AP']
    ax.legend(legend_content, loc='upper left', bbox_to_anchor=(0.1, 1.01), ncol=6)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.get_figure().savefig(outfile, format='pdf', bbox_inches='tight')
    plt.show()


def main():
    for run_name, info in runs.items():
        rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                                run_b_orig_path=ORIG_B,
                                run_a_orig_path=ORIG_A,
                                run_b_rep_path=None,
                                run_a_rep_path=None,
                                qrel_rpd_path=info['qrel'])

        rpl_eval.trim()
        rpl_eval.evaluate()

        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            trim(info['run'])
            info['scores'] = rpl_eval.evaluate(info['run'])

    average_retrieval_performance(rpl_eval.run_b_orig_score,
                                  {
                                      'c18_g_td': runs.get('uwmrgx_c18_g_td').get('scores'),
                                      'c18_g_t': runs.get('uwmrgx_c18_g_t').get('scores'),
                                      'c18_d_td': runs.get('uwmrgx_c18_d_td').get('scores'),
                                      'c18_d_t': runs.get('uwmrgx_c18_d_t').get('scores'),
                                      'c17_g_td': runs.get('uwmrgx_c17_g_td').get('scores'),
                                      'c17_g_t': runs.get('uwmrgx_c17_g_t').get('scores'),
                                      'c17_d_td': runs.get('uwmrgx_c17_d_td').get('scores'),
                                      'c17_d_t': runs.get('uwmrgx_c17_d_t').get('scores'),
                                      'r5_g_td': runs.get('uwmrgx_r5_g_td').get('scores'),
                                      'r5_g_t': runs.get('uwmrgx_r5_g_t').get('scores'),
                                      'r5_d_td': runs.get('uwmrgx_r5_d_td').get('scores'),
                                      'r5_d_t': runs.get('uwmrgx_r5_d_t').get('scores'),
                                      'r4_g_td': runs.get('uwmrgx_r4_g_td').get('scores'),
                                      'r4_g_t': runs.get('uwmrgx_r4_g_t').get('scores'),
                                      'r4_d_td': runs.get('uwmrgx_r4_d_td').get('scores'),
                                      'r4_d_t': runs.get('uwmrgx_r4_d_t').get('scores')
                                  },
                                  measures=['P_10', 'ndcg', 'map'],
                                  xlabel='Reproduced and replicated baseline runs (uwmrgx)',
                                  ylabel='Score',
                                  outfile='./data/plots/arp_base.pdf')

    average_retrieval_performance(rpl_eval.run_a_orig_score,
                                  {
                                      'c18_g_td': runs.get('uwmrg_c18_g_td').get('scores'),
                                      'c18_g_t': runs.get('uwmrg_c18_g_t').get('scores'),
                                      'c18_d_td': runs.get('uwmrg_c18_d_td').get('scores'),
                                      'c18_d_t': runs.get('uwmrg_c18_d_t').get('scores'),
                                      'c17_g_td': runs.get('uwmrg_c17_g_td').get('scores'),
                                      'c17_g_t': runs.get('uwmrg_c17_g_t').get('scores'),
                                      'c17_d_td': runs.get('uwmrg_c17_d_td').get('scores'),
                                      'c17_d_t': runs.get('uwmrg_c17_d_t').get('scores'),
                                      'r5_g_td': runs.get('uwmrg_r5_g_td').get('scores'),
                                      'r5_g_t': runs.get('uwmrg_r5_g_t').get('scores'),
                                      'r5_d_td': runs.get('uwmrg_r5_d_td').get('scores'),
                                      'r5_d_t': runs.get('uwmrg_r5_d_t').get('scores'),
                                      'r4_g_td': runs.get('uwmrg_r4_g_td').get('scores'),
                                      'r4_g_t': runs.get('uwmrg_r4_g_t').get('scores'),
                                      'r4_d_td': runs.get('uwmrg_r4_d_td').get('scores'),
                                      'r4_d_t': runs.get('uwmrg_r4_d_t').get('scores')
                                  },
                                  measures=['P_10', 'ndcg', 'map'],
                                  xlabel='Reproduced and replicated advanced runs (uwmrg)',
                                  ylabel='Score',
                                  outfile='./data/plots/arp_adv.pdf')


if __name__ == "__main__":
    main()
