import itertools

"""生成排列组合"""

a = list(range(0,10))
for i in itertools.combinations(a,2):
	print(i)