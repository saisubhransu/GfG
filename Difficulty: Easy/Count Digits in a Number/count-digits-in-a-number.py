class Solution:
    def countDigits(self, n):
        # code here
        num = abs(n)
        count = 0
        while(num > 0):
            last = num % 10
            num //= 10
            count += 1
        return count    
