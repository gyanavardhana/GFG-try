#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        n=len(arr)
        currSum=arr[0]
        i,j=0,0
        while True:
            if currSum==target:
                return [i+1,j+1]
            elif currSum>target:
                currSum-=arr[i]
                i+=1
            else:
                j+=1
                if j==n:
                    return [-1]
                currSum+=arr[j]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends