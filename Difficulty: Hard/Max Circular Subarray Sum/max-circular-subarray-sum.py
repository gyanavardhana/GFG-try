#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    tot = 0
    masum = cma = float('-inf')
    misum = cmi = float('inf')
    for i in arr:
        cma = max(i, cma + i)
        masum = max(masum, cma)
        cmi = min(i, cmi+i)
        misum = min(misum, cmi)
        tot += i
    return max(masum, tot-misum, tot)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends