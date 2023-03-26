from time import sleep
from datetime import datetime, timedelta
from playsound import playsound
from pathlib import Path

class Timer:
	"""
	base timer class that counts down the seconds and
	activates an alarm
	"""
	def __init__(self, min, sec = 0, output='TIMER'):
		# set arguments
		self.min = min
		self.sec = sec
		self.output = output
		# resolve path for mp3 to play
		self.alarm_mp3 = str(
			(Path(__file__).parent / 'alarm.mp3')
			.resolve())

	def start(self):
		"""
		prints information for user, starts timer
		and plays the alarm file
		"""
		time_sleep = self.min * 60 + self.sec
		self.__user_info()
		sleep(time_sleep)
		print('FINISHED {}'.format(self.output))
		playsound(self.alarm_mp3)

	def __user_info(self):
		"""
		timer information for user
		prints purpose (default 'TIMER'),
		time to run, start time and end time
		"""
		start = datetime.now()
		time_sleep = timedelta(minutes=self.min, seconds=self.sec)
		end = start + time_sleep
		print('-------------------------------------------')
		print('{}:'.format(self.output))
		print(time_sleep)
		print()
		print('start time:')
		print(start.strftime('%H:%M:%S'))
		print()
		print('end time:')
		print(end.strftime('%H:%M:%S'))
		print('-------------------------------------------')
