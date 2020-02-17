from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

sample1 = np.random.normal(loc=-1.0, scale=1, size=320)
sample2 = np.random.normal(loc=2.0, scale=0.6, size=320)
sample = np.hstack([sample1, sample2])
probDensityFun = gaussian_kde(sample)
plt.title("KDE Demonstration using Scipy and Numpy", fontsize=20)
x = np.linspace(-5, 5, 200)
plt.plot(x, probDensityFun(x), 'r')
plt.hist(sample, normed=1, alpha=0.45, color='purple')
plt.show()