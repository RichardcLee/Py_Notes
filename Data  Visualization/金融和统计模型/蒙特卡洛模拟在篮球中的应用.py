import numpy as np
import matplotlib.pyplot as plt

'''
当落后3分且离比赛结束还有30s时，应该尝试投难度较大的3分球还是更容易的2分球后再控制下一个球？
'''

colors = [(31, 119, 180), (174, 199, 232), (255, 128, 0), (255, 15, 14), (44, 160, 44), (152, 223, 138), (214, 39, 40),
          (255, 173, 61), (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148), (227, 119, 194), (247, 182, 210),
          (127, 127, 127), (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207), (15, 218, 229), [217, 217, 217]]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r/255., g/255., b/255.)

# 让我们来尝试投3分球
def attemptThree():
    if np.random.randint(0, high=100) < threePtPercent:
        if np.random.randint(0, high=100) < overtimePercent:
            return True     # We won
    return False    # We either missed the 3 or lost in OT

# 选择投2分球与离比赛结束的时间，以及球在哪个球队有关。
# 假设平均意义上，尝试投2分球平均需要5秒，而且球员twoPtPercent的概率相当大，那么他们会得到2分球，并从pointsDown中扣除
# 尝试投2分球
def attemptTwo():
    havePossession = True   # 是否掌握控球权
    pointsDown = 3     # 分差
    timeLeft = 30   # 剩余时间
    while timeLeft > 0:
        # what to do if we have possession
        if havePossession:
            # If we are down by 3 or more, we take te 2 quickly.
            if pointsDown >= 3:
                timeLeft -= timeToShoot
            # If we are down by 2 or less, we run down the clock first
            else:
                timeLeft = 0

            # Do we make the shot?
            # yes we do
            if np.random.randint(0, high=100) < twoPtPercent:
                pointsDown -= 2
                havePossession = False
            # no
            else:
                # Does the opponent team rebound?
                # If so, we lose possession.
                # This doesn't really matter when we run the clock down
                if np.random.randint(0, high=100) >= offenseReboundPercent:
                    havePossession = False
                # else havePossession = True

        else:   # cases where we don't have possession
            if pointsDown > 0:  # foul to get back possession
                # takes time to foul
                timeLeft -= timeToFoul

                # opponent takes 2 free throws，对方站上罚球线
                if np.random.randint(0, high=100) <= oppFtPercent:
                    pointsDown += 1

                if np.random.randint(0, high=100) <= oppFtPercent:
                    pointsDown += 1
                    havePossession = True

            else:
                if np.random.randint(0, high=100) >= ftReboundPercent:
                    # you were able to rebound the missed ft
                    havePossession = True

                else:
                    # tied or up so don't want to foul;
                    # assume opponent to run out clock and take
                    if np.random.randint(0, high=100) < oppTwoPtPercent:
                        pointsDown += 2     # they made teh 2
                    timeLeft = 0

    if pointsDown > 0:
        return False
    else:
        if pointsDown < 0:
            return True
        else:
            if np.random.randint(0, high=100) < overtimePercent:
                return True
            else:
                return False


# 我们选择5名擅长3分球或2分球，或都擅长的球员
fig = plt.figure(figsize=(8, 8))
names = ['Lebron James', 'Kyrie Irving', 'Steph Curry', 'Kyle Krover', 'Dirk Nowitzki']
threePercents = [35.4, 46.8, 44.3, 49.2, 38.0]
twoPercents = [53.6, 49.1, 52.8, 47.0, 48.6]
colid = 0

xx = [[]]*5
yy1 = [[]]*5
yy2 = [[]]*5

for i in range(5):
    x = []
    y1 = []
    y2 = []
    trials = 400
    threePtPercent = threePercents[i]
    twoPtPercent = twoPercents[i]
    oppTwoPtPercent = 40    # opponent & chance making 2-pter
    oppFtPercent = 70
    timeToShoot = 5
    timeToFoul = 5
    offenseReboundPercent = 25
    ftReboundPercent = 15
    overtimePercent = 50    # overtime

    winsTakingThree = 0
    lossTakingThree = 0
    winsTakingTwo = 0
    lossTakingTwo = 0
    curTrial = 1

    while curTrial < trials:
        # run a trial take the 3
        if attemptThree():
            winsTakingThree += 1
        else:
            lossTakingThree += 1

        # run a trial take the 2
        if attemptTwo():
            winsTakingTwo += 1
        else:
            lossTakingTwo += 1

        x.append(curTrial)
        y1.append(winsTakingThree)
        y2.append(winsTakingTwo)
        curTrial += 1
    xx[i] = x
    yy1[i] = y1
    yy2[i] = y2

    ax = plt.subplot(231+i)
    ax.plot(x, y1, color=colors[colid], label=names[i]+" wins taking 3 pt", linewidth=2)
    ax.plot(x, y2, color=colors[20], label=names[i]+" wins taking 2 pt", linewidth=2)

    legend = ax.legend(loc='best', shadow=True, fontsize=6)
    for legobj in legend.legendHandles:
        legobj.set_linewidth(1.1)


fig2 = plt.figure(2, figsize=(8, 8))
ax2 = fig2.add_subplot(111)
for i in range(5):
    ax2.plot(xx[i], yy1[i], color=colors[i], label=names[i] + " wins taking 3 pt", linewidth=2)
    ax2.plot(xx[i], yy2[i], color=colors[20-i], label=names[i] + " wins taking 2 pt", linewidth=2)


ax2.legend(loc='best')
plt.show()
