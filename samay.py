from datetime import datetime,timedelta
import re
class samay(object):
	__slots__ = '__mtime'
	def __init__(self,mtime=None):
		if mtime != None:
			if isinstance(mtime,datetime):
				self.__mtime = mtime
			elif isinstance(mtime,int):
				try:
					if len(str(mtime)) > 10:
						self.__mtime = datetime.fromtimestamp(mtime//1000)
					else:
						self.__mtime = datetime.fromtimestamp(mtime)
				except:
					print('Argument must be of epoch time')
			else:
				try:
					Checker__mtime = mtime.split(":")
					if len(Checker__mtime)==2:
						self.__mtime = datetime.strptime(mtime,"%Y-%m-%d %H:%M")
					elif len(Checker__mtime)==3:
						self.__mtime = datetime.strptime(mtime,"%Y-%m-%d %H:%M:%S")
				except Exception as e:
					print('Argument must be of format YYYY-MM-DD HH:mm')
		else:
			self.__mtime = datetime.now()

		if not self.__mtime:
			raise Exception('Argument must be instance of datetime')

	@property
	def mtime(self):
		return self.__mtime

	def startOf(self,arg):

		arg = str(arg).lower()

		if arg == "min" or arg=="minute" or arg=="minutes" or arg=="m":
			self.__mtime =  self.__mtime.replace(second=0, microsecond=0)
		elif arg == "hour" or arg=="hours" or arg=="h":
			self.__mtime =  self.__mtime.replace(minute=0, second=0, microsecond=0)
		elif arg == "day" or arg=="days" or arg=="d":
			self.__mtime =  self.__mtime.replace(hour=0, minute=0, second=0, microsecond=0)
		else:
			raise Exception('Argument 1 can be min,hour or day')
		return self

	def add(self,val,time):
		time = str(time).lower()
		try:
			val = int(val)
		except ValueError as e:
			raise Exception('1st Argument must be a integer in samay.Add')
			return

		if time == "sec" or time=="second" or time=="seconds" or time=="s":
			self.__mtime =  self.__mtime + timedelta(seconds=val)
		elif time == "min" or time=="minute" or time=="minutes" or time=="m":
			self.__mtime =  self.__mtime + timedelta(minutes=val)
		elif time == "hour" or time=="hours" or time=="h":
			self.__mtime =  self.__mtime + timedelta(hours=val)
		elif time == "day" or time=="days" or time=="d":
			self.__mtime =  self.__mtime + timedelta(days=val)
		else:
			raise Exception('Argument 2 can be min,hour or day')
		
		return self

	def set(self,val,time):
		time = str(time).lower()

		try:
			val = int(val)
		except ValueError as e:
			raise Exception('1st Argument must be a integer in samay.set')
			return

		if time == "min" or time=="minute" or time=="minutes" or time=="m":
			self.__mtime =  self.__mtime.replace(minute = val)
		elif time == "hour" or time=="hours" or time=="h":
			self.__mtime =  self.__mtime.replace(hour = val)
		elif time == "day" or time=="days" or time=="d":
			self.__mtime =  self.__mtime.replace(day = val)
		elif time == "month" or time=="M":
			self.__mtime =  self.__mtime.replace(month = val)
		elif time == "year" or time=="y":
			self.__mtime =  self.__mtime.replace(year = val)
		elif time == "sec" or time=="s" or time=="second":
			self.__mtime =  self.__mtime.replace(second = val)

		else:
			raise Exception('Argument 2 can be min,hour or day,month, year or second')
		
		return self

	def sub(self,val,time):
		time = str(time).lower()
		if not isinstance(val,int) :
			raise Exception('1st Argument must be a integer')
			return

		if time == "sec" or time=="second" or time=="seconds" or time=="s":
			self.__mtime =  self.__mtime - timedelta(seconds=val)
		elif time == "min" or time=="minute" or time=="minutes" or time=="m":
			self.__mtime =  self.__mtime - timedelta(minutes=val)
		elif time == "hour" or time=="hours" or time=="h":
			self.__mtime =  self.__mtime - timedelta(hours=val)
		elif time == "day" or time=="days" or time=="d":
			self.__mtime =  self.__mtime - timedelta(days=val)
		else:
			raise Exception('Argument 2 can be min,hour or day')
		
		return self

	def format(self,strArg=None):
		if not strArg:
			return self.__mtime.strftime("%Y-%m-%d %H:%M")
		strArg = str(strArg)
		strArg = strArg.replace("YYYY","%Y").replace("DD","%d").replace("dd","%d").replace("mm","%M").replace("MM","%m").replace("ss","%S").replace("hh","%H").replace("HH","%H")
		return self.__mtime.strftime(strArg)

	def __str__(self):
		return str(self.format("YYYY-MM-DD HH:mm"))

	def unix(self):
		return int(self.__mtime.strftime("%s"))*1000

	def __gt__(self,other):
		return self.__mtime > other.__mtime

	def __ge__(self,other):
		return self.__mtime >= other.__mtime

	def __eq__(self,other):
		return self.__mtime == other.__mtime

	def __lt__(self,other):
		return self.__mtime < other.__mtime

	def __le__(self,other):
		return self.__mtime <= other.__mtime

	def __sub__(self,other):
		return divmod(self.unix()//1000 - other.unix()//1000 , 60)[0]
