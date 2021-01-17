
import calendar


#create a plain calendar object

c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2021,1,0,0)
print(st)

# create an html formatted calendar object
c = calendar.HTMLCalendar(calendar.SUNDAY)
st = c.formatmonth(2021,1)
print(st)