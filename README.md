# Hanzi2Pinyin （汉字转拼音）

Hanzi2Pinyin是[jpinyin](https://github.com/stuxuhai/jpinyin)的Python实现（略有改动），主要功能是将汉字转为拼音，兼容Python2、Python3，支持多音字。



## 安装

方式1：
```
$ python setup.py install --user
```

方式2：
```
$ sudo python setup.py install
```


## 汉字转拼音

#### 基本使用


```python
from Hanzi2Pinyin import *

print PinyinHelper.convertToPinyinFromSentence('了解了')
# 输出：[u'li\u01ceo', u'ji\u011b', u'le']

print '/'.join(PinyinHelper.convertToPinyinFromSentence('了解了'))
# 输出：liǎo/jiě/le

print PinyinHelper.convertToPinyinFromSentence('了解了', pinyinFormat=PinyinFormat.WITH_TONE_MARK)
# 输出：[u'li\u01ceo', u'ji\u011b', u'le']

print PinyinHelper.convertToPinyinFromSentence('了解了', pinyinFormat=PinyinFormat.WITH_TONE_NUMBER)
# 输出：[u'lia3o', u'jie3', u'le']

print PinyinHelper.convertToPinyinFromSentence('了解了', pinyinFormat=PinyinFormat.WITHOUT_TONE)
# 输出：[u'liao', u'jie', u'le']
```

__第一个参数必须是unicode类型，或者utf-8编码的字符串。__


非中文字符保持不变：

```python
print PinyinHelper.convertToPinyinFromSentence('了解了，Mike', pinyinFormat=PinyinFormat.WITHOUT_TONE)
# 输出：[u'liao', u'jie', u'le', u'\uff0c', u'M', u'i', u'k', u'e']
```

可以用指定的字符作为非中文字符的输出：
```python
print PinyinHelper.convertToPinyinFromSentence('了解了，Mike', pinyinFormat=PinyinFormat.WITHOUT_TONE, replace='%')
# 输出：[u'liao', u'jie', u'le', u'%', u'%', u'%', u'%', u'%']
```

某些情况下，为了保证准确性，可以指定一个分词函数，该函数必须返回一个可迭代对象，例如下面的cut函数：

```python
import jieba

def cut(s):
    return jieba.cut(s, cut_all=False)

for word in cut('我来到北京清华大学,mike'):
    print word

'''输出
我
来到
北京
清华大学
,
mike
'''
```

使用segment参数指定分词函数：

```python
import jieba

def cut(s):
    return jieba.cut(s, cut_all=False)

print PinyinHelper.convertToPinyinFromSentence('我来到北京清华大学', pinyinFormat=PinyinFormat.WITHOUT_TONE, segment=cut)
# 输出：[u'wo', u'lai', u'dao', u'bei', u'jing', u'qing', u'hua', u'da', u'xue']
```

#### 获取某汉字的所有拼音
```python
print PinyinHelper.convertToPinyinFromChar('了')
# 输出：[u'le', u'li\u01ceo']

print PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITH_TONE_MARK)
# 输出：[u'le', u'li\u01ceo']

print PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITH_TONE_NUMBER)
# 输出：[u'le', u'lia3o']

print PinyinHelper.convertToPinyinFromChar('了', PinyinFormat.WITHOUT_TONE)
# 输出：[u'le', u'liao']

print PinyinHelper.convertToPinyinFromChar('了解')
# 输出：[u'\u4e86\u89e3']  # 即“了解”

print PinyinHelper.convertToPinyinFromChar('12')
# 输出：[u'12']
```

#### 判断是否为多音字

```python
print PinyinHelper.hasMultiPinyin('了')
# 输出：True

print PinyinHelper.hasMultiPinyin('你')
# 输出：False
```

#### 获取拼音的声母部分

```python
print PinyinHelper.getShengmu('ni')
# 输出：n

print PinyinHelper.getShengmu('sheng')
# 输出：sh

print PinyinHelper.getShengmu('en')
# 输出：None
```

#### 是否全部是汉字

```python
print ChineseHelper.isChinese('n')
# 输出：False

print ChineseHelper.isChinese('你好')
# 输出：True

print ChineseHelper.isChinese('hi，小王')
# 输出：False
```

#### 简/繁转换
实现得比较简单。

```python
print ChineseHelper.convertToTraditionalChinese('hi，你好，我来到了北京天安门')
# 输出：hi，你好，我來到了北京天安門

print ChineseHelper.convertToSimplifiedChinese('hi，你好，我來到了北京天安門')
# 输出：hi，你好，我来到了北京天安门
```

## 相关项目

* jpinyin: https://github.com/stuxuhai/jpinyin
* pinyin: https://github.com/hotoo/pinyin
* pypinyin: https://github.com/mozillazg/python-pinyin



