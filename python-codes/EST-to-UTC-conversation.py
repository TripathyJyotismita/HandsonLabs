import datetime
from datetime import timedelta

from_date='2018-12-12T02:12'
sd=from_date.replace("T"," ")
u_sd=datetime.datetime.strptime(sd,'%Y-%m-%d %H:%M')
utc_to_time=u_sd+timedelta(hours=+4)
print('utc_to_time:',utc_to_time)
sutc_to_time=str(utc_to_time)
print(sutc_to_time)
print(from_date)
s=(str((datetime.datetime.strptime(from_date.replace("T"," "),'%Y-%m-%d %H:%M')))[:-3])
print(s)
print(s)
#s='2017-12-12 16:12:00'



