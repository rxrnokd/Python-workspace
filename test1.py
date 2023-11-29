from tkinter import *
import tkinter.ttk as ttk
import datetime as dt
from weather import *


root = Tk()
root.title('Calendar')

root_width = 335
root_height = 405
root_pos_x = 650
root_pos_y = 250

root.geometry('{}x{}+{}+{}'.format(root_width, root_height, root_pos_x, root_pos_y)) # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # x좌표 y좌표 값 변경 불가

root.configure(bg='beige')

def display_custom_calendar(month, year):
    global btn
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    first_weekday = dt.date(year, month, 1).weekday()

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[2] = 29

    day_counter = 1 - first_weekday
    i = 1
    for a in range(3,9):
        for b in range(7):
            if 1 <= day_counter <= month_days[month]:
                btn = Button(root, text=str(i), width=5, height=2, bg='beige')
                btn.grid(row=a, column=b, sticky=N+E+W+S)
                btns.append(btn)
                i += 1
            day_counter += 1

btns = []

def enter_btn_cmd():
    year = year_entry.get()
    month = month_combobox.get()
    year_entry.delete(0, END)
    print(btns)
    for btn in btns:
        btn.destroy()
    btns.clear()
    change_date.config(text=year+'년 '+month+'월')
    display_custom_calendar(int(month), int(year))

today = dt.datetime.today()

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


frame_today_weather = Frame(root, width=root_width, height=40, relief='solid', bd=1, bg='beige')
frame_today_weather.grid(row=0, column=0, columnspan=7)

label_today_weather = Label(frame_today_weather, text=str(today.month) + '월 ' + str(today.day) + '일 '+ weekday +' 부산광역시 현재기온: ' + temp + ' ' + rain, font=('Arial',10), bg='beige')
label_today_weather.place(x = 0, y = 8)

# change_date = Frame(root, width=root_width, height=40, relief='solid', bd=1, bg='beige' )
# change_date.grid(row=1, column=0, columnspan=7)

change_date = Label(root, text=str(today.year)+'년 '+str(today.month)+'월', bg='beige', font=('Arial', 10))
change_date.grid(row=1, column=0, columnspan=2)

valuse = [str(i) for i in range(1, 13)]
month_combobox = ttk.Combobox(root, width=2, height=5, values=valuse, state='readonly')
month_combobox.grid(row=1, column=5, sticky=N+E+W+S)
month_combobox.set(str(today.month))

year_entry = Entry(root, width=5)
year_entry.grid(row=1, column=4, sticky=N+E+W+S)

enter_btn = Button(root, width=5, text='입력', bg='beige', command=enter_btn_cmd)
enter_btn.grid(row=1, column=6, sticky=N+E+W+S)



mo_label = Label(root, width=5, height=2, text='월', bg='beige', font=('Arial',10))
tu_label = Label(root, width=5, height=2, text='화', bg='beige', font=('Arial',10))
we_label = Label(root, width=5, height=2, text='수', bg='beige', font=('Arial',10))
th_label = Label(root, width=5, height=2, text='목', bg='beige', font=('Arial',10))
fr_label = Label(root, width=5, height=2, text='금', bg='beige', font=('Arial',10))
sa_label = Label(root, width=5, height=2, text='토', bg='beige', font=('Arial',10))
su_label = Label(root, width=5, height=2, text='일', bg='beige', font=('Arial',10))
mo_label.grid(row=2, column=0, sticky=N+E+W+S)
tu_label.grid(row=2, column=1, sticky=N+E+W+S)
we_label.grid(row=2, column=2, sticky=N+E+W+S)
th_label.grid(row=2, column=3, sticky=N+E+W+S)
fr_label.grid(row=2, column=4, sticky=N+E+W+S)
sa_label.grid(row=2, column=5, sticky=N+E+W+S)
su_label.grid(row=2, column=6, sticky=N+E+W+S)


display_custom_calendar(today.month, today.year)
    

root.mainloop()