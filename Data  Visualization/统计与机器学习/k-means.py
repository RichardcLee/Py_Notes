# -*- encode utf-8 -*-
# k个初始类聚类中心点的选取对聚类结果具有较大的影响
import math
from random import randint
from functools import reduce
from matplotlib import pyplot as plt
from copy import deepcopy


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


# 随机选k个点作为簇心
def randCent(dataSet, k):
    centroid, max_len = [], len(dataSet)
    while len(centroid) < k:
        i = randint(0, max_len-1)
        while dataSet[i] in centroid:
            i = randint(0, max_len - 1)
        centroid.append(dataSet[i])
    return centroid


def compare(data, core):
    '''
    计算单个数据data与所有簇心的距离，返回最小距离的簇心，注意这里采用的是欧几里得距离
    :param data: 单个数据元组
    :param core: 簇心集合
    :return: 最近的簇心
    '''
    min_distance, min_index = 10e10000, -1
    for index, c in enumerate(core):
        temp = [[data[i], c[i]] for i in range(len(data))]
        # print(temp)
        distance = math.sqrt(sum(list(map(lambda x: (x[0] - x[1])**2, temp))))
        # print(index, distance)
        if min_distance > distance:
            min_distance, min_index = distance, index
    # print('min-dis:', min_distance)
    return min_index, min_distance


def k_means(k, dataSet):
    '''
    k-means
    :param k: 初始选取k个簇心
    :param dataSet: 形如[(A, B, C, D, ...), ...] 十三维的元组集，这里要用list代替tuple
    :return: 簇心和分类结果
    输入：k, dataSet[n];
    （1） 选择k个初始中心点，例如c[0]=dataSet[0],…c[k-1]=dataSet[k-1]；
    （2） 对于dataSet[0]….dataSet[n]，分别与c[0]…c[k-1]比较，假定与c[i]差值最少，就标记为i；
    （3） 对于所有标记为i点，重新计算c[i]={ 所有标记为i的dataSet[j]之和}/标记为i的个数；
    （4） 重复(2)(3)，直到所有c[i]值的变化小于给定阈值。
    '''
    data_len = len(dataSet[0])
    print('数据维度: ', data_len)
    centroids = randCent(dataSet, k)     # 随机选取的簇心
    rand_centroids = deepcopy(centroids)
    # print('初始随机选取的簇心: ', centroids)
    clusterAssment = [[-1, -1] for i in range(len(dataSet))]   # 记录每个数据元组所属的簇心和距离簇心的距离
    cluster_changed = True
    while cluster_changed is True:  # 只要簇心还再变化就继续聚集
        cluster_changed = False
        for i, d in enumerate(dataSet):
            min_index, min_distance = compare(d, centroids)
            if min_index != clusterAssment[i][0]:
                cluster_changed = True
                clusterAssment[i][:] = min_index, min_distance
        # print('centroid:', centroids)
        # print('clusterAssment', clusterAssment)
        # 重新计算簇心（即每个簇的均值）
        cluster = [[] for i in range(k)]  # 表示每个簇包含的所有data元组
        for index, ass in enumerate(clusterAssment):
            cluster[ass[0]].append(dataSet[index])
        # print('cluster:', cluster)
        for i, c in enumerate(cluster):
            if not c == []:
                res = reduce(lambda x, y: [x[i]+y[i] for i in range(data_len)], c)
                res = list(map(lambda x: x / len(c), res))
            else:
                continue
            centroids[i] = res
        # print('new_centroid:', centroids)
    return rand_centroids, centroids, clusterAssment, cluster


def random_data(num=100, dimension=3, rand_range=(0, 40)):
    s, e = rand_range
    with open('k-mean-data', 'w+', encoding='utf-8') as f:
        for i in range(num):
            num_list = [(randint(s + 1, e - 1)) for i in range(dimension)]
            out = ''
            for rand_num in num_list:
                out += str(rand_num) + ','
            f.write('(' + out.rstrip(",") + ')\n')


if __name__ == '__main__':
    def D2_DataSet():
        # 图一
        x, y = [i[0] for i in dataSet], [i[1] for i in dataSet]
        z, w = [i[0] for i in rc], [i[1] for i in rc]
        f1 = plt.figure(num=1, figsize=(8, 5))
        plt.xlim((0, 50)); plt.ylim((0, 50))
        plt.xticks(range(0, 51, 5)); plt.yticks(range(0, 51, 5))
        plt.plot(x, y, 'b.', z, w, 'ro')
        plt.grid(True)
        plt.title('region DataSet with region centroid')
        f1.savefig('2Df1.jpg')
        # 图二
        f2 = plt.figure(num=2, figsize=(8, 5))
        plt.xlim((0, 50));plt.ylim((0, 50))
        plt.xticks(range(0, 51, 5));plt.yticks(range(0, 51, 5))
        plt.grid(True)
        plt.title('after k-means process on  DataSet')
        color = ['r.', 'g.', 'b.', 'm.', 'c.', 'y.']
        # color = ['ro', 'go', 'bo', 'mo', 'co', 'yo']
        for i, c in enumerate(cluster):
            x = list(map(lambda t: t[0], c))
            y = list(map(lambda t: t[1], c))
            plt.plot(x, y, color[i])
        z, w = [i[0] for i in centroids], [i[1] for i in centroids]
        plt.plot(z, w, 'ko')
        f2.savefig('2Df2.jpg')

        plt.show()

    def D3_DataSet():
        from mpl_toolkits import mplot3d
        # 图一
        x, y, z = [i[0] for i in dataSet], [i[1] for i in dataSet], [i[2] for i in dataSet]
        u, v, w = [i[0] for i in rc], [i[1] for i in rc], [i[2] for i in rc]
        f1 = plt.figure(num=1, figsize=(10, 7), dpi=72)
        plt.xlim((0, 1000));plt.ylim((0, 1000))
        plt.xticks(range(0, 1001, 50));plt.yticks(range(0, 1001, 50))
        plt.title('region DataSet with region centroid')
        ax = plt.axes(projection='3d')
        ax.plot3D(x, y, z, 'b.');ax.plot3D(u, v, w, 'ro-')
        f1.savefig('3Df1.jpg')

        # 图二
        f2 = plt.figure(num=2, figsize=(10, 7), dpi=72)
        ax = plt.axes(projection='3d')
        plt.xlim((0, 1000));plt.ylim((0, 1000))
        plt.xticks(range(0, 1001, 100));plt.yticks(range(0, 1001, 100))
        plt.title('after k-means process on  DataSet')
        color = ['r.', 'g.', 'b.', 'm.', 'c.', 'y.']
        # color = ['ro', 'go', 'bo', 'mo', 'co', 'yo']
        for i, c in enumerate(cluster):
            x, y, z = list(map(lambda t: t[0], c)), list(map(lambda t: t[1], c)), list(map(lambda t: t[2], c))
            ax.plot3D(x, y, z, color[i])
        x, y, z = [i[0] for i in centroids], [i[1] for i in centroids], [i[2] for i in centroids]
        ax.plot3D(x, y, z, 'ko-')
        f2.savefig('3Df2.jpg')

        plt.show()
    '''
    start from here
    '''
    # random_data(1000, dimension=2, rand_range=(0, 50))   # 生成随机数据
    random_data(4000, 3, (0, 1000))
    dataSet = load_data('k-mean-data')  # 读取数据
    print('dataSet: ', dataSet)
    k = 6; rc, centroids, clusterAssment, cluster = k_means(k, dataSet)
    print('初始随机选取的簇心:', rc)
    print('簇心:', centroids)
    print('分布:', clusterAssment)
    print('簇:', cluster)
    # D2_DataSet()
    D3_DataSet()
