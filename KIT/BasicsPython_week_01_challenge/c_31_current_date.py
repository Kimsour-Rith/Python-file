from datetime import date
def current_date():
    today = date.today()
    day = today.strftime("%d/%m/%y")  # dd/mm/YY
    return str(day)

from datetime import datetime
def current_time():
    now = datetime.now()
    dt_now = now.strftime("%H:%M:%S")
    return str(dt_now)

print(current_date())
print(current_time())
print(type(current_date()))
print(type(current_time()))
