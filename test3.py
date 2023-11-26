from weather import *
import datetime as dt
today = dt.datetime.today()
print(today)
c = '12'
print(c.rjust(2, '0'))
print(str(today.year)+str(today.month)+str(today.day), str(today.hour).rjust(2, '0')+'00')
a, b = short_term_situation(str(today.year)+str(today.month)+str(today.day), str(today.hour).rjust(2, '0')+'00')
print(a)