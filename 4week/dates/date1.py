from datetime import datetime,timedelta
current_date = datetime.now()
five_days = timedelta(days = 5)
print(current_date-five_days)