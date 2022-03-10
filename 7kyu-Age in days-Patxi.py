from datetime import date

def age_in_days(year, month, day):
    bday = date(year, month, day)
    today = date.today()
    delta = today - bday
    return f'You are {delta.days} days old'
