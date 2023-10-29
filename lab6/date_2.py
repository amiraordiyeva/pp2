from datetime import date, datetime, timedelta
yesterday= datetime.today()- timedelta(days=1)
print(yesterday)
today=datetime.today()
print(today)
tomorrow=datetime.today()+ timedelta(days=1)
print(tomorrow)