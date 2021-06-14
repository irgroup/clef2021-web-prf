from repro_eval.Evaluator import RpdEvaluator
from repro_eval.util import print_base_adv, print_simple_line, trim, arp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks")
palette = sns.color_palette("Paired")
sns.set_palette(palette)
import pandas as pd
import matplotlib.pyplot as plt
import pytrec_eval

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'

MEASURE = 'ndcg'

runs_rpd = {
    'uwmrgx_c18_d_t':
        {'path': './data/runs/uwmrgx_core18_ddg_title/uwmrgx'},
    'uwmrg_c18_d_t':
        {'path': './data/runs/uwmrg_core18_ddg_title/uwmrg'},
    'uwmrgx_c18_d_td':
        {'path': './data/runs/uwmrgx_core18_ddg_title_desc/uwmrgx'},
    'uwmrg_c18_d_td':
        {'path': './data/runs/uwmrg_core18_ddg_title_desc/uwmrg'},
    'uwmrgx_c18_g_t':
        {'path': './data/runs/uwmrgx_core18_google_title/uwmrgx'},
    'uwmrg_c18_g_t':
        {'path': './data/runs/uwmrg_core18_google_title/uwmrg'},
    'uwmrgx_c18_g_td':
        {'path': './data/runs/uwmrgx_core18_google_title_desc/uwmrgx'},
    'uwmrg_c18_g_td':
        {'path': './data/runs/uwmrg_core18_google_title_desc/uwmrg'},
}


def main():
    cutoffs = [1000, 100, 50, 20, 10, 5]

    # BASELINE
    for run_name, info in zip(list(runs_rpd.keys())[::2], list(runs_rpd.values())[::2]):
        rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                                run_b_orig_path=ORIG_B,
                                run_a_orig_path=None,
                                run_b_rep_path=None,
                                run_a_rep_path=None)

        rpd_eval.trim()
        rpd_eval.evaluate()

        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            for cutoff in cutoffs:
                rpd_eval.trim(cutoff)
                rpd_eval.trim(cutoff, info['run'])
                info['ktu_' + str(cutoff)] = arp(rpd_eval.rbo(info['run'])['baseline'])

    df_content = {}
    for run_name, info in zip(list(runs_rpd.keys())[::2], list(runs_rpd.values())[::2]):
        df_content[run_name] = [info.get('ktu_' + str(cutoff)) for cutoff in cutoffs[::-1]]

    ax = pd.DataFrame(data=df_content, index=[str(cutoff) for cutoff in cutoffs[::-1]]).plot(style='o-')
    ax.set_xlabel('Cut-off values')
    ax.set_ylabel("Rank-biased Overlap")
    ax.get_figure().savefig('./data/plots/rpd_b_rbo.pdf', format='pdf', bbox_inches='tight', loc='upper right')
    plt.show()

    # ADVANCED
    for run_name, info in zip(list(runs_rpd.keys())[1::2], list(runs_rpd.values())[1::2]):
        rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                                run_b_orig_path=ORIG_A,
                                run_a_orig_path=None,
                                run_b_rep_path=None,
                                run_a_rep_path=None)

        rpd_eval.trim()
        rpd_eval.evaluate()

        with open(info.get('path')) as run_file:
            info['run'] = pytrec_eval.parse_run(run_file)
            for cutoff in cutoffs:
                rpd_eval.trim(cutoff)
                rpd_eval.trim(cutoff, info['run'])
                # scores = rpl_eval.evaluate(info['run'])
                info['ktu_' + str(cutoff)] = arp(rpd_eval.rbo(info['run'])['baseline'])

    df_content = {}
    for run_name, info in zip(list(runs_rpd.keys())[1::2], list(runs_rpd.values())[1::2]):
        df_content[run_name] = [info.get('ktu_' + str(cutoff)) for cutoff in cutoffs[::-1]]

    ax = pd.DataFrame(data=df_content, index=[str(cutoff) for cutoff in cutoffs[::-1]]).plot(style='o-')
    ax.set_xlabel('Cut-off values')
    ax.set_ylabel("Rank-biased Overlap")
    ax.get_figure().savefig('./data/plots/rpd_a_rbo.pdf', format='pdf', bbox_inches='tight', loc='upper right')
    plt.show()


if __name__ == "__main__":
    main()
