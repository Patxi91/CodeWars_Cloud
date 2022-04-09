from datetime import date, timedelta
import datetime


def friday_the_thirteenths(start, end=0):
    end = end + 1 if end!=0 else start+1
    def friday_13_in_year(y):
        day = date(y, 1, 1)
        end = date(y, 12, 31)
        one_day = timedelta(days=1)
        while day < end:
            if day.weekday() == 4 and day.day == 13:
                yield datetime.datetime.strptime(str(day), "%Y-%m-%d").strftime("%-m/%-d/%-Y")
            day += one_day

    return ' '.join( [str(d) for y in range(start, end) for d in friday_13_in_year(y)] )
