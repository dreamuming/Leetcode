from __future__ import print_function

class Solution(object):
	def __init__(self):
		self.map = {}
		self.odd = 0
	def ifPalindrome(self, s):
		self.__init__()
		for i in range(0, len(s)):
			self.map[s[i]] = 1 if s[i] not in self.map else self.map[s[i]] + 1
		print(self.map)
		for i in range(0, len(s)):
			if (self.map[s[i]] % 2 != 0):
				self.odd = self.odd + 1
		return False if self.odd > 1 else True



palin = Solution()
print (palin.ifPalindrome("abb"))

print (palin.ifPalindrome("code"))
print (palin.ifPalindrome("carerac"))


