import traceback
from datetime import timedelta, date
import datetime

class Pregnancy:
	def __init__(self, date, weeks, today):
		self.date  = date
		self.weeks = weeks
		self.today = today

	def weeks_pregnant(self):

		monday1 = (self.date  - timedelta(days=self.date.weekday()))
		monday2 = (self.today - timedelta(days=self.today.weekday()))
		print((monday2 - monday1).days / 7)
		weeks_passed = (monday2 - monday1).days / 7

		return weeks_passed + self.weeks

	def weeks_remain(self):
		return 41 - self.weeks_pregnant()

	def calc_due_date(self):
		return 41 - self.weeks_pregnant()

# set variables
date_created  = datetime.datetime(2020, 10, 25, 12, 56, 12, 352707)
today = datetime.datetime.now()

p1 = Pregnancy(date_created, 12, today)

dod_result  = p1.weeks_remain() 
week_result = p1.weeks_pregnant()
due_date    = p1.calc_due_date()

print(f"Weeks Pregnant: {week_result}")
print(f"Weeks Remaining: {dod_result}")
print(f"Due Date: {dod_result}")