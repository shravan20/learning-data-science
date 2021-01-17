from datetime import date
from datetime import time
from datetime import datetime


def main():
    #get current datetime
    now = datetime.now()
    print(now.strftime('Current year is %Y'))

    #%y %a %b %d == year,weekday,month,dayOfMonth
    print(now.strftime('Current year is %Y'))
    print(now.strftime('Current weekday is %a'))
    print(now.strftime('Current month is %b'))
    print(now.strftime('Current dayOfMonth is %d'))

    #%x == localTime for a given location
    #%c == local date + local time
    print(now.strftime('localTime = %x'))
    print(now.strftime('localTime = %X'))
    print(now.strftime('localDateTime = %c'))




if __name__ == '__main__':
    main()