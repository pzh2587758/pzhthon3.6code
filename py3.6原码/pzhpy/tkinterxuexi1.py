from tkinter import *
from tkinter import ttk

root = Tk()
root.title("pzh之地")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column = 0,row =0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()




ttk.Button(mainframe,text="增").grid(column=3,row=1,sticky=W)
ttk.Button(mainframe,text="删").grid(column=3,row=2,sticky=N)
ttk.Button(mainframe,text="查").grid(column=3,row=3,sticky=S)
ttk.Button(mainframe,text="改").grid(column=2,row=1,sticky=E)

root.mainloop()
