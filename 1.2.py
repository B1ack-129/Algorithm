class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value is val:
                return node
            node = node.next
        return None 

    def find_all(self, val):
        list = []
        node = self.head
        while node is not None:
            if node.value is val:
                list.append(node)
            node = node.next
        return list 

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value is val:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                    pass
                elif node.prev is None:
                    self.head = node.next
                    node.next = None
                    node = self.head
                    if all is False:
                        pass
                elif node.next is None:
                    self.tail = node.prev
                    node.prev.next = None
                    pass
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                    node.next, node.prev = None
                    if all is False:
                        pass
            else:
                node = node.next
        pass 

    def clean(self):
        self.head, self.tail = None
        pass

    def len(self):
        num = 0
        node = self.node
        while node is not None:
            num += 1
            node = node.next
        return num

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None:
            node = self.tail
            newNode.prev = node
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value is afterNode.value:
                    if newNode.next is not None:
                        prevNode = newNode
                        while prevNode.next is not None:
                            prevNode = pNode.next
                        endNode = prevNode
                    else:
                        endNode = newNode
                    if node.next is self.tail:
                        self.tail = endNode
                    node.next.prev = endNode
                    endNode.next = node.next.prev
                    node.next = newNode
                    newNode.prev = node
                    pass
                node = node.next
        pass

    def add_in_head(self, newNode):
        node = self.head
        node.prev = newNode
        newNode.next = node
        self.head = newNode
        pass
