title_only = True  # only necessary for scraping
corpus = 'wapo'  # can either be 'wapo', 'nyt', 'rob04' or 'rob05'
websearch = 'bing'  # can either be 'bing', 'duck' or 'google'

gl_google = 'ca'
gl_duck = 'ca-en'

num_cpu = 4
model_type = 'logreg-scikit'  # default: logreg-scikit

# logreg
tol = 1e-4  # default: 1e-4
C = 1.5  # default: 1.5
logreg_solver = 'lbfgs'  # default: 100
max_iter = 100  # default: 100

# svm
svm_C = 1.0
svm_kernel = 'linear'
svm_gamma = 'auto'
svm_tol = 1e-3
svm_max_iter = -1

# tfidf
analyzer = 'word'  # options: 'word', 'char', 'char_wb'
ngram_range = (1, 1)  # default: (1,1) in combination with analyzer = 'word'
max_df = 1.0  # default: 1
min_df = 1  # default: 1
max_features = None  # default: None
binary = False  # default: False
norm = 'l2'  # default: l2
use_idf = True  # default: True
smooth_idf = True  # default: True
sublinear_tf = True  # default: True
