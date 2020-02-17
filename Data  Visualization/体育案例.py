import csv
import matplotlib.pyplot as plt
'''
四分卫球员的触地得分TD，前五个最高纪录？

'''		

		
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
plt.xlim(10, 744)
plt.ylim(1940, 2021)

colindex = 0
lastage = 20

res = {}
tmp = {}

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
			y += [yrval]
			x += [prevysum]
	
	res[qbn] = list(zip(x, y))
	tmp[qbn] = lastage
	
# print(res)
sorted_res = dict(sorted(res.items(), key=lambda x: x[1][-1][0]))
# print(sorted_res)

	

for qbn, data in sorted_res.items():
	x = [_[0] for _ in data]
	y = [_[1] for _ in data]
	lastyr = y[-1]
	prevysum = x[-1]
	lastage = tmp[qbn]
	
	if  rank > highrank:
		plt.plot(x, y, color=colorsdata[colindex], label=qbn, linewidth=2.5)
		plt.legend(loc=0, prop={'size': 10})
		colindex = (colindex + 1)%22
		plt.text(prevysum+2, lastyr-1, qbn+"("+str(prevysum)+"):"+str(lastage), fontsize=6)
	else:
		plt.plot(x, y, color=colorsdata[22], linewidth=1.5)
		rank += 1
	

plt.xlabel('Year', fontsize=18)
plt.ylabel('Cumulative Touch Downs', fontsize=18)
plt.title('Cumulative Touch Downs by Quater Backs', fontsize=20)
plt.show()



