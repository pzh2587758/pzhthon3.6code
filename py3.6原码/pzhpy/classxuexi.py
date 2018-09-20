class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		#从属性设定一个值
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条公里数的消息"""
		print("这辆汽车行驶了" + str(self.odometer_reading) + "公里")

	def update_odometer(self,mileage):
		"""将里程表设置为指定的值"""
		"""禁止设定值，禁止回调值"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("这不是合法的，你不能回调里程数。")

	def increment_odometer(slef,miles):
		self.odometer_reading += miles

if __name__ == "__main__":
	my_new_car = Car('audi','a4',2018)
	print(my_new_car.get_descriptive_name())
	#直接修改对象的属性值
	my_new_car.odometer_reading = 55
	#通过一个方法修改对象属性的值
	my_new_car.update_odometer(56)
	my_new_car.read_odometer()