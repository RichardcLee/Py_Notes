from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os


def load_data(file_path: str, test_size: float=0.25):
    '''
    加载手写体数据，并分割出测试集和训练集
    :param file_path: 特征文件路径
    :param test_size: 测试集占比
    :return: 返回test_size:(1-test_size)的测试集和训练集，形如：X_train, X_test, y_train, y_test
    '''
    data = np.loadtxt(file_path)
    X, y = data[:, :-1], data[:, -1]
    return train_test_split(X, y, test_size=test_size, stratify=y)


def train_model(*data, neighbors: int=3):
    '''
    训练模型
    :param data:  X_train, X_test, y_train, y_test，但是只是使用 X_train，y_train 即训练集的特征和标签
    :param neighbors: k值
    :return: 返回训练好的模型
    '''
    X_train, _, y_train, _ = data
    clf = KNeighborsClassifier(n_neighbors=neighbors)
    clf.fit(X_train, y_train)   # 训练
    return clf


def test_my_model(clf, X_test:np.ndarray, y_test: np.ndarray):
    '''
    模型测试
    :param clf: 训练好的模型
    :param X_test: 测试集特征
    :param y_test:  测试集标签
    :return: 返回并输出测试score
    '''
    score = clf.score(X_test, y_test)
    print('testing set score:', score)
    return score


def my_app(clf, pic_path):
    '''
    :param clf: 训练好的模型
    :param pic_path:　待分类图像的路径
    :return:
    '''
    from dataPreprocessing_and_featureExtract import load_picture
    success, failed = 0, 0
    for pic in os.listdir(pic_path):
        img = load_picture(pic_path+'/'+pic)    # 加载图像并二值化
        img = img.reshape((1, 64))
        res = clf.predict(img)
        if int(pic.split('_')[0]) == int(res[0]):
            success += 1
        else:
            failed += 1
        print(pic, res)
    print('Precision is : %f' % (success / (success + failed)))


if __name__ == '__main__':
    # 加载数据，分割得测试集和训练集
    X_train, X_test, y_train, y_test = load_data('./train_data.txt')
    # 使用训练集训练模型
    clf = train_model(X_train, X_test, y_train, y_test, neighbors=3)
    # 使用测试集测试模型
    test_my_model(clf, X_test, y_test)
    # 模型应用

    old_path = './target_picture'
    my_app(clf, old_path)

    # 多次重复取最合适的k值

    # 训练多个较好的模型，多次预测取比例最高的为预测结果，如出现　８　９　８，取结果为　８

