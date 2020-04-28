# encoding = gbk
# coding=gbk

# 结巴
import jieba
# 自然语言
import nltk
import re

f = open(r'data.txt', 'r', encoding='utf-8')
tmp_string = f.read()
f.close()

tmp_string = re.sub(r"[0-9+\.\!\/,$%^()?;: :-【】±\"\']+|[+——!,;:。？、~@#￥%......&*（）]+", "", tmp_string)
tmp_string = re.sub('[评价id评价内容是的在了和\n]', '', tmp_string)
lst_word = list((jieba.cut(tmp_string)))
print(lst_word)
# frequese 频率Dist
worded = nltk.FeatDict(lst_word)
worded.print(30)
# worded.plot(30 )
