#!-*-coding:utf-8-*-
# encoding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# �������������������wordcloud
import wordcloud

# ���ⲿ.txt�ļ��ж�ȡ����ı����������txt��
f = open('0.txt', encoding='utf-8')
txt = f.read()

# �������ƶ��󣬸�ֵ��w������W�ͱ�ʾ��һ�����ƶ������ô���ͼƬ���ߡ����塢������ɫ�Ȳ��� ,font path='msyh.ttc'
w = wordcloud.WordCloud(width=1000, height=700, background_color='white')

# ���ô��ƶ����generate���������ı�����
w.generate(txt)

# �����ɵĴ��Ʊ���Ϊoutput1.pngͼƬ�ļ������浽��ǰ�ļ�����
w.to_file('output2.png')
