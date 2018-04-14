from __future__ import print_function

class Solution(object):
	def addStringNumber(self, num1, num2):
		
		result = []
		div1, div2 = len(num1), len(num2)
		carry = 0
		digit = 0
		while div1 or div2 or carry:
			digit = carry

			if div1:
				div1 -= 1
				digit += int(num1[div1])
			if div2:
				div2 -= 1
				digit += int(num2[div2])

			carry = digit > 9
			result.append(str(digit%10))

		return ''.join(result[::-1])

addstring=Solution()
print(addstring.addStringNumber("123","456"))


	
