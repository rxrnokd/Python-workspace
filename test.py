import datetime as dt
import pickle
from weather import *

def display_custom_calendar(month, year):
    # 각 월의 일수를 저장한 리스트 (윤년이 아닌 경우)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 월의 첫 요일을 가지고 온다
    first_weekday = dt.date(year, month, 1).weekday()

    # 윤년 확인     
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[2] = 29    

    # 오늘 요일 얻기
    if today.weekday() == 0:
        weekday  = '월요일'
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

    # 현재 날짜 기온 강수상태 출력
    print(f"{today.month}월 {today.day}일 {weekday}")
    print(f'부산 현재기온: {temp} {rain}')
    print('-' * 20)

    # 달력 상단에 현재 월/연도 표시
    month_names = ["", "1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
    print(f"{year}년 {month_names[month]}") 

    # 요일 이름 출력
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    print(" ".join(weekdays))    
    print("-" * 20)

    # 일자 출력
    day_counter = 1 - first_weekday
    for _ in range(6): # 한 달은 최대 6주까지 있을 수 있음
        for _ in range(7):
            if 1 <= day_counter <= month_days[month]:
                if (year, month, day_counter) in events:
                    print(str(day_counter).rjust(2), end='*')
                else:    
                    print(str(day_counter).rjust(2), end=' ')
            else:
                print('  ', end=' ')
            day_counter += 1
        print()


def get_all_events():
    # events 파일에 내용이 있는지 확인 있으면 있는 딕셔너리 리턴 없으면 빈 딕셔너리 리턴
    try:
        with open('events', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def add_event(year, month, date, event):
    # get_all_events 함수로 파일을 events 객체에 불러온다
    events = get_all_events()

    # 일정이 있으면 추가 없으면 새로 추가
    if (year, month, date) in events:
        events[(year, month, date)] += ' ' + event
    else:    
        events[(year, month, date)] = event

    # 다시 파일에 쓰기
    with open('events', 'wb') as f:
        pickle.dump(events, f) 
    print('일정을 저장 했습니다')

def view_events(year, month, date):
    # get_all_events 함수로 파일을 events 객체에 불러온다
    events = get_all_events()

    # 일정이 있으면 보여주고 없으면 안보여줌
    if (year, month, date) in events:
        print('{}년 {}월 {}일 일정: {}'.format(year, month, date, events[(year, month, date)]))
    else:
        print('{}년 {}월 {}일 일정이 없습니다'.format(year, month, date))

def del_event(year, month, date):
    # get_all_events 함수로 파일을 events 객체에 불러온다
    events = get_all_events()

    #일정이 있으면 삭제 하고 파일에 다시 쓰기 없으면 삭제 안함
    if (year, month, date) in events:
        del events[year, month, date]
        with open('events', 'wb') as f:
            pickle.dump(events, f)
        print('일정을 삭제 했습니다')
    else:
        print('일정이 없습니다')

# 오늘 날짜 객체 생성
today = dt.datetime.today() 

# 기온 강수 상태값 받아오기
temp, rain = short_term_situation(str(today.year)+str(today.month)+str(today.day), str(today.hour)+'00')

# get_all_events 함수로 파일을 events 객체에 불러온다
events = get_all_events()

year = int(input('연도를 입력하세요: '))
month = int(input('월을 입력하세요: '))
print()
display_custom_calendar(month, year)

while True:
    print()
    print('1. 일정 추가')
    print('2. 일정 조회')
    print('3. 일정 삭제')
    print('4. 종료')
    choice = int(input('선택: '))

    if choice == 1:
        date = int(input('추가할 일정의 날짜를 입력하세요: '))
        event = input('일정을 입력하세요: ')

        add_event(year, month, date, event)
    elif choice == 2:
        date = int(input('일정을 조회할 날짜를 입력하세요: '))

        view_events(year, month, date)

    elif choice == 3:
        date = int(input('일정을 삭제할 날짜를 입력하세요: '))

        del_event(year, month, date)

    elif choice == 4:
        print()
        # get_all_events 함수로 파일을 events 객체에 불러온다
        events = get_all_events()

        display_custom_calendar(month, year)
        
        print('프로그램을 종료합니다')
        break

    else:
        print('잘못된 입력입니다')