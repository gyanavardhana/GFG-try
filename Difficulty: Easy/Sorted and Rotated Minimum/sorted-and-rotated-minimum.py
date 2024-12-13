#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        for i in range(1, len(arr)):
            if arr[i]<arr[i-1]:
                return arr[i]
        return min(arr)

#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends