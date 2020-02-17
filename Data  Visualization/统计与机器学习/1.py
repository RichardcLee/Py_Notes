import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
'''
一种简单场景是在GPA得分和SAT得分数据的基础上，预测一个学生是否有可能被大学生本科培养计划接受
'''

mpl.rcParams['axes.facecolor'] = '#f8f8f8'
mpl.rcParams['grid.color'] = '#303030'
# mpl.rcParams['grid.color'] = '#303030'
mpl.rcParams['grid.linestyle'] = '--'
# SAT Score
x = [2400, 2350, 2400, 2290, 2100, 2380, 2300, 2280, 2210, 2390]

# High school GPA
y = [4.4, 4.5, 4.2, 4.3, 4.0, 4.1, 3.9, 4.0, 4.3, 4.5]

a = '#6D0000'
r = '#00006f'
# Acceptance or rejections score
z = [a, a, a, r, r, a, r, r, a, a]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=z, s=600)

# To see where the separation lies
for i in range(1, 5):
    x_plot = np.linspace(2490-i*2, 2150+i*2, 20)
    y_plot = np.linspace(3.3+i*0.2, 5-0.2*i, 20)
    plt.plot(x_plot, y_plot, c='gray')

plt.grid(True)

plt.xlabel('SAT Score', fontsize=18)
plt.xlabel('GPA', fontsize=18)
plt.title('Acceptance in College', fontsize=20)
plt.legend()

plt.show()