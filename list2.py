class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def sort_list(self):
        if self.head is None:
            return
        end = self._get_tail(self.head)
        self._quick_sort(self.head, end)

    def _get_tail(self, node):
        while node.next:
            node = node.next
        return node

    def _partition(self, start, end):
        pivot = end
        current = start
        while start != end:
            if start.data < pivot.data:
                start.data, current.data = current.data, start.data
                current = current.next
            start = start.next
        pivot.data, current.data = current.data, pivot.data
        return current

    def _quick_sort(self, start, end):
        if start != end and end != None and start != end.next:
            pivot = self._partition(start, end)
            self._quick_sort(start, pivot.prev)
            self._quick_sort(pivot.next, end)


dllist = DoublyLinkedList()
dllist.append(3)
dllist.append(1)
dllist.append(2)

print("Doubly Linked List:")
dllist.print_list()