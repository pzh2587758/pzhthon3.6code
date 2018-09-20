"""使用for循环，操作数列中的每一个元素+1"""
numbers = [2,8,13,17,25,29,36,45,61,87,94]
a = input("请输入增加的数字:")
b =int(a)
for number in numbers:
     print(str(number) + "+"+str(b)+"=" +str(number+b))



