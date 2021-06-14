from repro_eval.Evaluator import RpdEvaluator
from repro_eval.util import trim, arp
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
         'qrel': './data/qrels/core18.txt'}
}


def main():
    for run_name, info in runs.items():
        rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                                run_b_orig_path=ORIG_B,
                                run_a_orig_path=ORIG_A,
                                run_b_rep_path=None,
                                run_a_rep_path=None)

        rpd_eval.trim()
        rpd_eval.evaluate()
        with open(info['path_base']) as run_file_base, open(info['path_adv']) as run_file_adv:
            info['run_base'] = pytrec_eval.parse_run(run_file_base)
            trim(info['run_base'])
            info['scores_base'] = rpd_eval.evaluate(info['run_base'])
            info['run_adv'] = pytrec_eval.parse_run(run_file_adv)
            trim(info['run_adv'])
            info['scores_adv'] = rpd_eval.evaluate(info['run_adv'])
            info['ktu'] = rpd_eval.ktau_union(run_b_score=info['run_base'], run_a_score=info['run_adv'])
            info['rbo'] = rpd_eval.rbo(run_b_score=info['run_base'], run_a_score=info['run_adv'])
            info['rmse'] = rpd_eval.rmse(run_b_score=info['scores_base'], run_a_score=info['scores_adv'])

    for run_name, info in runs.items():
        arp_base = np.array([info['scores_base'][key]['ndcg'] for key in info['scores_base'].keys()]).mean()
        arp_adv = np.array([info['scores_adv'][key]['ndcg'] for key in info['scores_base'].keys()]).mean()
        ktu_base = arp(info['ktu']['baseline'])
        ktu_adv = arp(info['ktu']['advanced'])
        rbo_base = arp(info['rbo']['baseline'])
        rbo_adv = arp(info['rbo']['advanced'])
        rmse_base = info['rmse']['baseline']['ndcg']
        rmse_adv = info['rmse']['advanced']['ndcg']

        print(run_name,
              ' & ', '{:.4f}'.format(arp_base),
              ' & ', '{:.4f}'.format(ktu_base),
              ' & ', '{:.4f}'.format(rbo_base),
              ' & ', '{:.4f}'.format(rmse_base),
              ' & ', '{:.4f}'.format(arp_adv),
              ' & ', '{:.4f}'.format(ktu_adv),
              ' & ', '{:.4f}'.format(rbo_adv),
              ' & ', '{:.4f}'.format(rmse_adv)
              )


if __name__ == "__main__":
    main()
