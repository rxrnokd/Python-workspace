from tkinter import *

root = Tk()
root.title('Calendar')

root.geometry('640x480+650+250') # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # x좌표 y좌표 값 변경 불가

root.configure(bg='pink')

bt1 = Button(root, fg='blue', bg='pink', text='버튼1')
bt1.pack()

txt = Text(root, width=20, height=8)
txt.pack()


root.mainloop()