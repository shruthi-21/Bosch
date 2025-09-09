class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next   
        current.next = prev         
        prev = current            
        current = next_node      
    return prev 

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")
node1 = SinglyLinkedListNode(1)
node2 = SinglyLinkedListNode(2)
node3 = SinglyLinkedListNode(3)

node1.next = node2
node2.next = node3

print("Original Linked List:")
printLinkedList(node1)
new_head = reverse(node1)
print("\nReversed Linked List:")
printLinkedList(new_head)
