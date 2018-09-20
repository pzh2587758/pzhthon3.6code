# python 3.62
# UTF8

from susuan import susuan


def tous():
    print("****************************************")
    print("*1.正则表达式练习  *10.python内置方法  *")
    print("*2.vim键位练习     *11.python内置关键字*")
    print("*3.python内置模块  *                   *")
    print("*4.python内置函数  *                   *")
    print("*5.加法速算        *                   *")
    print("*6.减法速算        *                   *")
    print("*7.乘法速算        *16.小范围测试      *")
    print("*8.除法速算        *                   *")
    print("*9.混合速算        *                   *")
    print("****************************************")
    print("输入'Quit'退出程序。")
    print(">>>>>>>>>>>")


def xunhuan(timu):
    """题库循环"""
    timu.recodes_key_list()
    while True:
        if timu.breaks == False:
            timu.goceshi()
            timu.right_error()
        elif timu.breaks == True:
            break


def susuanxh(num):
    """速算循环"""
    susuanti = susuan()
    while True:
        if susuanti.breaksusuan == True:
            if num == "5":
                susuanti.digit_add()
                susuanti.right_error()
            elif num == "6":
                susuanti.digit_SUB()
                if susuanti.num1 > susuanti.num2:
                    susuanti.right_error()
                else:
                    pass
            elif num == "7":
                susuanti.digit_MUL()
                susuanti.right_error()
            elif num == "8":
                susuanti.digit_DIV()
                if susuanti.num1 > susuanti.num2:
                    susuanti.right_error()
                else:
                    pass
        elif susuanti.breaksusuan == False:
            break
