from tkinter import  *
from tkinter import ttk

class app(ttk.Frame):
     def __init__(self,master=None):
          super().__init__(master)
          self.pack()
          self.create_widgets()

     def create_widgets(self):
          self.hi_there = Button(self,text='hello\n(clike me)',
                                    command=self.say_hi)
          self.hi_there.pack(side='top')

          self.quit=Button(self,bg='blue',text='quit',
                               command=root.destroy)
          self.quit.pack(side='bottom')

     def say_hi(self):
          print('hi ther,everyone!')

root = Tk()
app = app(master=root)
app.mainloop()
