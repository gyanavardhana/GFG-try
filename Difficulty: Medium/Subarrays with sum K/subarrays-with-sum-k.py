#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        res =0
        c=0
        sum_freq={0:1}
        n=len(arr)
        for i in range(n):
            res+=arr[i]
            target=res-k
            if target in sum_freq:
                c+=sum_freq[target]
            sum_freq[res]=sum_freq.get(res,0)+1
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends