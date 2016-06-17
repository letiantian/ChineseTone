# coding: utf-8

from __future__ import (print_function, unicode_literals)

from ChineseTone import *

print(PinyinHelper.convertWithToneNumber('yú'))
print(PinyinHelper.convertWithToneNumber('diào'))
print(PinyinHelper.convertWithToneNumber('lüè'))

print(20*'*')

print(PinyinHelper.convertWithoutTone('yú'))
print(PinyinHelper.convertWithoutTone('diào'))
print(PinyinHelper.convertWithoutTone('lüè'))

print(20*'*')

print(PinyinHelper.formatPinyin('diào'))
print(PinyinHelper.formatPinyin('diào', PinyinFormat.WITH_TONE_MARK))
print(PinyinHelper.formatPinyin('diào', PinyinFormat.WITH_TONE_NUMBER))
print(PinyinHelper.formatPinyin('diào', PinyinFormat.WITHOUT_TONE))


print(20*'*')

print(','.join(PinyinHelper.convertToPinyinFromChar('你')))
print(','.join(PinyinHelper.convertToPinyinFromChar('省略')))
print(','.join(PinyinHelper.convertToPinyinFromChar('了')))
print(','.join(PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITH_TONE_MARK)))
print(','.join(PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITH_TONE_NUMBER)))
print(','.join(PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITHOUT_TONE)))

print(20*'*')

print(','.join(PinyinHelper.convertToPinyinFromSentence('你')))
print(','.join(PinyinHelper.convertToPinyinFromSentence('省略')))
print(','.join(PinyinHelper.convertToPinyinFromSentence('了解了', pinyinFormat=PinyinFormat.WITHOUT_TONE)))
print(','.join(PinyinHelper.convertToPinyinFromSentence('了解了！abc03127', pinyinFormat=PinyinFormat.WITHOUT_TONE)))
print(','.join(PinyinHelper.convertToPinyinFromSentence('了解了！abc03127', replace='*')))

print(20*'*')

print(PinyinResource.PHRASE_MAX_LEN)  # 词库中短语最长长度