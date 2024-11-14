#User function Template for python3
import heapq
class Solution:
    def nearlySorted(self, arr, k):
        pq = []
        
        for i in range(k):
            heapq.heappush(pq,arr[i])
        index = 0
        for i in range(k,len(arr)):
            heapq.heappush(pq,arr[i])
            x = heapq.heappop(pq)

            arr[index] = x
            index += 1
        while pq:
            x = heapq.heappop(pq)
            arr[index] = x
            index += 1
        
        
        return arr

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends