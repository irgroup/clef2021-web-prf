from repro_eval.Evaluator import RpdEvaluator
from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
import pytrec_eval
from repro_eval.util import trim
import seaborn as sns
sns.set(style="ticks")
palette = sns.color_palette("GnBu_d")
sns.set_palette(palette)

QREL = './data/qrels/core18.txt'
ORIG_B = './data/runs/orig/uwmrgx'
ORIG_A = './data/runs/orig/uwmrg'
RPL_B = './data/runs/uwmrgx_core18_google_title_desc/uwmrgx'
RPL_A = './data/runs/uwmrg_core18_google_title_desc/uwmrg'
MEASURE = 'ndcg'


def order_dict(dictionary):
    return OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))


def main():
    rpd_eval = RpdEvaluator(qrel_orig_path=QREL,
                            run_b_orig_path=ORIG_B,
                            run_a_orig_path=ORIG_A,
                            run_b_rep_path=RPL_B,
                            run_a_rep_path=RPL_A)

    rpd_eval.trim()
    rpd_eval.evaluate()

    base_orig_scores = order_dict(rpd_eval.run_b_orig_score)
    base_rpl_scores = order_dict(rpd_eval.run_b_rep_score)
    base_orig_ndcg = {key: value.get(MEASURE) for key, value in base_orig_scores.items()}
    base_rpl_ndcg = {key: value.get(MEASURE) for key, value in base_rpl_scores.items()}

    diff_ndcg = {key: value - base_rpl_ndcg.get(key) for key, value in base_orig_ndcg.items()}

    with open('./data/runs/uwmrgx_core18_google_title_desc/uwmrgx') as run_file:
        run = pytrec_eval.parse_run(run_file)
        trim(run)
        scores = rpd_eval.evaluate(run)

    rpd_rpd_scores = {key: value.get(MEASURE) for key, value in order_dict(scores).items()}

    diff_ndcg_rpl = {key: value - rpd_rpd_scores.get(key) for key, value in base_orig_ndcg.items()}

    # df = pd.DataFrame(diff_ndcg.values(), index=diff_ndcg.keys(), columns=['ndcg'])
    # df.sort_values('ndcg', ascending=False).plot.bar(figsize=(12, 4))
    df = pd.DataFrame({r'$\Delta$' + ' nDCG': list(diff_ndcg.values())}, index=diff_ndcg.keys())
    ax = df.sort_values(r'$\Delta$' + ' nDCG', ascending=False).plot.bar(figsize=(12, 4), legend=False)
    ax.set_xlabel('Topics')
    ax.set_ylabel(r'$\Delta$' + ' nDCG')
    ax.set_title('Topic-wise Differences between Original Results and Reproductions (Core18)')
    ax.hlines(0, -1, 50, color='black')
    plt.savefig('./data/plots/rpd_topic_diff.pdf', format='pdf', bbox_inches='tight')
    plt.show()

    pass


if __name__ == "__main__":
    main()
