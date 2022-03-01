import datetime
current_date = datetime.datetime.today()
second_date = datetime.datetime(year = 2001,month = 8, day = 3)
difference =current_date - second_date
print(difference.total_seconds())