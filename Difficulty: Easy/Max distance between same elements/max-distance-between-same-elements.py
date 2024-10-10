class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]].append(i)
            else:
                d[arr[i]] = [i]
        m  = 0
        for i in d.keys():
            m = max(m, max(d[i])-min(d[i]))
        return m


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends