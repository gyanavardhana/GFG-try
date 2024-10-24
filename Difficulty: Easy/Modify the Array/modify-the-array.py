#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        for i in range(n - 1):
            if arr[i] == arr[i + 1] and arr[i] != 0:
                arr[i] = arr[i] * 2
                arr[i + 1] = 0
        result = [x for x in arr if x != 0]  # Collect all non-zero elements
        zeros = [0] * (n - len(result))  # Append required number of zeros
        result.extend(zeros)
        return result


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends