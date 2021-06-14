import os
from conf import path

from core.data import raw_text_from_trec, clean_raw_text

if __name__ == '__main__':

    if not os.path.exists(path.ROB04_RAW):
        os.makedirs(path.ROB04_RAW)

    raw_text_from_trec(path.ROB04_ORIG, path.TMP_DIR, path.ROB04_RAW)

    if not os.path.exists(path.ROB04_CLEAN):
        os.makedirs(path.ROB04_CLEAN)

    clean_raw_text(path.ROB04_RAW, path.ROB04_CLEAN, wapo=False)