import csv
import matplotlib.pyplot as plt
import numpy as np


def num(s):
	try:
		return int(s)
	except ValueError:
		return 0


def getcolors():
	colors = [(31, 119, 180), (255, 0, 0), (0, 255, 0), (148, 103, 189), (140, 86, 75), (218, 73, 174), (127, 127, 127), (140, 140, 26), (23, 190, 207), (65, 200, 100), (200, 65, 100), (125, 255, 32), (32, 32, 198), (255, 191, 201), (172, 191, 201), (0, 128, 0), (244, 130, 150), (255,127, 14), (128, 128, 0), (10, 10, 10), (44, 160, 44), (214, 39, 40), (206, 206, 216)]
	
	for i in range(len(colors)):
		r, g, b = colors[i]
		colors[i] =(r/255., g/255., b/255.)
		
	return colors


def getQbNames():
	qbnames = ['Peyton Manning']
	name = ''
	i = 0
	with open('qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['Name'] != name and qbnames[i] != row['Name']:
				qbnames.append(row['Name'])
				i = i+1
	return qbnames


def readQbdata():
	resultdata = []
	with open('qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		resultdata = [row for row in reader]
	return resultdata


'''
哪位四分卫球员职业生涯最长？
44岁的Warren Moon
'''

maxage = 30
qbname = ''

with open('qb_data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if num(row['Age']) > maxage:
			qbname = row['Name']
			maxage = num(row['Age'])

print(qbname, maxage)

'''
现在还有人能超越Peython Manning触地得分记录的四分卫球员吗？
'''
fdata = []
prevysum = 0

qbnames = getQbNames()
fdata = readQbdata()
# print(qbnames)
# print(fdata)

i = 0
rank =0 
prevysum = 0
lastyr = 0
highrank = 16
colorsdata = getcolors()


fig = plt.figure()
ax = fig.add_subplot(111)

# limits for TD
plt.xlim(20, 50)
plt.ylim(10, 744)

colindex = 0
lastage = 20

res = {}

for qbn in qbnames:
	x = []
	y = []
	prevysum = 0
	for row in fdata:
		if row['Name'] == qbn and row['Year'] != 'Career':
			yrval = num(row['Year'])
			lastage = num(row['Age'])
			prevysum += num(row['TD'])
			lastyr = yrval
			x += [lastage]
			y += [prevysum]
	
	res[qbn] = list(zip(x, y))
	
# print(res)
sorted_res = dict(sorted(res.items(), key=lambda x: x[1][-1][1]))
# print(sorted_res)

	

for qbn, data in sorted_res.items():
	x = [_[0] for _ in data]
	y = [_[1] for _ in data]
	lastage = x[-1]
	prevysum = y[-1]
	#print(x, y)
	
	if  rank > highrank:
		if lastage == 43:
			plt.plot(x, y, color='red', label=qbn, linewidth=3.5)
		else:		
			plt.plot(x, y, color=colorsdata[colindex], label=qbn, linewidth=2.5)
		plt.legend(loc=0, prop={'size': 10})
		colindex = (colindex + 1)%22
		plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):"+str(lastage), fontsize=6)
	else:
		if lastage == 43:
			plt.plot(x, y, color='red', label=qbn, linewidth=3.5)
			plt.legend(loc=0, prop={'size': 10})
			plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):"+str(lastage), fontsize=6)
		else:
			plt.plot(x, y, color=colorsdata[22], linewidth=1.5)
		rank += 1
	
plt.text(25, 650, 'The most likely player to overtake Peyton Manning: Drew Brees', fontsize=9, color='red')	

plt.xlabel('Age', fontsize=18)
plt.ylabel('Number of Touch Downs', fontsize=18)
plt.title('Touch Downs by Quater Backs by Age', fontsize=20)

'''
画一个堆叠的柱状图，仅包含四位选手：（（相对）最接近的）
Peyton Manning, Brett Favre, Drew Brees, Tom Brady
'''
res = {}
qbnames = ['Peyton Manning', 'Brett Favre', 'Drew Brees', 'Tom Brady']

for qbn in qbnames:
	x = []
	y = []
	prevysum = 0
	for row in fdata:
		if row['Name'] == qbn and row['Year'] != 'Career':
			yrval = num(row['Year'])
			lastage = num(row['Age'])
			prevysum += num(row['TD'])
			lastyr = yrval
			x += [lastage]
			y += [prevysum]
	
	res[qbn] = list(zip(x, y))
	
plt.figure()
plt.xlim(26, 35)
plt.ylim(10, 744)

ind = np.arange(27, 35)
width = 0.2
i = 0
index = [-0.4, -0.2, 0, 0.2]
c_index = [4, 3, 1, 0]

def autolabel(rects):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()+rect.get_width()/2, height, str(height), ha='center', va='bottom')


for qbn in qbnames:
	y = [_[1] for _ in res[qbn] if 27<=num(_[0])<=34]
	abar = plt.bar(ind+index[i], y, width, color=colorsdata[c_index[i]], label=qbn)
	i += 1	
	autolabel(abar)

plt.legend(loc='best')






plt.show()


