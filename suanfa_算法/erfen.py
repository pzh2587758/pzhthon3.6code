def erfen(list,item):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        
        if guess == item:
            return list[mid]
        if guess > item:
            print("大了")
            high = mid -1
        else:
            print("小了")
            low = mid + 1

    return None

my_list = range(0,100000000)
a = erfen(my_list,9)
print(a)
