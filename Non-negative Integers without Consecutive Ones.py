'''
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.
'''


class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 2
        s = bin(n)[2:]
        num = len(s)
        dp = [1, 2] + [0]*(num-2)
        for i in range(2,num):
            dp[i] = dp[i-1] + dp[i-2]

        flag, ans = 0, 0
        for i in range(num):
            if s[i] == "0": continue
            if flag == 1: break
            if i > 0 and s[i-1] == "1": flag = 1
            ans += dp[-i-1]
        
        return ans + (flag != 1)
