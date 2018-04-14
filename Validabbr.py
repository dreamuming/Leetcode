from __future__ import print_function

class Solution(object):
	"""

	"""
	def validAbbr(self, word, abbr):

		i, digit = 0, 0
		for c in abbr:
			if c.isdigit():
				if digit == 0 and c == '0':
					return False
				else:
					digit = digit * 10
					digit += int(c)


			else:
				if digit:
					i = i + digit
					digit = 0
				if i >= len(word):
					return False
				if word[i] != c:
					return False
				else:
					i += 1
		if digit:
			i += digit
		else:
			return i == len(word)

validabbr = Solution()
print (validabbr.validAbbr("internationalization","i11iz4n"))
