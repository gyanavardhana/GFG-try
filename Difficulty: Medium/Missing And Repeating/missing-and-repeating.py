#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        s = n*(n+1)//2
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l = []
        a = 0
        for i in d.keys():
            l.append(i)
            if d[i]==2:
                a = i
        b = s-sum(l)
        return a,b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends