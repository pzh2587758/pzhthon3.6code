#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : SundayCoder-俊勇
# @File    : eventthing.py
from tkinter import *
from tkinter import ttk

root = Tk()


def key(event):
    print("pressed at widget%s" % event.widget)
    print("pressed", repr(event.char))
    print("event.type is %s" % event.type)
    # 按下键盘上的f键的时候执行的事件
    # （注意大写的F与小写的f他们的事件监听是不一样的，这里监听是小写的f）
    print(event.keycode)
    # 按下键盘上的f键的时候执行的事件
    if event.keysym == 'f':
        print("hello world %s" % repr(event.char))
    # 这里可以使用keycode对大小写的F进行监听
    if event.keycode == 70:
        print("这里可以使用keycode对大小写的F进行监听")


def callback(event):
    frame.focus_set()
    print("num is %s" % event.num)
    print("width is %s, height is %s" % (event.width, event.height))
    print("clicked at widget%s" % event.widget, event.x, event.y,
          "root_x,root_y", event.x_root, event.y_root, event.type)


def sayhello(event):
    print("hello world")
frame = ttk.Frame(root, width=300, height=250, relief='ridge')
frame.bind("<Key>", key)
# button-1是鼠标左键按下，以此类推
# B1-Motion是鼠标左键移动，以此类推
frame.bind("<Button-1>", callback)
frame.bind("<Button-2>", callback)
frame.bind("<Button-3>", callback)
frame.bind("<B1-Motion>", callback)
frame.bind("<B2-Motion>", callback)
frame.bind("<B3-Motion>", callback)
# 注意这里的<Enter>事件不是键盘按下Enter而是鼠标进入到控件时候的事件，相当于java的获得焦点的事件监听
frame.bind("<Enter>", sayhello)
frame.pack()

root.mainloop()
