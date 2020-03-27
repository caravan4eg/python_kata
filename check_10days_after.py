# ввод сначала месяц, потом день
# результат False/True будет ли через 10 дней тот же месяц
import datetime as dt


def check_10days_after(month, day):
    cur_date = dt.date(year=2020, month=month, day=day)

    future_date =  dt.date(year=2020, month=month, day=day) + dt.timedelta(days=10)
    return cur_date.month == future_date.month

print(f'It\'ll be the same month in 10 days? {check_10days_after(2, 25)}')
