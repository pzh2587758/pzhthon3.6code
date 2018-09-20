import random
'''随机生成一个4位数的验证码'''
checkcode = ''
for i in range(4):
	current = random.randrange(0,4)
	if current != i:
		temp = chr(random.randint(65,90))
	else:
		temp = random.randint(0,9)
	checkcode += str(temp)
print(checkcode)
