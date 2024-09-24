#User function Template for python3
class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        d = {}
        for char in p:
            d[char] = d.get(char, 0) + 1
        i = 0
        ml = float('inf')
        mwind = ""
        dd = {}
        count = 0  

        for j in range(len(s)):
            char = s[j]
            dd[char] = dd.get(char, 0) + 1
            if char in d and dd[char] == d[char]:
                count += 1
            while count == len(d):
                if j - i + 1 < ml:
                    ml = j - i + 1
                    mwind = s[i:j + 1]
                dd[s[i]] -= 1
                if s[i] in d and dd[s[i]] < d[s[i]]:
                    count -= 1
                i += 1

        return mwind if ml != float('inf') else "-1"

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends
