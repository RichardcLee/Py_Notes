import csv
import matplotlib.pyplot as plt


def num(s):
	try:
		return float(s)
	except ValueError:
		return 0

		
fig = plt.figure(figsize=(10, 8))
plt.ylim(35, 102)
plt.xlim(1965, 2015)

colorsdata = ['#168cf8', '#ff0000', '#009f00', '#1d437c', '#eb912b', '#8663ec', '#38762b']
labeldata = ['Below 25', '25-44', '45-54', '55-64', '65-74', '75-84', 'Over 85']

with open('mortality2.csv') as csvfile:
	mortdata = [row for row in csv.reader(csvfile)]

x = []
for row in mortdata:
	yrval = int(row[0])
	if yrval == 1969:
		y = [[num(row[1])], [num(row[2])], [num(row[3])], [num(row[4])], [num(row[5])], [num(row[6])], [num(row[7])]]
	else:
		for col in range(0, 7):
			y[col] += [num(row[col+1])]
	x += [yrval]

for col in range(0, 7):
	if col == 1:
		plt.plot(x, y[col], color=colorsdata[col], label=labeldata[col], linewidth=3.8)
	else:
		plt.plot(x, y[col], color=colorsdata[col], label=labeldata[col], linewidth=2)

plt.legend(loc=0, prop={'size': 10})
plt.show()
