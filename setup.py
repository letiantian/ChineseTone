# coding: utf-8

from distutils.core import setup

LONGDOC = """
Please go to https://github.com/someus/ChineseTone for more info.  

ChineseTone主要功能是将汉字转为拼音，兼容Python2、Python3，支持多音字。

具体使用方法见 https://github.com/someus/ChineseTone 。
"""

setup(
    name='ChineseTone',
    version='0.1.4',
    description='汉字转换为拼音，支持多音字',
    long_description=LONGDOC,
    author='Letian Sun',
    author_email='sunlt1699@gmail.com',
    url='https://github.com/someus/ChineseTone',
    classifiers=[
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='NLP,Chinese,Tone',
    packages=['ChineseTone'],
    package_dir={'ChineseTone':'ChineseTone'},
    package_data={'ChineseTone':['*.py', 'data/*.db']},
)