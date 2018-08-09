# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

# TODO: make this fold self-contained, only depends on utils package

from datasets.imdb import imdb
from datasets.pascal_voc import pascal_voc
from datasets.pascal3d import pascal3d
from datasets.imagenet3d import imagenet3d
from datasets.kitti import kitti
from datasets.kitti_tracking import kitti_tracking
from datasets.nissan import nissan
from datasets.nthu import nthu
from datasets import factory

## NOTE: obsolete
import os.path as osp
from datasets.imdb import ROOT_DIR
from datasets.imdb import MATLAB

# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def _which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
"""
if _which(MATLAB) is None:
    msg = ("MATLAB command '{}' not found. "
           "Please add '{}' to your PATH.").format(MATLAB, MATLAB)
    raise EnvironmentError(msg)
"""
