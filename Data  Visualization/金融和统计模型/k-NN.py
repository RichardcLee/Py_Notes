from numpy import random, argsort, sqrt
from pylab import plot, show
import matplotlib.pyplot as plt

'''
    k-最近邻算法不从训练集数据建立模型（无监督学习）。
    它逐一比较无标签数据和每一个有标签数据。
    然后，取最相似的数据部分（最近的邻居），并查看其标签。
    现在，从已知的数据集中取前k条最相似的数据（k为整数，并且通常小于20）。
'''


def knn_search(x, data, K):
    """ k nearest neighbors """
    ndata = data.shape[1]
    K = K if K < ndata else ndata
    # euclidean distances from the other points
    sqd = sqrt(((data - x[:, :ndata])**2).sum(axis=0))
    idx = argsort(sqd)  # 排序后返回的原数组中数据的索引
    # return the indexes of K nearest neighbors
    return idx[:K]


data = random.rand(2, 200)  # 2rows 200columns，两列分别代表坐标x,y

x = random.rand(2, 1)   # 2rows 1columns, 两列分别代表坐标x,y

neig_idx = knn_search(x, data, 10)

plt.figure(figsize=(10, 8))

# plotting the data and the input point
plot(data[0, :], data[1, :], 'o', color='#9a88a1', alpha=0.6, markersize=20)
plot(x[0, 0], x[1, 0], 'r*', alpha=0.6, markersize=20)


# highlighting the neighbors
plot(data[0, neig_idx], data[1, neig_idx], 'o', markerfacecolor='#bbe4b4', alpha=0.6, markersize=22, markeredgewidth=1)

show()