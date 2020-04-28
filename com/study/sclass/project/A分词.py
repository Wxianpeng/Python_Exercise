#!-*-coding:utf-8-*-
# encoding=utf-8
import jieba
import jieba.analyse

import re

import io
import sys



# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 待分词的路径
sourceTxt = 'dataFilter1.txt'
# 分好词的路径
targetTxt = 'A分词.txt'

with open(sourceTxt, 'r', encoding='utf-8') as sourceFile, open(targetTxt, 'a+', encoding='utf-8') as targetFile:
    for line in sourceFile:

        # 这句话去掉 所有中文标点符号
        subline = re.sub('\W', '', line)
        seg = jieba.cut(subline, cut_all=True)
        output = '  '.join(seg)
        targetFile.write(output)
        targetFile.write('\n')

print('写入成功！')

with open(targetTxt, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
