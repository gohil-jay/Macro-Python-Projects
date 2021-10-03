from datetime import date
today = date.today()

b_year = input('Enter birthday year')
b_month = input('Enter birthday month')
b_date = input('Enter date of your Birthday')
name = input('Name the birthday legend')
age = today.year - int(b_year)
if(today.month==int(b_month) and today.day==int(b_date)):
    print(f"Happy Birthday {name}")
    print(f"its your {age} birthday")
else:
    print(f"the coming birthday will be your {age+1} birthday")
