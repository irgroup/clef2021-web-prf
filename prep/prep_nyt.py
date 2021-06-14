import os
from conf import path

from core.data import raw_text_from_times, clean_raw_text

if __name__ == '__main__':

    if not os.path.exists(path.NYT_RAW):
        os.makedirs(path.NYT_RAW)

    raw_text_from_times(path.NYT_ORIG, path.TMP_DIR, path.NYT_RAW)

    if not os.path.exists(path.NYT_CLEAN):
        os.makedirs(path.NYT_CLEAN)

    clean_raw_text(path.NYT_RAW, path.NYT_CLEAN, wapo=False)