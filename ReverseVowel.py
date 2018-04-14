from __future__ import print_function

class Solution(object):

    def reverseVowel(self, s):

        result = []
        left, right = 0, len(s)-1


        VOWELS = ['a', 'e', 'i', 'o', 'u']

        while True:

            if s[left].lower() not in VOWELS and left < len(s):
                left += 1
            if s[right].lower() not in VOWELS and right >=0:
                right -= 1

            if left > right:
                break

            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

        return ''.join(s)


reversevowel = Solution()
s = list("aeiou")
print(reversevowel.reverseVowel(s))






