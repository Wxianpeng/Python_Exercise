#!-*-coding:utf-8-*-
# encoding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 导入词云制作第三方库wordcloud
import wordcloud

# 从外部.txt文件中读取大段文本，存入变量txt中
f = open('0.txt', encoding='utf-8')
txt = f.read()

# 创建词云对象，赋值给w，现在W就表示了一个词云对象，设置词云图片宽、高、字体、背景颜色等参数 ,font path='msyh.ttc'
w = wordcloud.WordCloud(width=1000, height=700, background_color='white')

# 调用词云对象的generate方法，将文本传入
w.generate(txt)

# 将生成的词云保存为output1.png图片文件，保存到当前文件夹中
w.to_file('output2.png')
