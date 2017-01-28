#https://www.hackerrank.com/challenges/calendar-module
import calendar
mm,dd,yy=map(int, input().split())
dayNo=calendar.weekday(yy,mm,dd)
print((calendar.day_name[dayNo]).upper()) #Fetching day from array and converting to upper case
