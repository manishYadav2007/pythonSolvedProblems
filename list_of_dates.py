from datetime import datetime, timedelta


start_date = input("Enter the string date: ")
end_date = input("Enter the end date: ")

start_dt_format = "%b %d %Y"
end_dt_format = "%b %d %Y"


date1 = datetime.strptime(start_date, start_dt_format)
date2 = datetime.strptime(end_date, end_dt_format)


days = (date2 - date1).days 

for each_day in range(1, days + 1):
    list_of_date = date1 + timedelta(days=each_day)
    print(list_of_date)
    
    
    



