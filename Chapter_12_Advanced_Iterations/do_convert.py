from datetime import datetime
from pprint import pprint


def convert_to_ampm(time24: str) -> str:
    """ Convert 24h time format to 12h (AM, PM) """
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:  # open csv file
    ignore = data.readline()  # ignore title
    flights = {}  # create new empty dict
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


pprint(flights)
print()

fts = {convert_to_ampm(k): v.title() for k, v in flights.items()}

pprint(fts)
print()

wests = [k for k, v in fts.items() if v == 'West End']

when = {}
for i in set(fts.values()):
    when[i] = [k for k, v in fts.items() if v == i]

pprint(when)
print()

when2 = {i: [k for k, v in fts.items() if v == i] for i in set(fts.values())}

pprint(when2)
print()






