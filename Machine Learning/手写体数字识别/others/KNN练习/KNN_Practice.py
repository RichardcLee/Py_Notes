from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split


def load_classification_data():
    digits = datasets.load_digits()
    X_train = digits.data
    y_train = digits.target
    return train_test_split(X_train, y_train, random_state=0, test_size=0.25, stratify=y_train)


def test_KNeighborsClassifier(*data):
    X_train, X_test, y_train, y_test = data
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)
    print('Training Score: %f', clf.score(X_train, y_train))
    print('Testing Score: %f', clf.score(X_test, y_test))


if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_classification_data()
    test_KNeighborsClassifier(X_train, X_test, y_train, y_test)