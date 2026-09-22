from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        low = 0
        f = defaultdict(int)
        n = len(s)
        res = -float('INF')
        for high in range(n):
            f[s[high]] += 1
            while(len(f) > k):
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del f[s[low]]
                low += 1
            if len(f) == k:
                l = high - low + 1
                res = max(res,l)
        if res != -float('INF'):
            return res
        else:
            return -1
            