class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next
        
node1 = SinglyLinkedListNode(10)
node2 = SinglyLinkedListNode(20)
node3 = SinglyLinkedListNode(30)

node1.next = node2
node2.next = node3

printLinkedList(node1)