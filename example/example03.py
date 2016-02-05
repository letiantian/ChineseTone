# coding: utf-8

from __future__ import (print_function, unicode_literals)

from Hanzi2Pinyin import *

print( PinyinHelper.hasMultiPinyin('你') )
print( PinyinHelper.hasMultiPinyin('了') )

print( 20*'*' )

print( PinyinHelper.getShengmu('ni') )
print( PinyinHelper.getShengmu('sheng') )
print( PinyinHelper.getShengmu('en') )

