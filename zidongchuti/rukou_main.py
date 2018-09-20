# python 3.62
# utf8

from tou import tous
from tou import xunhuan
from tou import susuanxh
from tiku import tikus
from luoji import zidongwendaji
from susuan import susuan
import sys


def chuti():
    tous()
    tiku = tikus()
    num = input("请输入序列号:")
    if num == "1":
        print("===>正则表达式练习<===")
        timu = zidongwendaji(tiku.zenzecodes)
        xunhuan(timu)
    elif num == "2":
        print("===>vim键位练习<===")
        timu = zidongwendaji(tiku.vimkey)
        xunhuan(timu)

    elif num == "3":
        print("===>Python内置模块练习<===")
        timu = zidongwendaji(tiku.python_neizhimodle)
        xunhuan(timu)
    elif num == "4":
        print("===>python内置函数练习<===")
        timu = zidongwendaji(tiku.python_neizhihanshu)
        xunhuan(timu)

    elif num == "5":
        print("===>加法速算练习<===")
        susuanxh(num)
    elif num == "6":
        print("===>减法速算练习<===")
        susuanxh(num)
    elif num == "7":
        print("===>乘法速算练习<===")
        susuanxh(num)
    elif num == "8":
        print("===>除法速算练习<===")
        susuanxh(num)
    elif num == "9":
        print("9")
    elif num == "10":
        print("===>Python内置方法练习<===")
        timu = zidongwendaji(tiku.python_fangfa)
        xunhuan(timu)
    elif num == "11":
        print("===>Python内置关键字<===")
        timu = zidongwendaji(tiku.keyword)
        xunhuan(timu)
    elif num == "16":
        print("===>小范围测试<===")
        timu = zidongwendaji(tiku.xiaofanwei1)
        xunhuan(timu)
    elif num == "Quit":
        sys.exit()
    else:
        print("??没有对应的序列号-_-!")


if __name__ == '__main__':
    while True:
        chuti()
