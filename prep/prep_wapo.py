import os
from conf import path

from core.data import raw_text_from_wapo, clean_raw_text

if __name__ == '__main__':

    if not os.path.exists(path.WAPO_RAW):
        os.makedirs(path.WAPO_RAW)

    raw_text_from_wapo(path.WAPO_ORIG, path.WAPO_RAW)

    if not os.path.exists(path.WAPO_CLEAN):
        os.makedirs(path.WAPO_CLEAN)

    clean_raw_text(path.WAPO_RAW, path.WAPO_CLEAN, wapo=True)
