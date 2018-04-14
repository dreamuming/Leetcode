from __future__ import print_function

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        snum = str(num)
        valid = ["69", "96", "00", "11", "88"]
        for i in range(len(snum)/2+1):
            if snum[i] + snum[-i-1] not in valid:
                return False
        return True


strobog = Solution()
print(strobog.isStrobogrammatic(161191))