from tkinter import *

root = Tk()
root.title("Protocol Example")
root.geometry('640x340')
b = {}
txt = Text(root, width=30, height=20)
txt.pack()
def get_txt():
    a = txt.get('1.0', END)
    print(a)
    b['txt'] = a
    print(b['txt'])
def show_txt(a):
    print(a) 
i = 2       
btn = Button(root, text=str(i), command=lambda : show_txt(i))
btn.pack()

root.mainloop()
