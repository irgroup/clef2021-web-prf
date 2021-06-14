from repro_eval.Evaluator import RplEvaluator, RpdEvaluator
import pandas as pd

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'

_data = {}


def main():
    # Core18 - DDG - Title
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core18_ddg_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core18_ddg_title/uwmrg')
    rpd_eval.trim()
    rpd_eval.evaluate()
    pvals = rpd_eval.ttest()

    print('Core18 - DDG - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())

    _data['uwmrgx_core18_ddg_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                        'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                        'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())

    _data['uwmrg_core18_ddg_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                       'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                       'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core18 - DDG - Title+Desc
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core18_ddg_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core18_ddg_title_desc/uwmrg')
    rpd_eval.trim()
    rpd_eval.evaluate()
    pvals = rpd_eval.ttest()

    print('Core18 - DDG - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())

    _data['uwmrgx_core18_ddg_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                             'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                             'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())

    _data['uwmrg_core18_ddg_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                            'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                            'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core18 - Google - Title
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core18_google_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core18_google_title/uwmrg')
    rpd_eval.trim()
    rpd_eval.evaluate()
    pvals = rpd_eval.ttest()

    print('Core18 - Google - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())

    _data['uwmrgx_core18_google_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                           'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                           'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())

    _data['uwmrg_core18_google_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                          'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                          'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core18 - Google - Title+Desc
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core18_google_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core18_google_title_desc/uwmrg')
    rpd_eval.trim()
    rpd_eval.evaluate()
    pvals = rpd_eval.ttest()

    print('Core18 - Google - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpd_eval.run_b_rep_score.items()]) / len(rpd_eval.run_b_rep_score.items())

    _data['uwmrgx_core18_google_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                                'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                                'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpd_eval.run_a_rep_score.items()]) / len(rpd_eval.run_a_rep_score.items())

    _data['uwmrg_core18_google_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                               'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                               'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core17 - DDG - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core17_ddg_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core17_ddg_title/uwmrg',
                            qrel_rpl_path='./data/qrels/core17.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Core17 - DDG - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_core17_ddg_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                        'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                        'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_core17_ddg_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                       'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                       'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core17 - DDG - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core17_ddg_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core17_ddg_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/core17.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Core17 - DDG - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_core17_ddg_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                             'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                             'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_core17_ddg_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                            'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                            'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core17 - Google - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core17_google_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core17_google_title/uwmrg',
                            qrel_rpl_path='./data/qrels/core17.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Core17 - Google - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_core17_google_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                           'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                           'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_core17_google_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                          'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                          'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Core17 - Google - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_core17_google_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_core17_google_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/core17.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Core17 - Google - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_core17_google_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                                'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                                'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_core17_google_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                               'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                               'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust05 - DDG - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob05_ddg_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob05_ddg_title/uwmrg',
                            qrel_rpl_path='./data/qrels/robust05.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust05 - DDG - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob05_ddg_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                       'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                       'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob05_ddg_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                      'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                      'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust05 - DDG - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob05_ddg_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob05_ddg_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/robust05.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust05 - DDG - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob05_ddg_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                            'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                            'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob05_ddg_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                           'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                           'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust05 - Google - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob05_google_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob05_google_title/uwmrg',
                            qrel_rpl_path='./data/qrels/robust05.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust05 - Google - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob05_google_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                          'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                          'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob05_google_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                         'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                         'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust05 - Google - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob05_google_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob05_google_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/robust05.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust05 - Google - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob05_google_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                               'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                               'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob05_google_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                              'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                              'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust04 - DDG - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob04_ddg_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob04_ddg_title/uwmrg',
                            qrel_rpl_path='./data/qrels/robust04.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust04 - DDG - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob04_ddg_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                       'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                       'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob04_ddg_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                      'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                      'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust04 - DDG - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob04_ddg_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob04_ddg_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/robust04.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust04 - DDG - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob04_ddg_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                            'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                            'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob04_ddg_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                           'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                           'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust04 - Google - Title
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob04_google_title/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob04_google_title/uwmrg',
                            qrel_rpl_path='./data/qrels/robust04.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust04 - Google - Title')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob04_google_title'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                          'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                          'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob04_google_title'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                         'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                         'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    # Robust04 - Google - Title+Desc
    rpl_eval = RplEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path='./data/runs/uwmrgx_rob04_google_title_desc/uwmrgx',
                            run_a_rep_path='./data/runs/uwmrg_rob04_google_title_desc/uwmrg',
                            qrel_rpl_path='./data/qrels/robust04.txt')
    rpl_eval.trim()
    rpl_eval.evaluate()
    pvals = rpl_eval.ttest()

    print('Robust04 - Google - Title+Desc')
    print('====================')
    print('uwmrgx - P@10:', pvals['baseline']['P_10'])
    print('uwmrgx -   AP:', pvals['baseline']['map'])
    print('uwmrgx - nDCG:', pvals['baseline']['ndcg'])
    print('uwmrg  - P@10:', pvals['advanced']['P_10'])
    print('uwmrg  -   AP:', pvals['advanced']['map'])
    print('uwmrg  - nDCG:', pvals['advanced']['ndcg'])
    print()

    p10_base = sum([scores['P_10'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    map_base = sum([scores['map'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())
    ndcg_base = sum([scores['ndcg'] for _, scores in rpl_eval.run_b_rep_score.items()]) / len(rpl_eval.run_b_rep_score.items())

    _data['uwmrgx_rob04_google_title_desc'] = {'ARP (P@10)': p10_base, 'p-val (P@10)': pvals['baseline']['P_10'],
                                               'ARP (nDCG)': ndcg_base, 'p-val (nDCG)': pvals['baseline']['ndcg'],
                                               'ARP (AP)': map_base, 'p-val (AP)': pvals['baseline']['map']}

    p10_adv = sum([scores['P_10'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    map_adv = sum([scores['map'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())
    ndcg_adv = sum([scores['ndcg'] for _, scores in rpl_eval.run_a_rep_score.items()]) / len(rpl_eval.run_a_rep_score.items())

    _data['uwmrg_rob04_google_title_desc'] = {'ARP (P@10)': p10_adv, 'p-val (P@10)': pvals['advanced']['P_10'],
                                              'ARP (nDCG)': ndcg_adv, 'p-val (nDCG)': pvals['advanced']['ndcg'],
                                              'ARP (AP)': map_adv, 'p-val (AP)': pvals['advanced']['map']}

    print(pd.DataFrame(_data).transpose().to_latex(float_format="%.4f"))


if __name__ == "__main__":
    main()
