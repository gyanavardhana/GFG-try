from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        p = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                p += prices[i+1]-prices[i]
        return p



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends