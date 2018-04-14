from __future__ import print_function

class Solution(object):

	def __init__(self):
		self.dic = {}

	def groupShifttedString(self, strings):

		for s in strings:
			hash = self.hashString(s)

			if hash not in self.dic: 
				self.dic[hash] = [s] # notice, change the string to a list element

			else:
				self.insertString(hash, s)
		
		for value in self.dic.values():
			value.sort()

		return self.dic.values()


	def insertString(self, hash, astring):
		self.dic[hash].append(astring)

	def hashString(self, s):
		hash = [] # need to initialize the list
		for i in s:
			diff = (ord(i) + 26 - ord(s[0])) % 26
			hash.append(diff)
		return tuple(hash)

test = Solution()
strings = ["ab", "cd", "efg", "acf", "bdg","ef", "abc", "cde",]
print(test.groupShifttedString(strings))







