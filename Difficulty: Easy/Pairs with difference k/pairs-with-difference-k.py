#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	d = {}
        count = 0
        for i in arr:
            if i-k in d:
                count += d[i-k]
            if i+k in d:
                count += d[i+k]
            d[i] = d.get(i, 0) + 1
        return count





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends