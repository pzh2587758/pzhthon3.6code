from tkinter import *
from tkinter import ttk

root = Tk()


def callback(event):  # 创建一个要被执行的事件
    print("鼠标左键点击位置为：", event.x, event.y)  # 显示xy坐标
frame = ttk.Frame(root, width=100, height=100, relief='ridge')
frame.bind("<Button-1>", callback)  # bind(检测事件，执行事件)1左键2中键3右键
frame.pack()

button = ttk.Button(root, text='ding')
# button.focus_set()
button.bind("<Button-3>", callback)
button.pack()

button2 = ttk.Button(root, text='dang')
button2.focus_set()
button2.pack()

# button = ttk.Button(master=root,text='文本',command='指定控件的事件处理函数',
# bitmap=''
# .focus_set(),
# bg='背景色',fg='前景色',font='字体',
# height,width,
# state,wraplength,
# anchor=N,S,W,E,
# bd=2,
# textvariable)
# button.pack()

root.mainloop()
