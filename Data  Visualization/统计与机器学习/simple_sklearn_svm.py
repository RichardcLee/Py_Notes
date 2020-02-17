import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


X = np.sort(5 * np.random.rand(40, 1), axis=0)
Y = (np.cos(X) + np.sin(X)).ravel()
Y[::5] += 3 * (0.5 - np.random.rand(8))
# print(X)
# print(Y)

svr_rbfmodel = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_linear = SVR(kernel='linear', C=1e3)
svr_polynom = SVR(kernel='poly', C=1e3, degree=2)
y_rbfmodel = svr_rbfmodel.fit(X, Y).predict(X)
y_linear = svr_linear.fit(X, Y).predict(X)
y_polynom = svr_polynom.fit(X, Y).predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(X, Y, c='k', label='data')
# plt.hold('on')
plt.plot(X, y_rbfmodel, c='g', label='RBF model')
plt.plot(X, y_linear, c='r', label='linear model')
plt.plot(X, y_polynom, c='b', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support vector Regression')
plt.legend()
plt.show()
