from __future__ import print_function

class LoggerRateLimit(object):
	def __init__(self):
		self.map = {}

	def shouldPrintMessage(self, msg, t):
		if msg not in self.map or (t - self.map[msg]) >= 10:
			self.map[msg] = t
			result = True
		else:
			result = False

		return result

logger = LoggerRateLimit()
print(logger.shouldPrintMessage("foo",1))
print(logger.map)
print(logger.shouldPrintMessage("foo",3))
print(logger.map)
print(logger.shouldPrintMessage("foo",14))
print(logger.map)