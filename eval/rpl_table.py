from repro_eval.Evaluator import RplEvaluator
from repro_eval.util import trim, arp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
import pytrec_eval
import numpy as np

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'


runs = {
    'c18_g_td_20':
        {'path_base': './data/runs/uwmrgx_core18_google_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_core18_google_title_desc/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'c18_g_t_20':
        {'path_base': './data/runs/uwmrgx_core18_google_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_core18_google_title/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'c18_d_td_20':
        {'path_base': './data/runs/uwmrgx_core18_ddg_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_core18_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'c18_d_t_20':
        {'path_base': './data/runs/uwmrgx_core18_ddg_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_core18_ddg_title/uwmrg',
         'qrel': './data/qrels/core18.txt'},
    'c17_g_td_20':
        {'path_base': './data/runs/uwmrgx_core17_google_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_core17_google_title_desc/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'c17_g_t_20':
        {'path_base': './data/runs/uwmrgx_core17_google_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_core17_google_title/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'c17_d_td_20':
        {'path_base': './data/runs/uwmrgx_core17_ddg_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_core17_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'c17_d_t_20':
        {'path_base': './data/runs/uwmrgx_core17_ddg_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_core17_ddg_title/uwmrg',
         'qrel': './data/qrels/core17.txt'},
    'r5_g_td_20':
        {'path_base': './data/runs/uwmrgx_rob05_google_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob05_google_title_desc/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'r5_g_t_20':
        {'path_base': './data/runs/uwmrgx_rob05_google_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob05_google_title/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'r5_d_td_20':
        {'path_base': './data/runs/uwmrgx_rob05_ddg_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob05_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'r5_d_t_20':
        {'path_base': './data/runs/uwmrgx_rob05_ddg_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob05_ddg_title/uwmrg',
         'qrel': './data/qrels/robust05.txt'},
    'r4_g_td_20':
        {'path_base': './data/runs/uwmrgx_rob04_google_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob04_google_title_desc/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'r4_g_t_20':
        {'path_base': './data/runs/uwmrgx_rob04_google_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob04_google_title/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'r4_d_td_20':
        {'path_base': './data/runs/uwmrgx_rob04_ddg_title_desc/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob04_ddg_title_desc/uwmrg',
         'qrel': './data/qrels/robust04.txt'},
    'r4_d_t_20':
        {'path_base': './data/runs/uwmrgx_rob04_ddg_title/uwmrgx',
         'path_adv': './data/runs/uwmrg_rob04_ddg_title/uwmrg',
         'qrel': './data/qrels/robust04.txt'}
}


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

        with open(info['path_base']) as run_file_base, open(info['path_adv']) as run_file_adv:
            info['run_base'] = pytrec_eval.parse_run(run_file_base)
            info['run_adv'] = pytrec_eval.parse_run(run_file_adv)
            trim(info['run_base'])
            trim(info['run_adv'])
            info['scores_base'] = rpl_eval.evaluate(info['run_base'])
            info['scores_adv'] = rpl_eval.evaluate(info['run_adv'])
            info['dri'] = rpl_eval.dri(run_b_score=info['scores_base'], run_a_score=info['scores_adv'])
            info['er'] = rpl_eval.er(run_b_score=info['scores_base'], run_a_score=info['scores_adv'])

        pass
    for run_name, info in runs.items():
        arp_base = np.array([info['scores_base'][key]['map'] for key in info['scores_base'].keys()]).mean()
        arp_adv = np.array([info['scores_adv'][key]['map'] for key in info['scores_base'].keys()]).mean()
        dri = info['dri']['map']
        er = info['er']['map']

        print(run_name,
              ' & ', '{:.4f}'.format(arp_base),
              ' & ', '{:.4f}'.format(arp_adv),
              ' & ', '{:.4f}'.format(dri),
              ' & ', '{:.4f}'.format(er)
              )


if __name__ == "__main__":
    main()
