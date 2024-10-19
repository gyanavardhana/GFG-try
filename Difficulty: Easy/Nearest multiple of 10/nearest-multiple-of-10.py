#User function Template for python3

class Solution:
    def roundToNearest (self, str_num) : 
        #Complete the function
        n = len(str_num)
    
        if str_num[n-1] <= '5':
            str_num = str_num[:n-1] + '0'
            return str_num
        
        str_num = str_num[:n-1] + '0'
        i = n - 2
        
        while i >= 0 and str_num[i] == '9':
            str_num = str_num[:i] + '0' + str_num[i+1:]
            i -= 1
        
        if i < 0:  # for cases like "9", "99", "999", etc.
            return '1' + str_num
        else:
            str_num = str_num[:i] + chr(ord(str_num[i]) + 1) + str_num[i+1:]
        
        return str_num




#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends