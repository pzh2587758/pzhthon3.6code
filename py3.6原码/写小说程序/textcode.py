from tkinter import *
from tkinter import ttk

root = Tk()
root.title('小说写作程序')
root.geometry('1400x900+80+80')
root.resizable(width=False,height=False)
root.config(background='#262626')
root.tk.call('tk','windowingsystem')#检查运行与哪个平台
root.option_add('*tearOff',False)#防止菜单撕裂
#################################################
menubar = Menu(root)

menu_file=Menu(menubar)
menu_edit=Menu(menubar)
menubar.add_cascade(menu=menu_file,label='文件')
menubar.add_cascade(menu=menu_edit,label='控制')
#__________________________________________________________


#__________________________________________________________
"""菜单栏结束"""
root.config(menu=menubar)
#__________________________________________________________
marst_text = Text(root,bg='#5d9014',width=800,height=600)
marst_text.focus_set()
marst_text.pack()


#################################################
root.mainloop()
