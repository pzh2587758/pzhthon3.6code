from tkinter import *
from tkinter import ttk
#import tkinter as tk
#--------------------------------------------------------------------------


#--------------------------------------------------------------------------
root = Tk()
root.title("3D预测")  # 标题
# root.geometry('212x264+80+80')#初始大小
# root.resizable(width=True,height=True)#大小是否能调整
root.config(background='#d8e4f2')  # 背景色
#---------------------------------------------------------------------------
root.tk.call('tk', 'windowingsystem')  # 检查程序运行与哪个平台（菜单）

root.option_add('*tearOff', False)  # 使得菜单栏好看一些，不显示菜单窗口控制，防止撕裂****

#_____________________________________________


#_____________________________________________

"""要为一个窗口创建一个menubar，
我们首先创建一个菜单控件（顶层控件win），
然后使用win的“菜单”配置选项将菜单小部件连接到窗口."""
# win = Toplevel(root)#创建一个新窗口

menubar = Menu(root)  # 创建一个主菜单栏对象，属于新窗口
# win['menu'] = menubar#新窗口win的菜单配置选项，将主菜单控件连接。


menu_file = Menu(menubar)  # 子菜单1，属于menubar
menu_edit = Menu(menubar)  # 子菜单2，属于menubar
menu_sql = Menu(menubar)  # 创建子菜单对象3
menubar.add_cascade(menu=menu_file, label='文件')  # 主菜单控件连接子菜单1，属性
menubar.add_cascade(menu=menu_edit, label='控制')  # 2连接到主菜单
menubar.add_cascade(menu=menu_sql, label='sql')  # 3连接到主菜单
###################################################
'''menu_file下的选项设置'''
newFile = Menu(menu_file)  # 创建子菜单menu_file下的选项
openFile = Menu(menu_file)
closeFile = Menu(menu_file)


menu_file.add_command(label='新建', command=newFile)  # 为menu_file菜单项设置属性
menu_file.add_command(label='打开...', command=openFile)
menu_file.add_command(label='关闭', command=closeFile)


menu_file.add_separator()  # 这是一个横杠

check = StringVar()  # 勾选框
menu_file.add_checkbutton(label='Check', variable=check,
                          onvalue=1, offvalue=0)  # 向添加

radio = StringVar()  # 单选框
menu_file.add_radiobutton(label='One', variable=radio, value=1)
menu_file.add_radiobutton(label='Two', variable=radio, value=2)
####################################################
zen = Menu(menu_sql)
shan = Menu(menu_sql)
cha = Menu(menu_sql)
gai = Menu(menu_sql)

menu_sql.add_command(label='增', command=zen)
menu_sql.add_command(label='删', command=shan)
menu_sql.add_command(label='查', command=cha)
menu_sql.add_command(label='改', command=gai)

root.config(menu=menubar)  # 关键，root用来连接菜单栏的哈哈哈哈哈*******
#-----------------------------------------------------------------------------

content = ttk.Frame(root, padding=(3, 3, 12, 12))  # 矩形容器（父，填补）

# 矩形容器（父，边框宽度，雕刻类型，宽，高）
# relief ="flat" (default), "raised", "sunken", "solid", "ridge", or "groove"
frame = ttk.Frame(content, borderwidth=5,
                  relief="ridge", width=200, height=100)

namelbl = ttk.Label(content, text="名字")  # 标签（父，文本）
name = ttk.Entry(content)  # 条目？（父）

onevar = BooleanVar()  # 设置布尔变量，为复选框准备布尔值
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)  # 布尔变量的固定值
twovar.set(False)
threevar.set(True)

# 复选按钮（父，文本，复选框变量，复选框吸合值（作用值）
one = ttk.Checkbutton(content, text="石头", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="剪刀", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="布", variable=threevar, onvalue=True)


ok = ttk.Button(content, text="确定")
cancel = ttk.Button(content, text="取消")

# 网格位置设置(列，行，粘黏性(组件紧靠所在单元格的某一边角)）
"""sticky 意思是组件紧靠所在单元格的某一边角。
     取值有：“n”, “s”, “w”, “e”, “nw”, “sw”, “se”, “ne”, “center” """
content.grid(column=0, row=0, sticky=(N, S, E, W))
#(列，行，跨列，跨行，粘性）
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
#(列，行，跨行，粘性,x方向外部间隔）
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
#（行，列，跨行，粘性，组件外部在y方向填充空间大小，组件外部在x方向填充空间大小)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)  # 列配置，添加填充整个列
root.rowconfigure(0, weight=1)  # 行配置,如果主窗口改变大小，框架应该扩展到其余空间。
content.columnconfigure(0, weight=3)  # 当主窗口大小改变，第0列跟着改变，权重为3
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
#-------------------------------------------------------------------------
root.mainloop()
