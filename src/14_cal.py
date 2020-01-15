"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import date

# calendar.setfirstweekday(6)
# print(calendar.firstweekday())

def make_cal(arg):
	x = input("Calendar? ")
	if arg is int:
		tc = calendar.TextCalendar(firstweekday = 0)
		print(tc.formatmonth(int(s), int(arg)))
	else:
		z = date.today()
		i = z.isoformat()
		y = date.fromisoformat(i)
		o = slice(0, 4)
		w = slice(5, 7)
		s = i[o]
		q = i[w]
		tc = calendar.TextCalendar(firstweekday = 0)
		print(tc.formatmonth(int(s), int(q)))

make_cal(int(5))