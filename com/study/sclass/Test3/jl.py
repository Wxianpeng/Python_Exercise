import jieba
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import csv
# 'baidu_stopwords.csv'
# 'dataFilter11.csv'


# 加载数据
def load_data(data_path, stopwords_path):
    # 加载停用词
    stopwords = pd.read_csv(stopwords_path, index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
    stopwords = stopwords['stopword'].values

    # 加载语料
    data_df = pd.read_csv(data_path, encoding='utf-8', sep=',')

    # 删除语料的nan行
    data_df.dropna(inplace=True)
    # 转换成list
    return data_df.values.tolist(), stopwords


# 定义分词函数preprocess_text
# 参数content_lines即为data
# 参数sentences是定义的空list，用来储存分词后的数据
def preprocess_text(content_lines, stopwords):
    sentences = []
    for line in content_lines:
        try:
            segs = jieba.lcut(str(line))
            segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
            segs = list(filter(lambda x: len(x) > 1, segs))  # 长度为1的字符
            segs = list(filter(lambda x: x not in stopwords, segs))  # 去掉停用词
            sentences.append(" ".join(segs))
        except Exception:
            print(line)
            continue
    return sentences


def tf_idf(sentences):
    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
    # 统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(sentences))
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()
    return weight


def draw(clf):
    from sklearn.manifold import TSNE
    tsne = TSNE(n_components=2)
    decomposition_data = tsne.fit_transform(weight)

    x = []
    y = []

    for i in decomposition_data:
        x.append(i[0])
        y.append(i[1])

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()
    plt.scatter(x, y, c=clf.labels_, marker="x")
    plt.xticks(())
    plt.yticks(())
    # plt.show()
    plt.savefig('sample.png', aspect=1)


def save_data(labels):
    for o in range(np.max(labels) + 2):
        k = []
        for j in range(len(labels)):
            if labels[j] == o - 1:
                k.append(data[j])

        f = open('分类/' + str(o) + '.txt', 'w', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerows(k)
        f.close


data, stopwords = load_data(data_path='dataFilter11.csv', stopwords_path='baidu_stopwords.csv')
sentences = preprocess_text(data, stopwords)
weight = tf_idf(sentences)

clf = DBSCAN(eps=0.01,  # 邻域半径
             min_samples=20,  # 最小样本点数，MinPts
             metric='euclidean',
             metric_params=None,
             algorithm='auto',  # 'auto','ball_tree','kd_tree','brute',4个可选的参数 寻找最近邻点的算法，例如直接密度可达的点
             leaf_size=30,  # balltree,cdtree的参数
             p=None,  #
             n_jobs=1)

labels = clf.fit_predict(weight)
draw(clf)
save_data(labels)
