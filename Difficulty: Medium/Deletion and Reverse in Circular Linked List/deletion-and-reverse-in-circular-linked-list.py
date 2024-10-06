#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if head is None or head.next == head:
            return head
        
        prev = None
        current = head
        next_node = None
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            if current == head:
                break
        
        head.next = prev
        head = prev  # Update the head to the new first element
        
        return head
        
    def deleteNode(self, head, key):
        if head is None:
            return None
            
        if head.data == key and head.next == head:
            return None  # Only one node in the list
        
        current = head
        prev = None
        
        # Deleting the head
        if head.data == key:
            while current.next != head:  # Find the last node
                current = current.next
            
            current.next = head.next  # Bypass the head
            head = head.next  # Update head to the next node
            return head
        
        # Search for the key to delete
        current = head
        while current.next != head and current.next.data != key:
            current = current.next
            
        if current.next.data == key:  # If the key is found
            current.next = current.next.next  # Bypass the node to delete
            
        return head

            
            
            
        
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        key = int(input())

        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        tail.next = head  # Make the list circular

        ob = Solution()
        head = ob.deleteNode(head, key)
        head = ob.reverse(head)
        printList(head)

# } Driver Code Ends