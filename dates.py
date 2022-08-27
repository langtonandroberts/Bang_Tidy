

#https://youtu.be/Zs9u8TAv4_k
#https://youtu.be/jngHjpBiiKo
#https://youtu.be/qk7qqbZxJGo
#Dates.

from datetime import datetime, timedelta 


#,,,returns date as Datetime objects. you must convert to a string(strftime)
curr_datetime=datetime.now()
curr_date=curr_datetime.date()
curr_time=curr_datetime.time()
print(curr_datetime)
print(curr_date)
print(curr_time)

#,,,another way to return date
today=datetime.now()
print("Day: " + str(today.day))
print("Month: " + str(today.month))
print("Year: " + str(today.year))
print("Hour: " + str(today.hour))
print("Minute: " + str(today.minute))

#,,,strftime() creates a string representation of a datetime object.
#curr_datetime=datetime.now()#retuns (2022-07-13 19:29:37.029066) string format.
#req_format=datetime.strftime(curr_datetime,'%d/%m/%Y %H-%M-%S')#change the format to (2022/07/13 19-29-37) string format.
#print(req_format)

#,,,strptime() the oppersit to strftime, converts back to datetime.
#dt_string= '2019/07/01 4:32:51'
#print(dt_string)
#print(datetime.strptime(dt_string,"%Y/%m/%d %H:%M:%S"))

#,,yesterdays date
one_day=timedelta(days=1)
one_week=timedelta(weeks=1)
yesterday=curr_date-one_day
last_week=curr_date-one_week
print("Yesterday was: " + str(yesterday))
print("Last week was: " + str(last_week))










