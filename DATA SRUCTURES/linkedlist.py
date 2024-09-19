class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    # Method for inserting values in linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head # Points to the head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head # Points to the head
    
    # Method for displaying the values in a linked list
    def display(self):
        if self.head is None:
            return
        
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            
            if current == self.head:
                break # Exit the loop when we reach the head again

    # Method to count the nodes
    def count_nodes(self):
        count = 0
        if self.head is None:
            return count
        else:
            count = 1

            current = self.head
            while current.next != self.head:
                count += 1
                current = current.next

            return count

linked_list = CircularLinkedList()

# Append values inside the linked list
linked_list.append(5)
linked_list.append(9)
linked_list.append(11)
linked_list.append(17)
linked_list.append(35)
linked_list.append(57)
linked_list.append(83)

# Display the values
print("Circular Linked List Data:")
linked_list.display()

# Display the number of nodes
print("\n\nNumber of nodes:", linked_list.count_nodes())