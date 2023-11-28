from tkinter import *
import datetime as dt
from weather import *

today = dt.datetime.today()
first_weekday = dt.date(today.year, today.month, 1).weekday()
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
temp, rain = short_term_situation(str(today.year)+str(today.month)+str(today.day), str(today.hour).rjust(2, '0')+'00')

if today.weekday() == 0:
    weekday = '월요일'
elif today.weekday() == 1:   
    weekday = '화요일'
elif today.weekday() == 2:   
    weekday = '수요일'
elif today.weekday() == 3:   
    weekday = '목요일'
elif today.weekday() == 4:   
    weekday = '금요일'
elif today.weekday() == 5:   
    weekday = '토요일'
elif today.weekday() == 6:   
    weekday = '일요일'

root = Tk()
root.title('Calendar')

root_width = 335
root_height = 405
root_pos_x = 650
root_pos_y = 250

root.geometry('{}x{}+{}+{}'.format(root_width, root_height, root_pos_x, root_pos_y)) # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # x좌표 y좌표 값 변경 불가

root.configure(bg='beige')

frame_today_weather = Frame(root, width=root_width, height=40, relief='solid', bd=1, bg='beige')
frame_today_weather.grid(row=0, column=0, columnspan=7)

label_today_weather = Label(frame_today_weather, text=str(today.year) + '년 ' + str(today.month) + '월 ' + str(today.day) + '일 '+ weekday +' 부산광역시 현재기온: ' + temp + ' ' + rain, font=('Arial',10), bg='beige')
label_today_weather.place(x = 0, y = 8)

mo_label = Label(root, width=5, height=2, text='월', bg='beige', font=('Arial',10))
tu_label = Label(root, width=5, height=2, text='화', bg='beige', font=('Arial',10))
we_label = Label(root, width=5, height=2, text='수', bg='beige', font=('Arial',10))
th_label = Label(root, width=5, height=2, text='목', bg='beige', font=('Arial',10))
fr_label = Label(root, width=5, height=2, text='금', bg='beige', font=('Arial',10))
sa_label = Label(root, width=5, height=2, text='토', bg='beige', font=('Arial',10))
su_label = Label(root, width=5, height=2, text='일', bg='beige', font=('Arial',10))
mo_label.grid(row=1, column=0, sticky=N+E+W+S)
tu_label.grid(row=1, column=1, sticky=N+E+W+S)
we_label.grid(row=1, column=2, sticky=N+E+W+S)
th_label.grid(row=1, column=3, sticky=N+E+W+S)
fr_label.grid(row=1, column=4, sticky=N+E+W+S)
sa_label.grid(row=1, column=5, sticky=N+E+W+S)
su_label.grid(row=1, column=6, sticky=N+E+W+S)



day_counter = 1 - first_weekday
i = 1
for a in range(2,8):
    for b in range(7):
        if 1 <= day_counter <= month_days[today.month]:
            btn = Button(root, text=str(i), width=5, height=2, bg='beige')
            btn.grid(row=a, column=b, sticky=N+E+W+S)
            i += 1
        # else:
        #     label = Label(root, text='', width=5, height=3)
        #     label.grid(row=a, column=b)
        day_counter += 1        




root.mainloop()