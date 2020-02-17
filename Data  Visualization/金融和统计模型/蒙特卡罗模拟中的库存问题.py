import numpy as np
from math import log
import matplotlib.pyplot as plt


'''
销售员每天出售水果，每份订单有Y个单位。每卖出一个单位会有60美分利润，在一天结束时未售出的部分以每件40美分的损失抛售。
每天的需求D服从均匀分布[80, 140]。请问，为了使预期利润最大化，需要有多少单位的订单？

P：利润      s: 销售数量      d: 需求量（消费者）
P = { 0.6s              若 d >= s
    { 0.6d + 0.4(s-d)   若 s  > d
'''

x = []
y = []

#   Equation that defines Profit
def generateProfit(d):
    global s

    if d >= s:
        return 0.6*s
    else:
        return 0.6*d + 0.4*(s-d)


# although d comes from uniform distribution in [80, 140]
# we are running simulation s in [20, 305]

maxprofit = 0

for s in range(20, 305):
    # Run a simulation for n = 1000
    # Even if we run for n = 10,000 the result word be almost the same
    for i in range(1, 1000):
        # generate a random value of d
        d = np.random.uniform(80, high=140)
        # for this random value of d, find profit and update maxprofit
        profit = generateProfit(d)
        # print(d)
        if profit > maxprofit:
            maxprofit = profit

    # store the value of s to be plotted along X axis
    x.append(s)
    # store the value of maxprofit plotted along Y axis
    y.append(log(maxprofit))    # plotted on log scale
    # y.append(maxprofit)
    # print(s, log(maxprofit))

plt.plot(x, y)
plt.xlabel('Units Sold')
plt.ylabel('Max Profits (log)')
# print('Max profit:', maxprofit, 'loged Max profit:', log(maxprofit))
plt.show()








