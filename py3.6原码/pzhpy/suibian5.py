# -*- coding: utf-8 -*-
# python 3.62

class Fib(object):
	"""斐波那契数列的实现"""
	def __init__(self):
		self.a,self.b =0 ,1 #初始化两个计数器a,b

	def __iter__(self):
		return self #实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b, self.a + self.b #计算下一个值
		if self.a>1000000000:
			raise StopIteration

		return self.a #返回下一个值

for n in Fib():
	print(n)