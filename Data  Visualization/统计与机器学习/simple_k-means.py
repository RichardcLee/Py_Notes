import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
from random import randint


def random_data(num=100, dimension=3, rand_range=(0, 40)):
    s, e = rand_range
    with open('simple-k-means-data', 'w+', encoding='utf-8') as f:
        for i in range(num):
            num_list = [(randint(s + 1, e - 1)) for i in range(dimension)]
            out = ''
            for rand_num in num_list:
                out += str(rand_num) + ','
            f.write('(' + out.rstrip(",") + ')\n')


def load_data(file):
    dataSet = []
    with open(file, 'r+', encoding='utf-8') as f:
        temp = list(map(lambda x: x.replace("\n", "").replace("(", "").replace(")", "").replace(",", " "), f.readlines()))
        temp = list(map(str.split, temp))
        def convert(c):
            table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
            if c in table:
                return table.index(c)+1
            else:
                return int(c)
        for d in temp:
            dataSet.append(list(map(convert, d)))
    return dataSet

'''
以上只是为了生成随机的数据以及读取，不用管
'''

# random_data(200, 2)
dataSet = load_data('simple-k-means-data')
x, y = list(map(lambda _: _[0], dataSet)), list(map(lambda _: _[1], dataSet))
# print(x, y)

plt.figure(figsize=(8, 6))
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.xlabel('X values', fontsize=14)
plt.ylabel('Y values', fontsize=14)
plt.title('Before Clustering ', fontsize=20)
plt.plot(x, y, 'k.', color='#0080ff', markersize=25, alpha=0.6)

# 简单的一个调用，重点只在这里！！！
kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(dataSet)

plt.figure(figsize=(8, 6))
plt.xlim(0, 40)
plt.ylim(0, 40)
plt.xlabel('X values', fontsize=14)
plt.ylabel('Y values', fontsize=14)
plt.title('After Clustering ', fontsize=20)

colors = ['r', 'g', 'b']
data = {'r': [], 'g': [], 'b': []}
label = kmeans.labels_
for i in range(len(label)):
    if label[i] == 0:
        data['r'].append(dataSet[i])
    elif label[i] == 1:
        data['g'].append(dataSet[i])
    elif label[i] == 2:
        data['b'].append(dataSet[i])

for i in colors:
    x, y = list(map(lambda _: _[0], data[i])), list(map(lambda _: _[1], data[i]))
    plt.plot(x, y, 'k.', color=i, markersize=45, alpha=0.6)

centroids = kmeans.cluster_centers_

plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='b', zorder=10)

plt.show()

