stop = []
standard_stop = []
text = []
after_text = []
# 停用词表
file_stop = r'hit_stopwords.txt'
# 要处理的文本文件
file_text = r'A分词.txt'

with open(file_stop, 'r', encoding='utf-8') as f:
    lines = f.readline()  # lines是list的类型
    for line in lines:
        lline = line.strip()  # line是str类型，strip去掉\n换行符
        stop.append(lline)  # 将stop为列表形式

#  stop 的元素是一行一行的句子，需要进行转化为一个词一行，即下面：
for i in range(0, len(stop)):
    for word in stop[i].split():
        standard_stop.append(word)
# print(standard_stop)

# 读取文本集
with open(file_text, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        # lline = line.strip()
        # print(lines)
        lline = line.split()
        # print(lline)
        for i in line:
            if i not in standard_stop:
                after_text.append(i)
print(after_text)

# 将结果保存在txt中
with open(r'B文本分析-停用词表.txt', 'w+', encoding="utf-8")as f:
    for i in after_text:
        f.write(i)
print('B文本分析—停用词表')
