#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        rows,cols = len(grid),len(grid[0])
        c = 0
        visit = set()
        if not grid:
            return 0
        def bfs(r,c):
            q=[]
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c = q.pop()
                dire = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
                for dr,dc in dire:
                    row = r+dr
                    col = c+dc
                    if(0<=row<rows and 0<=col<cols
                    and grid[row][col]==1 and (row,col) not in visit):
                        visit.add((row,col))
                        q.append((row,col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    bfs(i,j)
                    c+=1
        return c
#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends