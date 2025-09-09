class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        last = self.head
        while last.next :
            last = last.next
        last.next = new_node
        
    def get_node_value(self, pos):
        current = self.head
        index = 0
        while current:
            if index == pos:
                return current.data
            current = current.next
            index += 1
        return None


#  Create linked list with 3 values
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
 
# Print the list
print("Linked List values:")
pos = 1
print(f"Value at position {pos}:", ll.get_node_value(pos))  
 
