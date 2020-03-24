from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.preprocessing import MinMaxScaler

reflection = {  # 转换关系
    b'didntLike': 0,
    b'smallDoses': 1,
    b'largeDoses': 2
}

min_max = MinMaxScaler()    # 最大最小值归一化


# 将要读取的数据中的字符串数据转换为int型数据，参照转换关系
def str2int(s):
    return reflection[s]


def load_meeting_data(path):
    '''
    "读取数据，并分割出测试集和训练集"
    :param path: 数据文件的路径
    :return:
    '''
    data = np.loadtxt(path, converters={-1: str2int})   # 读取同时转换数据
    X_train, y_train = data[:900, :-1], data[:900, -1]  # 训练数据
    return train_test_split(X_train, y_train, random_state=0, stratify=y_train, test_size=0.25)


def data_preprocessing(*data):
    X_train, X_test, y_train, y_test = data
    X_train = min_max.fit_transform(X_train)
    X_test = min_max.transform(X_test)
    return X_train, X_test, y_train, y_test


def test_model(clf, X_test, y_test):
    print('testing score: ', clf.score(X_test, y_test))


def KNN_train(*data):
    X_train, X_test, y_train, y_test = data_preprocessing(*data)
    clf = KNeighborsClassifier()
    clf.fit(X_train, y_train)
    test_model(clf, X_test, y_test)
    return clf


def my_app(clf):
    data = np.loadtxt('./datingTestSet.txt', converters={-1: str2int})[900:]
    X_predict, y_predict = data[:, :-1], data[:, -1]
    X_predict = min_max.transform(X_predict)
    res = clf.predict(X_predict)
    print('score: ', clf.score(X_predict, y_predict))


if __name__ == '__main__':
    path = './datingTestSet.txt'
    X_train, X_test, y_train, y_test = load_meeting_data(path)
    clf = KNN_train(X_train, X_test, y_train, y_test)

    my_app(clf)

    # X_predict, y_target = data[900:, :-1], data[900:, -1]   # 待预测的数据
