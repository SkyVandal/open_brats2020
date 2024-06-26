import os
from pathlib import Path

user = "condor"
BRATS_TRAIN_FOLDERS = f"/home/{user}/tese/data/train"
BRATS_VAL_FOLDER = f"/home/{user}/tese/data/val"
BRATS_TEST_FOLDER = f"/home/{user}/tese/data/test"


def get_brats_folder(on="val"):
    if on == "train":
        return os.environ['BRATS_FOLDERS'] if 'BRATS_FOLDERS' in os.environ else BRATS_TRAIN_FOLDERS
    elif on == "val":
        return os.environ['BRATS_VAL_FOLDER'] if 'BRATS_VAL_FOLDER' in os.environ else BRATS_VAL_FOLDER
    elif on == "test":
        return os.environ['BRATS_TEST_FOLDER'] if 'BRATS_TEST_FOLDER' in os.environ else BRATS_TEST_FOLDER
