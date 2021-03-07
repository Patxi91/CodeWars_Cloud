
import datetime


def make_readable(seconds):
    t = datetime.timedelta(seconds=seconds)
    sol = str(t.days*24 + int(str(t).split()[-1][:-6])) + ':' + str(t).split()[-1][-5:]
    return sol if len(sol) == 8 else '0'+sol
