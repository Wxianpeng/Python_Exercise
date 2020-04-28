# coding=utf-8
import jieba
import jieba.posseg as pseg
import time

t1 = time.time()
f = open("dataFilter1.txt", "r", encoding='utf-8')  # 读取文本
string = f.read()
words = pseg.cut(string)  # 进行分词
result = ""  # 记录最终结果的变量
for w in words:
    result += str(w.word) + " "
f = open("分词.txt", "w", encoding='utf-8')  # 将结果保存到另一个文档中
f.write(result)
f.close()
t2 = time.time()
print("分词及词性标注完成，耗时：" + str(t2 - t1) + "秒。")  # 反馈结果


with open("分词.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
