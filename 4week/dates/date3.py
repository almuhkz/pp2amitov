import datetime
current_date = datetime.datetime.today()
formatted_date = current_date.replace(microsecond=0)
print(formatted_date)