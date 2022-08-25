


#https://youtu.be/jngHjpBiiKo
#https://youtu.be/qk7qqbZxJGo
#Dates.

from datetime import datetime 

#Datetime objects.
curr_datetime=datetime.now()
curr_date=curr_datetime.date()
curr_time=curr_datetime.time()

print(curr_datetime)
print(curr_date)
print(curr_time)

# strftime() creates a string representation of a datetime object.
curr_datetime=datetime.now()#retuns (2022-07-13 19:29:37.029066) string format.
req_format=datetime.strftime(curr_datetime,'%d/%m/%Y %H-%M-%S')#change the format to (2022/07/13 19-29-37) string format.
print(req_format)

# strptime() the oppersit to strftime, converts back to datetime.
dt_string= '2019/07/01 4:32:51'
print(dt_string)
print(datetime.strptime(dt_string,"%Y/%m/%d %H:%M:%S"))














