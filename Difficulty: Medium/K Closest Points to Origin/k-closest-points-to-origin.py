#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        dict={}
        value=[]
        for i in points:
            ans=0
            for j in i:
                ans+=j*j
            ans=ans**0.5
            value.append(ans)
            if ans in dict:
                dict[ans].append(i)
            else:
                dict[ans]=[i]
        sorted_values=sorted(dict.keys())
        value1=[]
        
        for i in range(len(sorted_values)):
            
            if len(dict[sorted_values[i]])>1:
                
                for j in range(len(dict[sorted_values[i]])):
                    
                    value1.append(dict[sorted_values[i]][j])
                    
            else:
                value1.append(dict[sorted_values[i]][0])
        return value1[0:k]
        
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends