from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import datetime as dt
from weather import *
import pickle


root = Tk()
root.title('달력 프로그램')

root_width = 335
root_height = 350
root_pos_x = 650
root_pos_y = 250

root.geometry('{}x{}+{}+{}'.format(root_width, root_height, root_pos_x, root_pos_y)) # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False) # x좌표 y좌표 값 변경 불가

bg_color = 'lightgreen'

root.configure(bg=bg_color)

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
                btn = Button(root, text=str(i), width=5, height=2, bg=bg_color, command=lambda : event_window(year, month, i))
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

def get_all_events():
    # events 파일에 내용이 있는지 확인 있으면 있는 딕셔너리 리턴 없으면 빈 딕셔너리 리턴
    try:
        with open('events', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def add_event(year, month, date):
    # get_all_events 함수로 파일을 events 객체에 불러온다
    
    if msgbox.askokcancel('알림', '저장하시겠습니까?'):
        event = event_txt.get('1.0', END)
        events[(year, month, date)] = event

        with open('events', 'wb') as f:
            pickle.dump(events, f)
        event_view_window.destroy()
    
   

def event_window(year, month, date):
    events = get_all_events()
    global event_view_window, event_txt
    event_view_window = Toplevel(root) 
    event_view_window.geometry('300x250+1000+250')
    event_txt = Text(event_view_window, font=('Arial',12))
    event_txt.pack(fill='both', expand=True)
    print(date)
    if (year, month, date) in events:
        event_txt.insert(END, events[(year, month, date)])
        
    event_view_window.protocol("WM_DELETE_WINDOW", lambda : add_event(year, month, date))   

events = get_all_events()

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


frame_today_weather = Frame(root, width=root_width, height=40, relief='solid', bd=1, bg=bg_color)
frame_today_weather.grid(row=0, column=0, columnspan=7)

label_today_weather = Label(frame_today_weather, text=str(today.month) + '월 ' + str(today.day) + '일 '+ weekday +' 부산광역시 현재기온: ' + temp + ' ' + rain, font=('Arial',10), bg=bg_color)
label_today_weather.place(x = 0, y = 8)

# change_date = Frame(root, width=root_width, height=40, relief='solid', bd=1, bg='beige' )
# change_date.grid(row=1, column=0, columnspan=7)

change_date = Label(root, text=str(today.year)+'년 '+str(today.month)+'월', bg=bg_color, font=('Arial', 10))
change_date.grid(row=1, column=0, columnspan=2)

valuse = [str(i) for i in range(1, 13)]
month_combobox = ttk.Combobox(root, width=2, height=5, values=valuse, state='readonly')
month_combobox.grid(row=1, column=5, sticky=N+E+W+S)
month_combobox.set(str(today.month))

year_entry = Entry(root, width=5)
year_entry.grid(row=1, column=4, sticky=N+E+W+S)

enter_btn = Button(root, width=5, text='입력', bg=bg_color, command=enter_btn_cmd)
enter_btn.grid(row=1, column=6, sticky=N+E+W+S)



mo_label = Label(root, width=5, height=2, text='월', bg=bg_color, font=('Arial',10))
tu_label = Label(root, width=5, height=2, text='화', bg=bg_color, font=('Arial',10))
we_label = Label(root, width=5, height=2, text='수', bg=bg_color, font=('Arial',10))
th_label = Label(root, width=5, height=2, text='목', bg=bg_color, font=('Arial',10))
fr_label = Label(root, width=5, height=2, text='금', bg=bg_color, font=('Arial',10))
sa_label = Label(root, width=5, height=2, text='토', bg=bg_color, font=('Arial',10))
su_label = Label(root, width=5, height=2, text='일', bg=bg_color, font=('Arial',10))
mo_label.grid(row=2, column=0, sticky=N+E+W+S)
tu_label.grid(row=2, column=1, sticky=N+E+W+S)
we_label.grid(row=2, column=2, sticky=N+E+W+S)
th_label.grid(row=2, column=3, sticky=N+E+W+S)
fr_label.grid(row=2, column=4, sticky=N+E+W+S)
sa_label.grid(row=2, column=5, sticky=N+E+W+S)
su_label.grid(row=2, column=6, sticky=N+E+W+S)


display_custom_calendar(today.month, today.year)
    

root.mainloop()