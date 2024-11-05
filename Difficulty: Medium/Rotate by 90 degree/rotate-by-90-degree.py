#User function Template for python3

def rotate(matrix): 
    #code here
    newmat = []
    for i in range(len(matrix[0])):
        submat = []
        for j in range(len(matrix)-1,-1,-1):
            submat.append(matrix[j][i])
        newmat.append(submat)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = newmat[i][j]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends