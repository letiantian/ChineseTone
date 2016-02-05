# coding: utf-8

from __future__ import (print_function, unicode_literals)

from Hanzi2Pinyin import *

print( ChineseHelper.isChinese('n') )
print( ChineseHelper.isChinese('你好') )
print( ChineseHelper.isChinese('hi，小王') )

print( ChineseHelper.convertToTraditionalChinese('hi，你好，我来到了北京天安门') )
print( ChineseHelper.convertToSimplifiedChinese('hi，你好，我來到了北京天安門') )
