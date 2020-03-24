from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d


# 加载数据集
def loadDataSet(filename):
    dataMat = []; labelMat = []
    fr=open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return array(dataMat), array(labelMat)


if __name__ == "__main__":
    data, target = loadDataSet("testSetRBF2.txt")
    index1 = where(target == 1)
    X1 = data[index1]
    index2 = where(target == -1)
    X2 = data[index2]
    # 二维空间画图
    plt.plot(X1[:,0],X1[:,1],'ro')
    plt.plot(X2[:,0],X2[:,1],'bx')
    # plt.show()
    # 转换为三维空间，a=x^2,b=x*y,c=y^2
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.scatter(X1[:, 0]**2, X1[:, 0]*X1[:, 1], X1[:, 1]**2, c='r', marker='o')
    ax.scatter(X2[:, 0]**2, X2[:, 0]*X2[:, 1], X2[:, 1]**2, c='b', marker='x')
    plt.show()
