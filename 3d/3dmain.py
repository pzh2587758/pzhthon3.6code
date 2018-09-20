#/usr/bin/python3.6

class main_3d():
    """这是3Dpredict程序的入口，显示选项。"""


    #主要选项
    def xuanxiang(self):
        print('主要选项:')
        print('1.测试一组随机数的正确率')



if __name__ == '__main__':
    a = main_3d()
    a.xuanxiang()
    b = input('请输入一个选项数字：')
    print('你选择的是 %s,现在开始测试：' % b)