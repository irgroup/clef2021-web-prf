from repro_eval.Evaluator import RplEvaluator
from repro_eval.util import trim
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

import pytrec_eval

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'

runs_rpl = {
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


def main():
    # rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
    #                         run_b_orig_path=ORIG_B,
    #                         run_a_orig_path=ORIG_A,
    #                         run_b_rep_path=None,
    #                         run_a_rep_path=None)

    for run_name, info in runs_rpl.items():
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

    dri_er = {
        'c18_g_t': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_c18_g_t']['scores'], runs_rpl['uwmrg_c18_g_t']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_c18_g_t']['scores'], runs_rpl['uwmrg_c18_g_t']['scores']),
            'type': 't'
        },
        'c18_g_td': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_c18_g_td']['scores'], runs_rpl['uwmrg_c18_g_td']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_c18_g_td']['scores'], runs_rpl['uwmrg_c18_g_td']['scores']),
            'type': 'td'
        },
        'c17_g_t': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_c17_g_t']['scores'], runs_rpl['uwmrg_c17_g_t']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_c17_g_t']['scores'], runs_rpl['uwmrg_c17_g_t']['scores']),
            'type': 't'
        },
        'c17_g_td': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_c17_g_td']['scores'], runs_rpl['uwmrg_c17_g_td']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_c17_g_td']['scores'], runs_rpl['uwmrg_c17_g_td']['scores']),
            'type': 'td'
        },
        'r5_g_t': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_r5_g_t']['scores'], runs_rpl['uwmrg_r5_g_t']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_r5_g_t']['scores'], runs_rpl['uwmrg_r5_g_t']['scores']),
            'type': 't'
        },
        'r5_g_td': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_r5_g_td']['scores'], runs_rpl['uwmrg_r5_g_td']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_r5_g_td']['scores'], runs_rpl['uwmrg_r5_g_td']['scores']),
            'type': 'td'
        },
        'r4_g_t': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_r4_g_t']['scores'], runs_rpl['uwmrg_r4_g_t']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_r4_g_t']['scores'], runs_rpl['uwmrg_r4_g_t']['scores']),
            'type': 't'
        },
        'r4_g_td': {
            'er': rpl_eval.er(runs_rpl['uwmrgx_r4_g_td']['scores'], runs_rpl['uwmrg_r4_g_td']['scores']),
            'dri': rpl_eval.dri(runs_rpl['uwmrgx_r4_g_td']['scores'], runs_rpl['uwmrg_r4_g_td']['scores']),
            'type': 'td'
        }
    }

    measures = ['P_10', 'map', 'ndcg']
    marker_color = [('o', 'b'), ('^', 'g'), ('v', 'r')]

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Effect Ratio (ER)')
    ax1.set_ylabel(u'Delta Relative Improvement (ΔRI)')

    for measure, mk in zip(measures, marker_color):
        ax1.plot([dri_er[r]['er'][measure] for r in ['c18_g_td', 'c17_g_td', 'r5_g_td', 'r4_g_td']],
                 [dri_er[r]['dri'][measure] for r in ['c18_g_td', 'c17_g_td', 'r5_g_td', 'r4_g_td']],
                 marker=mk[0],
                 color='g',
                 linestyle='None',
                 label=measure)

    for measure, mk in zip(measures, marker_color):
        ax1.plot([dri_er[r]['er'][measure] for r in ['c18_g_t', 'c17_g_t', 'r5_g_t', 'r4_g_t']],
                 [dri_er[r]['dri'][measure] for r in ['c18_g_t', 'c17_g_t', 'r5_g_t', 'r4_g_t']],
                 marker=mk[0],
                 color='b',
                 linestyle='None',
                 label=measure)

    ax1.tick_params(axis='y', labelcolor='k')
    fig.tight_layout()
    plt.axhline(0, color='grey')
    plt.axvline(1, color='grey')
    ax1.legend(measures)

    leg = ax1.get_legend()

    # leg.legendHandles[0].set_color('b')
    # leg.legendHandles[1].set_color('b')
    # leg.legendHandles[2].set_color('b')
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='P@10', markerfacecolor='black',  linestyle='None', markersize=8),
                       Line2D([0], [0], marker='^', color='w', label='AP', markerfacecolor='black',  linestyle='None', markersize=8),
                       Line2D([0], [0], marker='v', color='w', label='nDCG', markerfacecolor='black',  linestyle='None', markersize=8)]
    ax1.legend(handles=legend_elements, loc='upper right')

    plt.title('Query variations with Google')
    plt.savefig('./data/plots/dri_vs_er_google.pdf', format='pdf', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
