from weather import *
import datetime as dt
import pickle
today = dt.datetime.today()
print(today)
c = '12'
print(c.rjust(2, '0'))
print(str(today.year)+str(today.month)+str(today.day), str(today.hour).rjust(2, '0')+'00')
a, b = short_term_situation(str(today.year)+str(today.month)+str(today.day), str(today.hour).rjust(2, '0')+'00')
print(a)
with open('events', 'rb') as f:
        events = pickle.load(f)
        print(events)
# del events[(2023, 12, 32)]
# del events[(2023, 8, 32)]
# with open('events', 'wb') as f:
#         pickle.dump(events, f)