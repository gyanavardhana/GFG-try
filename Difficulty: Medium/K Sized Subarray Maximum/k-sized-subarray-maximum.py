class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        cur_max = max(arr[:k])
        ans = [cur_max]
        # Iterate through all the windows
        for i in range(len(arr)-k):
            # The curent max should not be in the previous window
            if cur_max != arr[i]:
                cur_max = max(cur_max, arr[i+k])
            # If the current max is in the previous window
            else:
                cur_max = max(arr[i+1:i+k+1])
            ans.append(cur_max)
        return ans


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
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends