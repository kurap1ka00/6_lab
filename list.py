class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def sort_list(self):
        if self.head is None:
            return

        new_head = None
        current = self.head

        while current:
            next_node = current.next
            if new_head is None or current.data <= new_head.data:
                current.next = new_head
                new_head = current
            else:
                search = new_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node

        self.head = new_head

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.data) + " "
            current_node = current_node.next
        return result


llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)

print("Before sorting:")
print(llist)

llist.sort_list()

print("After sorting:")
llist.print_list()
