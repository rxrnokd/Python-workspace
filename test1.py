from tkinter import *
import datetime as dt

today = dt.datetime.today()
first_weekday = dt.date(today.year, today.month, 1).weekday()
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

root = Tk()
root.title('Calendar')

root_width = 640
root_height = 480
root_pos_x = 650
root_pos_y = 250

root.geometry('{}x{}+{}+{}'.format(root_width, root_height, root_pos_x, root_pos_y)) # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # x좌표 y좌표 값 변경 불가

root.configure(bg='pink')

# frame_today_weather = Frame(root, width=root_width, height=40, relief='solid', bd=1)
# frame_today_weather.pack()

# label_today_weather = Label(frame_today_weather, text=str(today.year) + '년 ' + str(today.month) + '월 ' + str(today.day) + '일 ', font=('Arial',10))
# label_today_weather.place(x = 0, y = 8)

day_counter = 1 - first_weekday
i = 1
for a in range(6):
    for b in range(7):
        if 1 <= day_counter <= month_days[today.month]:
            btn = Button(root, text=str(i), width=5, height=2)
            btn.grid(row=a, column=b)
            i += 1
        # else:
        #     label = Label(root, text='', width=5, height=3)
        #     label.grid(row=a, column=b)
        day_counter += 1        




root.mainloop()