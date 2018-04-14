from __future__ import print_function

def guess(n):
	if n < 56:
		return -1
	elif n > 56:
		return 1
	else:
		return 0


class Solution(object):

	def guessNumber(self, n):

		left, right = 1, n
		mid = 0

		while left <= right:
			mid = (left + right) / 2
			trial = guess(mid)
			if trial == -1:
				left = mid
			elif trial == 1:
				right = mid
			else:
				return mid


guessnumber = Solution()

print(guessnumber.guessNumber(100))

