# coding: utf-8

from distutils.core import setup

LONGDOC = """
Please go to https://github.com/someus/ChineseTone for more info.
"""

setup(
    name='ChineseTone',
    version='0.1.0',
    description='将汉字转换为拼音',
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