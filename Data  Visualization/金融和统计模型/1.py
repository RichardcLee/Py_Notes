import matplotlib.pyplot as plt
'''
如果2010年投资10000，年收益率为6%，那么经过多少年投资价值会翻倍？
'''

# invested amount
principle_value = 10000
# Rt
grossReturn = 1.06

return_amt = []
x = []        # years
y = [10000]   # values
year = 2010
return_amt.append(principle_value)
x.append(year)

# 我们先看看投资价值能否在12年内翻一番
# 曲线一（参考线）：20000 = 10000 + 12*k --->> 斜率 k = 10000/12 = 833.33 --->> y = 833.33*x + 10000
# 曲线二（实际收益曲线）：return_amt = grossReturn^x * 10000
for i in range(1, 15):
    return_amt.append(return_amt[i-1] * 1.06)
    print('Year-', i, " Returned:", return_amt[i])

    year += 1
    x.append(year)
    y.append(833.33*(year-2010) + principle_value)

# set the grid to appear
plt.grid()

# plot the return values curve
plt.plot(x, return_amt, color='r')
plt.plot(x, y, color='b')

# 由图可知，2022年前达到翻倍
plt.show()


