
class Solution:
    def countTriplets(self, arr, target):
        # code here
        d1 = {}
        d2 = {}
        res = 0
        for v in arr:
            res += d2.get(target-v, 0)
            for v2 in d1:
                d2[v+v2] = d2.get(v+v2,0)+d1.get(v2,0)
            d1[v] = d1.get(v,0)+1
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends