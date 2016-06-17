# coding: utf-8

from __future__ import (print_function, unicode_literals)

import jieba
from ChineseTone import *

def cut(s):
    return jieba.cut(s, cut_all=False)

print(','.join(PinyinHelper.convertToPinyinFromSentence('我来到北京清华大学', segment=cut)))
print(','.join(PinyinHelper.convertToPinyinFromSentence('了解了！abc03127', pinyinFormat=PinyinFormat.WITHOUT_TONE, segment=cut)))
print(','.join(PinyinHelper.convertToPinyinFromSentence('了解了！abc03127', pinyinFormat=PinyinFormat.WITH_TONE_NUMBER, segment=cut)))