# coding: utf-8

from __future__ import (print_function, unicode_literals)

from ChineseTone import *

print(','.join(PinyinHelper.convertToPinyinFromSentence('金馆长啊', pinyinFormat=PinyinFormat.WITHOUT_TONE)))
PinyinHelper.addWordPinyin('金馆长', ['jin', 'guan', 'zhang'])  # 建议实际情况下拼音中加入声调
print(','.join(PinyinHelper.convertToPinyinFromSentence('金馆长啊', pinyinFormat=PinyinFormat.WITHOUT_TONE)))

print(','.join(PinyinHelper.convertToPinyinFromSentence('价值40$', pinyinFormat=PinyinFormat.WITHOUT_TONE)))
PinyinHelper.addCharPinyin('4', ['si'])   # 考虑多音字，所以用list
PinyinHelper.addCharPinyin('0', ['ling'])
PinyinHelper.addWordPinyin('$', ['mei', 'yuan'])  # 这个用法奇怪些
print(','.join(PinyinHelper.convertToPinyinFromSentence('价值40$', pinyinFormat=PinyinFormat.WITHOUT_TONE)))
