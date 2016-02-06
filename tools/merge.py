# coding: utf-8


from __future__ import print_function

import os
import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


data = {}

files = ['./dict-zi.db', './pinyin.db']

for fpath in files:
    for line in open(fpath):
        if '=' in line:
            hanzi, py = line.split('=')
        


