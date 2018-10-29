from datetime import datetime,timedelta
import re
class samay:

	def __init__(self,mtime=None):
		if mtime != None:
			if isinstance(mtime,datetime):
				self.mtime = mtime
			elif isinstance(mtime,int):
				try:
					if len(str(mtime)) > 10:
						self.mtime = datetime.fromtimestamp(mtime//1000)
					else:
						self.mtime = datetime.fromtimestamp(mtime)
				except:
					print('Argument must be of epoc time')
			else:
				try:
					Checkermtime = mtime.split(":")
					if len(Checkermtime)==2:
						self.mtime = datetime.strptime(mtime,"%Y-%m-%d %H:%M")
					elif len(Checkermtime)==3:
						self.mtime = datetime.strptime(mtime,"%Y-%m-%d %H:%M:%S")
				except Exception as e:
					print('Argument must be of format YYYY-MM-DD HH:mm')
		else:
			self.mtime = datetime.now()

		if not self.mtime:
			raise Exception('Argument must be instance of datetime')


	def startOf(self,arg):

		arg = str(arg).lower()

		if arg == "min" or arg=="minute" or arg=="minutes" or arg=="m":
			self.mtime =  self.mtime.replace(second=0, microsecond=0)
		elif arg == "hour" or arg=="hours" or arg=="h":
			self.mtime =  self.mtime.replace(minute=0, second=0, microsecond=0)
		elif arg == "day" or arg=="days" or arg=="d":
			self.mtime =  self.mtime.replace(hour=0, minute=0, second=0, microsecond=0)
		else:
			raise Exception('Argument 1 can be min,hour or day')
		return self

	def add(self,val,time):
		time = str(time).lower()
		if not isinstance(val,int) :
			raise Exception('1st Argument must be a integer')
			return

		if time == "min" or time=="minute" or time=="minutes" or time=="m":
			self.mtime =  self.mtime + timedelta(minutes=val)
		elif time == "hour" or time=="hours" or time=="h":
			self.mtime =  self.mtime + timedelta(hours=val)
		elif time == "day" or time=="days" or time=="d":
			self.mtime =  self.mtime + timedelta(days=val)
		else:
			raise Exception('Argument 2 can be min,hour or day')
		
		return self

	def sub(self,val,time):
		time = str(time).lower()
		if not isinstance(val,int) :
			raise Exception('1st Argument must be a integer')
			return

		if time == "min" or time=="minute" or time=="minutes" or time=="m":
			self.mtime =  self.mtime - timedelta(minutes=val)
		elif time == "hour" or time=="hours" or time=="h":
			self.mtime =  self.mtime - timedelta(hours=val)
		elif time == "day" or time=="days" or time=="d":
			self.mtime =  self.mtime - timedelta(days=val)
		else:
			raise Exception('Argument 2 can be min,hour or day')
		
		return self

	def format(self,strArg):
		strArg = str(strArg)
		strArg = strArg.replace("YYYY","%Y").replace("DD","%d").replace("dd","%d").replace("mm","%M").replace("MM","%m").replace("ss","%S").replace("hh","%H").replace("HH","%H")
		return self.mtime.strftime(strArg)

	def __str__(self):
		return str(self.format("YYYY-MM-DD HH:mm"))

	def unix(self):
		return int(self.mtime.strftime("%s"))*1000

	def __gt__(self,other):
		return self.mtime > other.mtime

	def __eq__(self,other):
		return self.mtime == other.mtime
	def __lt__(self,other):
		return self.mtime < other.mtime