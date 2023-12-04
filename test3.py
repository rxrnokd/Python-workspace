from weather import *
import datetime as dt

today = dt.datetime.today()

print(str(today.year)+str(today.month).rjust(2, '0')+str(today.day).rjust(2, '0'), str(today.hour).rjust(2, '0')+'00')
tmp, rain = short_term_situation(str(today.year)+str(today.month).rjust(2, '0')+str(today.day).rjust(2, '0'), str(today.hour).rjust(2, '0')+'00')
print(tmp)