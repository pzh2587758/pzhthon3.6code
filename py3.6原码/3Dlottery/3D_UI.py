from tkinter import *
from tkinter import ttk
#--------------------------------------------------------------------------
root = Tk()

"""窗口美化设置"""
root.title("3D预测")  # 标题
root.geometry('400x600')  # 初始大小
# root.resizable(width=False,height=False)#大小是否能调整
root.config(background='#d8e4f2')  # 背景色
#---------------------------------------------------------------------------
root.tk.call('tk', 'windowingsystem')  # 检查程序运行与哪个平台（菜单）

root.option_add('*tearOff', FALSE)  # 使得菜单栏好看一些，不显示菜单窗口控制，防止撕裂****
#########################################################
"""菜单栏设置"""
menubar = Menu(root)  # 创建一个主菜单栏对象，属于新窗口
#_________________________________________________________________________
"""一级菜单"""
menu_file = Menu(menubar)  # 子菜单1，属于menubar
menu_edit = Menu(menubar)  # 子菜单2，属于menubar
menu_sql = Menu(menubar)  # 创建子菜单对象3
menubar.add_cascade(menu=menu_file, label='文件')  # 主菜单控件连接子菜单1，属性
menubar.add_cascade(menu=menu_edit, label='工具')  # 2连接到主菜单
menubar.add_cascade(menu=menu_sql, label='服务器')  # 3连接到主菜单
#_________________________________________________________________________
'''file下的选项设置'''
newFile = Menu(menu_file)  # 创建子菜单menu_file下的选项
openFile = Menu(menu_file)
closeFile = Menu(menu_file)

menu_file.add_command(label='新建', command=newFile)  # 为menu_file菜单项设置属性
menu_file.add_command(label='打开...', command=openFile)
menu_file.add_command(label='关闭', command=closeFile)
#_________________________________________________________________________
"""sql的下级菜单"""
lianje = Menu(menu_sql)
duankai = Menu(menu_sql)
zen = Menu(menu_sql)
shan = Menu(menu_sql)
cha = Menu(menu_sql)
gai = Menu(menu_sql)

menu_sql.add_command(label='连接服务器', command=lianje)
menu_sql.add_command(label='断开服务器', command=duankai)
menu_sql.add_separator()
menu_sql.add_command(label='增加数据', command=zen)
menu_sql.add_command(label='删除数据', command=shan)
menu_sql.add_command(label='查找数据', command=cha)
menu_sql.add_command(label='改动数据', command=gai)
#_________________________________________________________________________
root.config(menu=menubar)  # 关键，root用来连接菜单栏的哈哈哈哈哈*******
"""菜单栏结束"""
#-----------------------------------------------------------------------------
"""小控件"""

sqlimpg = ttk.Label(root, text='服务器图')
sqlimpg.grid(row=0, column=0)

lianjiebutton = ttk.Button(root, text='连接')
lianjiebutton.grid(row=0, column=1)

lianjiempg = ttk.Label(root, text='连接断开图')
lianjiempg.grid(row=0, column=2)

duankaibutton = ttk.Button(root, text='断开')
duankaibutton.grid(row=0, column=3)

zenbutton = ttk.Button(root, text='增加数据')
shanbutton = ttk.Button(root, text='删除数据')
chabutton = ttk.Button(root, text='查找数据')
gaibutton = ttk.Button(root, text='改动数据')
zenbutton.grid(row=7, column=0)
shanbutton.grid(row=7, column=1)
chabutton.grid(row=7, column=2)
gaibutton.grid(row=7, column=3)
#———————————————————————————————————
"""树"""
# 创建一个树，设置为标题，并设置宽和列a,列b
sqltree = ttk.Treeview(root, show='headings', height=6, columns=('a', 'b'))
sqltree.grid(row=1, column=0, rowspan=6, columnspan=4, sticky=(N, S, E, W))


sqltree.column("a", width=100, anchor="center")  # 设置列a的宽，中心
sqltree.column("b", width=50, anchor="center")
sqltree.heading("a", text='期号')  # 设置列a的文本
sqltree.heading("b", text='开奖号')

for i in range(30):  # 循环插入数据
    sqltree.insert('', i, values=('a' + str(i), 'b' + str(i)))

# 创建一个滚动条（方向为竖（vertical，horizontal），执行一个内置方法yview)
sqlscrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=sqltree.yview)
# tree设置关联方法，关联了滚动条
sqltree.configure(yscrollcommand=sqlscrollbar.set)
# 滚动条网格位置
sqlscrollbar.grid(row=1, column=5, rowspan=6, sticky=NS)
#——————————————————————————————————
"""界面伸缩比"""
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
root.columnconfigure(7, weight=1)
root.columnconfigure(8, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)


#-------------------------------------------------------------------------
root.mainloop()
