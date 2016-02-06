# coding: utf-8


from __future__ import (print_function, unicode_literals)

import os
import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

PY2 = sys.version_info[0] == 2
if not PY2:
    # Python 3.x and up
    xrange       = range

    def as_text(v):  ## 生成unicode字符串
        if v is None:
            return None
        elif isinstance(v, bytes):
            return v.decode('utf-8', errors='ignore')
        elif isinstance(v, str):
            return v
        else:
            raise ValueError('Unknown type %r' % type(v))

    def is_text(v):
        return isinstance(v, str)

else:
    # Python 2.x
    xrange       = xrange

    def as_text(v):
        if v is None:
            return None
        elif isinstance(v, unicode):
            return v
        elif isinstance(v, str):
            return v.decode('utf-8', errors='ignore')
        else:
            raise ValueError('Invalid type %r' % type(v))

    def is_text(v):
        return isinstance(v, unicode)

def isChinese(s):
    s = as_text(s)
    return all(u'\u4e00' <= c <= u'\u9fff' or c == u'〇' for c in s)

data = {}

files = ['./pinyin.db', './dict-zi.db']

for fpath in files:
    for line in open(fpath):
        line = as_text(line.strip())
        if '=' in line and isChinese(line[0]):
            # print(line)
            hanzi, py = line.split('=')
            pys = py.split(',')
            data.setdefault(hanzi, [])
            for _ in pys:
                if _ not in data[hanzi]:
                    data[hanzi].append(_)

s = ''
for hanzi in data:
    s = s + hanzi + '=' + ','.join(data[hanzi]) + '\n'

print(s)

with open('../ChineseTone/data/pinyin.db', 'w') as out:
    out.write(s)

print( 'end' )
        


