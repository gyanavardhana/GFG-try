
class Solution:
    def maxLength(self, s):
        # code here
        res = 0
        st = []
        st.append(-1)
        
        for i in range(len(s)):
            c = s[i]
            
            if c == '(':
                st.append(i)
            else:
                if st:
                    st.pop()
                
                if st:
                    res = max(res, i - st[-1])
                else:
                    st.append(i)
        
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends