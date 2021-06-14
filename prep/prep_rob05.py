import os
from conf import path

from core.data import raw_text_from_trec, clean_raw_text

if __name__ == '__main__':

    if not os.path.exists(path.ROB05_RAW):
        os.makedirs(path.ROB05_RAW)

    raw_text_from_trec(path.ROB05_ORIG, path.TMP_DIR, path.ROB05_RAW)

    if not os.path.exists(path.ROB05_CLEAN):
        os.makedirs(path.ROB05_CLEAN)

    clean_raw_text(path.ROB05_RAW, path.ROB05_CLEAN, wapo=False)