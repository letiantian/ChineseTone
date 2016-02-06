# coding: utf-8

from __future__ import (print_function, unicode_literals)

import jieba
from ChineseTone import *

def cut(s):
    return jieba.cut(s, cut_all=False)

print(PinyinHelper.convertToPinyinFromSentence('提出了解决方案', pinyinFormat=PinyinFormat.WITHOUT_TONE))
print(PinyinHelper.convertToPinyinFromSentence('提出了解决方案', pinyinFormat=PinyinFormat.WITHOUT_TONE, segment=cut))