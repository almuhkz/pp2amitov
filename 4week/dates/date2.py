from datetime import datetime,timedelta
current_date = datetime.now()
difference = timedelta(days = 1)
print("Today is: " + str(current_date.strftime("%c")))
print("Yesterday was: "+str((current_date-difference).strftime("%c")))
print("Tommorow will be: "+ str((current_date+difference).strftime("%c")))