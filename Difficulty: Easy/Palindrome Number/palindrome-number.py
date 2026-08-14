class Solution:
    def isPalindrome(self, n):
		# code here
		num = abs(n)
		res = 0
		while(num > 0):
		    last = num % 10
		    res = (res * 10) + last
		    num = num // 10
		return abs(n) == res    