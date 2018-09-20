from name_function import get_formatted_name

print("按'q' 退出")
while True:
    first = input("\n请输入第一个名字：")
    if first == 'q':
        break

    last = input('请给我后面的名字：')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\t 全名为：" + formatted_name + '.')
