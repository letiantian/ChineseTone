# coding: utf-8

"""
@author:   letian
@homepage: http://www.letiantian.me
@github:   https://github.com/someus/
"""

from __future__ import (print_function, unicode_literals)

import os
import sys
from collections import namedtuple

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

PinyinFormat = namedtuple('PinyinFormat', ['WITH_TONE_MARK', 'WITHOUT_TONE', 'WITH_TONE_NUMBER'])(1,2,3)

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


class PinyinResource(object):

    PHRASE_MAX_LEN = 1

    @staticmethod
    def getPinyinResource():
        resource = {}
        for line in open(os.path.join(CURRENT_DIR, 'data', 'pinyin.db')):
            line = as_text(line.strip())
            if '=' not in line:
                continue
            hanzi, pinyins  = line.split('=')
            pinyins = pinyins.lower()
            resource[hanzi] = pinyins.split(',')
        return resource

    @staticmethod
    def getWordPinyinResource():
        resource = {}
        wordFiles = ['mutil_pinyin.db', 'phrase.db']
        wordFiles = [os.path.join(CURRENT_DIR, 'data', fname) for fname in wordFiles]

        for fpath in wordFiles:
            for line in open(fpath):
                line = as_text(line.strip())
                if '=' not in line:
                    continue
                word, pinyins  = line.split('=')
                pinyins = pinyins.lower()
                PinyinResource.PHRASE_MAX_LEN = max(PinyinResource.PHRASE_MAX_LEN, len(word))
                resource[word] = pinyins.split(',')

        return resource

    @staticmethod
    def getChineseResource():
        fan2jian_resource = {}
        jian2fan_resource = {}
        for line in open(os.path.join(CURRENT_DIR, 'data', 'chinese.db')):
            line = as_text(line.strip())
            if '=' not in line:
                continue
            traditional, simplified  = line.split('=')
            fan2jian_resource[traditional] = simplified
            jian2fan_resource[simplified] = traditional
        return fan2jian_resource, jian2fan_resource


class PinyinException(Exception):

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)

class PinyinHelper(object):

    initialized  = False

    PINYIN_TABLE = None
    WORD_PINYIN_TABLE = None

    ALL_UNMARKED_VOWEL = "aeiouv"
    ALL_MARKED_VOWEL = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ"

    MARKED_VOWEL_TO_UNMARKED = {
        'ā': 'a',
        'á': 'a',
        'ǎ': 'a',
        'à': 'a',
        'ē': 'e',
        'é': 'e',
        'ě': 'e',
        'è': 'e',
        'ī': 'i',
        'í': 'i',
        'ǐ': 'i',
        'ì': 'i',
        'ō': 'o',
        'ó': 'o',
        'ǒ': 'o',
        'ò': 'o',
        'ū': 'u',
        'ú': 'u',
        'ǔ': 'u',
        'ù': 'u',
        'ü': 'v',
        'ǖ': 'v',
        'ǘ': 'v',
        'ǚ': 'v',
        'ǜ': 'v',
        'ń': 'n',
        'ň': 'n',
        '': 'm',
    }

    MARKED_VOWEL_TO_TONE_NUMBER = {
        'ā': '1',
        'á': '2',
        'ǎ': '3',
        'à': '4',
        'ē': '1',
        'é': '2',
        'ě': '3',
        'è': '4',
        'ī': '1',
        'í': '2',
        'ǐ': '3',
        'ì': '4',
        'ō': '1',
        'ó': '2',
        'ǒ': '3',
        'ò': '4',
        'ū': '1',
        'ú': '2',
        'ǔ': '3',
        'ù': '4',
        'ǖ': '1',
        'ǘ': '2',
        'ǚ': '3',
        'ǜ': '4',
        'ń': '2',
        'ň': '3',
    }

    SHENGMU = set(['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s',])

    @staticmethod
    def loadTable():
        if not PinyinHelper.initialized:
            PinyinHelper.PINYIN_TABLE = PinyinResource.getPinyinResource()
            PinyinHelper.WORD_PINYIN_TABLE = PinyinResource.getWordPinyinResource()
            PinyinHelper.initialized = True

    @staticmethod
    def convertWithToneNumber(pinyin):
        ''' 将带声调格式的拼音转换为数字代表声调格式的拼音 '''
        pinyin = as_text(pinyin)
        pinyin = pinyin.replace('ü', 'v')
        converted_pinyin = ''
        for c in pinyin:
            if c in PinyinHelper.MARKED_VOWEL_TO_UNMARKED:
                converted_pinyin += PinyinHelper.MARKED_VOWEL_TO_UNMARKED[c]
                converted_pinyin += PinyinHelper.MARKED_VOWEL_TO_TONE_NUMBER[c]
            else:
                converted_pinyin += c
        return converted_pinyin


    @staticmethod
    def convertWithoutTone(pinyin):
        ''' 将带声调格式的拼音转换为不带声调格式的拼音 '''
        pinyin = as_text(pinyin)
        pinyin = pinyin.replace('ü', 'v')
        converted_pinyin = ''
        for c in pinyin:
            if c in PinyinHelper.MARKED_VOWEL_TO_UNMARKED:
                converted_pinyin += PinyinHelper.MARKED_VOWEL_TO_UNMARKED[c]
            else:
                converted_pinyin += c
        return converted_pinyin

    @staticmethod
    def formatPinyin(pinyin, pinyinFormat=PinyinFormat.WITH_TONE_MARK):
        ''' 将带声调的拼音格式化为相应格式的拼音 '''
        pinyin = as_text(pinyin)
        if pinyinFormat == PinyinFormat.WITH_TONE_MARK:
            return pinyin
        if pinyinFormat == PinyinFormat.WITH_TONE_NUMBER:
            return PinyinHelper.convertWithToneNumber(pinyin)
        if pinyinFormat == PinyinFormat.WITHOUT_TONE:
            return PinyinHelper.convertWithoutTone(pinyin)

    @staticmethod
    def convertToPinyinFromChar(c, pinyinFormat=PinyinFormat.WITH_TONE_MARK):
        PinyinHelper.loadTable()
        c = as_text(c)
        if c in PinyinHelper.PINYIN_TABLE:
            result = []
            for item in PinyinHelper.PINYIN_TABLE[c]:
                result.append( PinyinHelper.formatPinyin(item, pinyinFormat) )
            return result
        return [c]

    @staticmethod
    def convertToPinyinFromSentence(s, pinyinFormat=PinyinFormat.WITH_TONE_MARK, replace=None, segment=None):

        def __middle(s, pinyinFormat, replace):

            PinyinHelper.loadTable()
            phrase_max_len = PinyinResource.PHRASE_MAX_LEN
            s = as_text(s)
            result = []
            idx = 0
            length = len(s)
            while idx < length:
                isWord = False
                for step in xrange(phrase_max_len, 1, -1):
                    temp_word = s[idx: idx+step]
                    if temp_word in PinyinHelper.WORD_PINYIN_TABLE:
                        result += PinyinHelper.WORD_PINYIN_TABLE[temp_word]
                        idx += step
                        isWord = True
                        break
                if not isWord:
                    char = s[idx]
                    if char in PinyinHelper.PINYIN_TABLE:
                        result.append( PinyinHelper.PINYIN_TABLE[char][0] )
                    elif replace:
                        result.append(replace)
                    else:
                        result.append( char )
                    idx += 1

            return [PinyinHelper.formatPinyin(pinyin, pinyinFormat) for pinyin in result]

        if not segment:
            data = [s]
        else:
            data = segment(s)

        result = []
        for item in data:
            result += __middle(item, pinyinFormat, replace)
        return result

    @staticmethod
    def addWordPinyin(w, pinyinList):
        ''' 添加自定义的单词的拼音，若已有则替换 '''
        PinyinHelper.loadTable()
        PinyinHelper.WORD_PINYIN_TABLE[w] = pinyinList

    @staticmethod
    def addCharPinyin(c, pinyinList):
        ''' 添加自定义的字符的拼音，若已有则替换 '''
        PinyinHelper.loadTable()
        PinyinHelper.PINYIN_TABLE[c] = pinyinList

    @staticmethod
    def hasMultiPinyin(c):
        ''' 是否为多音字 '''
        PinyinHelper.loadTable()
        c = as_text(c)
        if len(PinyinHelper.PINYIN_TABLE[c]) > 1:
            return True
        else:
            return False

    @staticmethod
    def getShengmu(pinyin):
        pinyin = as_text(pinyin)
        if len(pinyin) == 0:
            return None
        elif len(pinyin) == 1:
            if pinyin in PinyinHelper.SHENGMU:
                return pinyin
            else:
                return None
        else:
            if pinyin[:2] in PinyinHelper.SHENGMU:
                return pinyin[:2]
            elif pinyin[:1] in PinyinHelper.SHENGMU:
                return pinyin[:1]
            else:
                return None


class ChineseHelper(object):

    initialized = False
    FAN2JIAN_TABLE = None
    JIAN2FAN_TABLE = None

    @staticmethod
    def isChinese(s):
        s = as_text(s)
        return all(u'\u4e00' <= c <= u'\u9fff' or c == u'〇' for c in s)

    @staticmethod
    def loadTable():
        if not ChineseHelper.initialized:
            ChineseHelper.FAN2JIAN_TABLE, ChineseHelper.JIAN2FAN_TABLE = PinyinResource.getChineseResource()
            ChineseHelper.initialized = True

    @staticmethod
    def convertToTraditionalChinese(s):
        ChineseHelper.loadTable()
        s = as_text(s)
        result = ''
        for c in s:
            if c in ChineseHelper.JIAN2FAN_TABLE:
                result += ChineseHelper.JIAN2FAN_TABLE[c]
            else:
                result += c
        return result

    @staticmethod
    def convertToSimplifiedChinese(s):
        ChineseHelper.loadTable()
        s = as_text(s)
        result = ''
        for c in s:
            if c in ChineseHelper.FAN2JIAN_TABLE:
                result += ChineseHelper.FAN2JIAN_TABLE[c]
            else:
                result += c
        return result