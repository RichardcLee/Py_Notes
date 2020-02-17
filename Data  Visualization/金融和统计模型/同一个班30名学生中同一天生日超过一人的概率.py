import numpy as np
'''
一个班30名学生，至少有两位同一天生日的概率是多少？
假定不是闰年，不用月和日表示生日，只用日历年的天数，即365天。
'''

numStudents = 30
numTrials = 10000   # 试验次数
numWithSameBDay = 0

for trial in range(numTrials):
    year = [0]*365
    for i in range(numStudents):
        newBDay = np.random.randint(365)
        year[newBDay] = year[newBDay] + 1

    haveSameBDay = False

    # 因为题目中只要求至少，所以不必统计相同的人数
    for num in year:
        if num > 1:
            haveSameBDay = True

    if haveSameBDay == True:
        numWithSameBDay += 1

prob = float(numWithSameBDay)/float(numTrials)
print('the probability of a shared birthday in a class of ', numStudents, " is ", prob)

