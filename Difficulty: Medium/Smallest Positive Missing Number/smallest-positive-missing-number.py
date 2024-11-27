#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr = [x for x in arr if x > 0]

        n = len(arr)
        presence = [False] * (n + 1)  

        for num in arr:
            if num <= n:
                presence[num] = True

        for i in range(1, n + 1):
            if not presence[i]:
                return i

        return n + 1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends