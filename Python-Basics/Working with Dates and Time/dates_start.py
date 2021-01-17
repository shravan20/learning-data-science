from datetime import date
from datetime import time
from datetime import datetime


def main():
    #get current date
    today = date.today()
    print('Today\'s date is', today)
    
    #get current date component
    print('Date Components:', today.day, today.month, today.year)
    
    #get week component
    print('Today\'s Weekday:', today.weekday())
    
    print('Time Components:', datetime.now())


if __name__ == '__main__':
    main()