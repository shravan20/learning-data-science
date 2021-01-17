from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta



def main():
    #construct a basic timedelta
    print(timedelta(days=365,hours=5,minutes=1))

    #print a today's date
    now = datetime.now()
    #printing today's date from 1 year now
    print('One year from now', str(now+timedelta(days=365,hours=5,minutes=1)))
    
    #calculae a date 1 week ago
    t = datetime.now()- timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print('A week back it was ', s)


if __name__ == '__main__':
    main()