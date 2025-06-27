from datetime import datetime

date_str = input("Enter the date (YYYY-MM-DD): ")
st_str = "%b %d %Y %I:%M %p"
date = datetime.strptime(date_str, st_str)
new_year = datetime(date.year + 1, 1, 1, 0, 0)
diff = new_year - date 
total_minutes = int(diff.total_seconds() // 60)
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{hours} hours {minutes} minutes")

