import datetime

def display_custom_calendar(month, year):
    # 각 월의 일수를 저장한 리스트 (윤년이 아닌 경우)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 월의 첫 요일을 가지고 온다
    first_weekday = datetime.date(year, month, 1).weekday()

    # 윤년 확인     
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        month_days[2] = 29

    # 달력 상단에 현재 월/연도 표시
    month_names = ["", "1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
    print(f"{month_names[month]} {year}년") 

    # 요일 이름 출력
    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    print(" ".join(weekdays))    
    print("-" * 20)

    # 일자 출력
    day_counter = 1 - first_weekday
    for _ in range(6): # 한 달은 최대 6주까지 있을 수 있음
        for _ in range(7):
            if 1 <= day_counter <= month_days[month]:
                if (year, month, day_counter) in events:
                    print(str(day_counter).rjust(2), end='*' )
                else:    
                    print(str(day_counter).rjust(2), end=' ')
            else:
                print('  ', end=' ')
            day_counter += 1
        print()

# 스케줄 저장 딕셔너리
events = {(2023, 10, 1): '수학시험', (2023, 10, 2): '국어시험', (2023, 10, 19): '영어시험'}

def add_event(year, month, date, event):
    global events
    # 일정을 딕셔너리에 저장
    if (year, month, date) in events:
        events[(year, month, date)] += ' ' + event
    else:    
        events[(year, month, date)] = event
    print('일정을 저장 했습니다')

def view_events(year, month, date):
    global events
    # 일정이 있으면 보여주고 없으면 안보여줌
    if (year, month, date) in events:
        print('{}년 {}월 {}일 일정: {}'.format(year, month, date, events[(year, month, date)]))
    else:
        print('{}년 {}월 {}일 일정이 없습니다'.format(year, month, date))

def del_event(year, month, date):
    global events
    # 일정을 삭제
    del events[year, month, date]
    print('일정을 삭제 했습니다')

year = int(input('연도를 입력하세요: '))
month = int(input('월을 입력하세요: '))

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
        display_custom_calendar(month, year)
        
        print('프로그램을 종료합니다')
        break

    else:
        print('잘못된 입력입니다')