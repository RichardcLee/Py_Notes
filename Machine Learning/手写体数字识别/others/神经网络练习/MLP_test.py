import numpy as np
import matplotlib.pyplot as plt
from sklearn import neural_network, datasets


np.random.seed(0)
iris = datasets.load_iris()
# 使用萼片长度和宽度两个特征
X = iris.data[:, :2]; Y = iris.target
data = np.hstack((X, Y.reshape((Y.size, 1))))
np.random.shuffle(data)     # 打乱样本顺序
X = data[:, :-1]; Y = data[:, -1]
train_x = X[:-30]; test_x = X[-30:]
train_y = Y[:-30]; test_y = Y[-30:]


def mlpclassifier_iris():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    classifier = neural_network.MLPClassifier(activation='logistic', max_iter=10000, hidden_layer_sizes=(30, ))
    classifier.fit(train_x, train_y)
    train_score = classifier.score(train_x, train_y)
    test_score = classifier.score(test_x, test_y)
    x_min, x_max = train_x[:, 0].min() - 1, train_x[:, 0].max() + 2
    y_min, y_max = train_x[:, 1].min() - 1, train_x[:, 1].max() + 2
    plot_classifier_predict_meshgrid(ax, classifier, x_min, x_max, y_min, y_max)
    plot_samples(ax, train_x, train_y)
    ax.legend(loc='best')
    ax.set_xlabel(iris.feature_names[0])
    ax.set_ylabel(iris.feature_names[1])
    ax.set_title('train score:%f; test score:%f' % (train_score, test_score))
    plt.show()


def plot_samples(ax, x, y):
    n_class = 3
    plot_colors = "bry"
    for i, color in zip(range(n_class), plot_colors):
        idx = np.where(y == i)
        ax.scatter(x[idx, 0], x[idx, 1], c=color, label=iris.target_names[i], cmap=plt.cm.Paired)


def plot_classifier_predict_meshgrid(ax, clf, x_min, x_max, y_min, y_max):
    plot_step = 0.02
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=plt.cm.Paired)


mlpclassifier_iris()