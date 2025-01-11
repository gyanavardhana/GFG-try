#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        st = 0
        d = {}
        ml = 0
        for e in range(len(s)):
            if s[e] not in d:
                d[s[e]] = e
            else:
                ml= max(ml, len(d))
                i = d[s[e]]
                while st <= i:
                    del d[s[st]]
                    st += 1
                d[s[e]] = e
        return max(ml, len(d))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends