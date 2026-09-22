class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k
        sum = 0
        n = len(arr)
        for i in range(k):
            sum += arr[i]
        
        res = sum
        while high < n:
            sum = sum - arr[low] + arr[high]
            res = max(sum,res)
            low += 1
            high += 1
        return res    