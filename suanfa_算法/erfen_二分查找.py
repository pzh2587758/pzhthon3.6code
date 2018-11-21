#!~/.git_repository/python3.6code/sranfa_算法 python3

def binary_search(list,item):
    """
       这是一个简单的二分查找算法。
       函数接受一个有序数组和一个想查找的元素。
       如果指定的元素包含在数组中，函数将返回这个元素的位置。
       反之报错。
       你将跟踪这个数组，每次都检查中间的那个元素。
       如果猜测的数字小了，就修改low
       如果猜测的数字大了，就修改high
    """
    low = 0 #最小的下标
    high = len(list)-1 #最后一个下标
    jiuu = 0

    while low <= high:
        mid = int((low + high)/2) #中间的下标
        guess = list[mid] #提取中间下标的值
        if guess == item:
            jiuu += 1
            print("找到")
            print("用了" + str(jiuu) + "次")
            return mid
        if guess > item:
            print("大了")
            high = mid - 1 #将最后一个下标设置为中间的下标之前的一个
            jiuu += 1
        else:
            print("小了")
            low = mid + 1 #将最小下标设置为中间下标之后的一个下标
            jiuu += 1
    return None
    
my_list = range(0,999)
a = binary_search(my_list,5)
print(a)

print(binary_search.__doc__)
