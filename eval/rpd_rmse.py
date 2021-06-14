import pytrec_eval
from repro_eval.Evaluator import RpdEvaluator
from repro_eval.util import arp, arp_scores
from repro_eval.util import trim
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# sns.set()
sns.set(style="ticks")
palette = sns.color_palette("Paired")
# palette = sns.color_palette("cubehelix", 8)
sns.set_palette(palette)
colors = sns.color_palette()

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'
MEASURE = 'ndcg'

runs_rpd = {
    'uwmrgx_c18_d_t':
        {'path': './data/runs/uwmrgx_core18_ddg_title/uwmrgx'},
    'uwmrgx_c18_d_td':
        {'path': './data/runs/uwmrgx_core18_ddg_title_desc/uwmrgx'},
    'uwmrgx_c18_g_t':
        {'path': './data/runs/uwmrgx_core18_google_title/uwmrgx'},
    'uwmrgx_c18_g_td':
        {'path': './data/runs/uwmrgx_core18_google_title_desc/uwmrgx'},
    'uwmrg_c18_d_t':
        {'path': './data/runs/uwmrg_core18_ddg_title/uwmrg'},
    'uwmrg_c18_d_td':
        {'path': './data/runs/uwmrg_core18_ddg_title_desc/uwmrg'},
    'uwmrg_c18_g_t':
        {'path': './data/runs/uwmrg_core18_google_title/uwmrg'},
    'uwmrg_c18_g_td':
        {'path': './data/runs/uwmrg_core18_google_title_desc/uwmrg'}
}


def main():
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=None,
                            run_b_rep_path=None,
                            run_a_rep_path=None)

    rpd_eval.trim()
    rpd_eval.evaluate()

    for run_name, info in zip(list(runs_rpd.keys())[:4], list(runs_rpd.values())[:4]):
        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            trim(info['run'])
            info['scores'] = rpd_eval.evaluate(info['run'])
            info['rmse'] = rpd_eval.rmse(run_b_score=info['scores'])


    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_A,
                            run_a_orig_path=None,
                            run_b_rep_path=None,
                            run_a_rep_path=None)

    rpd_eval.trim()
    rpd_eval.evaluate()

    for run_name, info in zip(list(runs_rpd.keys())[4:], list(runs_rpd.values())[4:]):
        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            trim(info['run'])
            info['scores'] = rpd_eval.evaluate(info['run'])
            info['rmse'] = rpd_eval.rmse(run_b_score=info['scores'])


    baseline_runs = list(runs_rpd.keys())[:4]
    advanced_runs = list(runs_rpd.keys())[4:]
    cutoffs = ['5', '10', '15', '20', '30', '100', '200', '500', '1000']

    df_content = {}
    for run_name in baseline_runs:
        df_content[run_name] = [runs_rpd[run_name]['rmse']['baseline']['ndcg_cut_' + co] for co in cutoffs]

    df = pd.DataFrame(df_content, index=cutoffs)
    ax = df.plot.line(style='o-')
    ax.set_xlabel('Cut-off values')
    ax.set_ylabel('RMSE')
    ax.get_figure().savefig('./data/plots/rpd_b_rmse.pdf', format='pdf', bbox_inches='tight')
    plt.show()

    df_content = {}
    for run_name in advanced_runs:
        df_content[run_name] = [runs_rpd[run_name]['rmse']['baseline']['ndcg_cut_' + co] for co in cutoffs]

    df = pd.DataFrame(df_content, index=cutoffs)
    ax = df.plot.line(style='o-')
    ax.set_xlabel('Cut-off values')
    ax.set_ylabel('RMSE')
    ax.get_figure().savefig('./data/plots/rpd_a_rmse.pdf', format='pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
