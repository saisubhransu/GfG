class Solution:
    def countTriplets(self, sum, arr):
        #code here
        arr.sort()
        n = len(arr)
        count = 0
        for i in range(0,n-2):
            left = i + 1
            right = n - 1
            while(left < right):
                add = arr[i] + arr[left] + arr[right]
                if add >= sum:
                    right -= 1
                else:
                    count += (right-left)
                    left += 1
        return count            
                    
                