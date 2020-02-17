import csv
from math import pow, sqrt
import matplotlib.pyplot as plt

count = 0
x = []  # shape
y = []  # weight
z = []  # color:fruit

with open('fruits_data.csv', 'r') as csvf:
    reader = csv.reader(csvf, delimiter=',')
    for row in reader:
        if count > 0:
            x.append(float(row[0]))
            y.append(float(row[1]))
            if row[2] == 'Apple':
                z.append('r')
            elif row[2] == 'Pear':
                z.append('g')
            else:
                z.append('y')
        count += 1
# print(x, y, z)

plt.figure(figsize=(8, 6))

classes = ['Apples', 'Pear', 'Bananas']
class_colours = ['r', 'g', 'y']

plt.title('Apples, Bananas and Pear by Weight and Shape', fontsize=14)
plt.xlabel('Shape category number', fontsize=12)
plt.ylabel('Weight in ounces', fontsize=12)
plt.xticks([i for i in range(0, 7, 1)])
plt.yticks([i for i in range(4, 11, 1)])

# 已有数据
plt.scatter(x, y, s=300, c=z, edgecolors='black')
# plt.legend(['Apple', 'Pear', 'Banana'], loc='best')


# knn
def determineFruit(xv, yv, threshold_redius):
    dist = []
    for i in range(1, len(x)):
        xdif = pow(x[i] - xv, 2)
        ydif = pow(y[i]- yv, 2)
        sqrtdist = sqrt(xdif+ydif)
        if xdif < threshold_redius and ydif < threshold_redius and sqrtdist < threshold_redius:
            dist.append(sqrtdist)
        else:
            dist.append(sqrtdist)
    pear_count = 0
    apple_count = 0
    banana_count = 0
    for i in range(1, len(dist)):
        if dist[i] < threshold_redius:
            if z[i] == 'g':
                pear_count += 1
            if z[i] == 'r':
                apple_count += 1
            if z[i] == 'y':
                banana_count += 1

    if apple_count >= pear_count and apple_count >= banana_count:
        return 'Apple'
    elif pear_count >= apple_count and pear_count >= banana_count:
        return 'Pear'
    elif banana_count >= apple_count and banana_count >= pear_count:
        return 'Banana'


# 待分类数据
data = [(3.5, 5.6, 1), (2.75, 6.2, 0.5), (2.9, 7.6, 0.7), (2.4, 7.0, 0.6), (4.0, 7.5, 1)]
lab = ['A', 'B', 'C', 'D', 'E']
plt.scatter(*[list(map(lambda xx: xx[0], data)), list(map(lambda yy: yy[1], data))], s=300, c='k')

for i, d in enumerate(data):
    plt.annotate(s=lab[i], xy=list(map(lambda x: x-0.05, d[:-1])), color='w')
    determine = determineFruit(*d)
    print(lab[i], d, ': ', determine)


plt.show()