class Solution(object):
	"""
	type n: int
	rtype: int
	"""
	def findNthDigit(self, n):
		digits = 1
		base = 9
		ith = 1

		while n > digits * base:
			n = n - digits * base
			digits = digits + 1
			ith = ith + base
			base = base * 10

		return ord(str((n-1)/digits+ith)[(n-1)%digits]) - ord('0')


solution = Solution()
print(solution.findNthDigit(23456))




