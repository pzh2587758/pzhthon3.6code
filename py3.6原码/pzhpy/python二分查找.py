def date_fine(date, date_num):
    mid = int(len(date)/2)
    if (date[mid] >= 1 and 0 <= date_num <= 99):
        if date[mid] > date_num:
            print("输入的数字比中间值[%s]小" % date[mid])
            date_fine(date[:mid], date_num)
        elif date[mid] < date_num:
            print("输入的数字比中间值[%s]大" % date[mid])
            date_fine(date[mid:], date_num)
        else:
            print("这就是你要找的数字是[%s]" % date[mid])
    else:
        print("没找到！")


if __name__ == "__main__":
    date = list(range(100))
    #print(date)
    date_num = int(input("请输入一个（0<=x<=99）数字："))
    date_fine(date, date_num)
