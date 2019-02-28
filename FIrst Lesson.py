class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        list = []
        while node is not None:
            if node.value == val:
                list.append(node)
            node = node.next
        return list  #1.4

    def delete(self, val, all=False):
        node = self.head
        node_past = None
        while node is not None:
            if node.value == val:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return
                elif node_past is None:
                    self.head = node.next
                    node.next = None
                    node = self.head
                    if all is False:
                        return
                elif node.next is None:
                    self.tail = node_past
                    node_past.next = None
                    return
                else:
                    node_past.next = node.next
                    node.next = None
                    node = node_past.next
                    if all is False:
                        return
            else:
                node_past = node
                node = node.next
        return #1.1 and 1.2

    def clean(self):
        self.head = None
        self.tail = None
        return #1.3

    def len(self):
        node = self.head
        s = 0
        while node is not None:
            s += 1
            node = node.next
        return s #1.5

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    if newNode.next is not None:
                        pNode = newNode
                        while pNode.next is not None:
                            pNode = pNode.next
                        endNode = pNode
                    else:
                        endNode = newNode
                    endNode.next = node.next
                    node.next = newNode
                    return
                node = node.next
        return # 1.6

    def get_head(self):
        if self.head is None:
            return None
        else:
            return self.head
    def get_tail(self):
        if self.tail is None:
            return None
        else:
            return self.tail

    def sum_list(self, list):
        if self.len() is not list.len():
            return
        else:
            d_list = LinkedList()
            node = self.head
            node_1 = list.head
            while node is not None:
                d_list.add_in_tail(Node(node.value + node_1.value))
                node = node.next
                node_1 = node_1.next
            return d_list
        return

def Test_Zero():
    o_list = LinkedList()
    #Test 'len'
    try:
        if o_list.len() is not 0:
            print('Error in function "len" with zero list')
            return
    except  Exception:
        print('Error in function "len" with zero list')
        return
    #Test 'clean'
    try:
        o_list.clean()
    except Exception:
        print('Error in function "clean" with zero list')
        return
    if len(o_list.find_all(1)) is not 0:
        print('Error in function "find_all" with zero list')
        return
    #Test 'delete(all = False)'
    try:
        o_list.delete(4)
    except Exception:
        print('Error in function "delete(all = False)" with zero list')
        return
    #Test 'delete(all = True)'
    try:
        o_list.delete(12, True)
    except Exception:
        print('Error in function "delete(all = True)" with zero list')
        return
    #Test 'insert'
    o_list.insert(None, Node(10))
    if o_list.get_head() is None or o_list.get_tail() is None:
        print('Error in function "insert" with zero list')
        return
    #Test 'find_all'
    if len(o_list.find_all(12)) is not 0:
        print('Error in function "find_all" with list of one symbol')
        return
    return "All right"





def Test_One():
    o_list = LinkedList()
    o_list.add_in_tail(Node(12))
    #Test 'len'
    try:
        if o_list.len() is not 1:
            print('Error in function "len" with list of one symbol')
            return
    except  Exception:
        print('Error in function "len" with list of one symbol')
        return
    #Test 'clean'
    try:
        o_list.clean()
    except Exception:
        print('Error in function "clean" with list of one symbol')
        return
    if o_list.len() is not 0:
        print('Error in function "clean" with list of one symbol')
        return
    #Test 'find_all'
    o_list.add_in_tail(Node(12))
    if len(o_list.find_all(12)) is not 1:
        print('Error in function "find_all" with list of one symbol')
        return
    #Test 'delete(all = False)'
    try:
        o_list.delete(10)
    except Exception:
        print('Error in function "delete(all = False)" with list of one symbol')
        return
    if o_list.len() is not 1:
        print('Error in function "delete(all = False)" with list of one symbol')
        return
    #Test 'delete(all = True)'
    try:
        o_list.delete(12, True)
    except Exception:
        print('Error in function "delete(all = True)" with list of one symbol')
        return
    if o_list.len() is not 0:
        print('Error in function "delete(all = True)" with list of one symbol')
        return
    o_list.add_in_tail(Node(12))
    #Test 'insert'
    o_list.insert(Node(12), Node(12))
    if o_list.len() is not 2:
        print('Error in function "insert" with list of one symbol')
        return
    #Test 'clean'
    try:
        o_list.clean()
    except Exception:
        print('Error in function "clean" with list of one symbol')
        return
    if o_list.get_head() is not None and o_list.get_tail() is not None:
        print('Error in function "clean" with list of one symbol')
        return
    return 'All right'



def Test():
    o_list = LinkedList()
    o_list.add_in_tail(Node(1))
    o_list.add_in_tail(Node(2))
    o_list.add_in_tail(Node(3))
    o_list.add_in_tail(Node(4))
    o_list.add_in_tail(Node(5))
    o_list.add_in_tail(Node(6))
    o_list.add_in_tail(Node(7))
    o_list.add_in_tail(Node(8))
    o_list.add_in_tail(Node(9))
    o_list.add_in_tail(Node(10))
    #Test 'len'
    try:
        if o_list.len() is not 10:
            print('Error in function "len" with list of symbols')
            return
    except  Exception:
        print('Error in function "len" with list of symbols')
        return
    #Test 'find_all'
    o_list.add_in_tail(Node(10))
    if len(o_list.find_all(10)) is not 2:
        print('Error in function "find_all" with list of symbols')
        return

    #Test 'delete(all = False)'
    try:
        o_list.delete(10)
    except Exception:
        print('Error in function "delete(all = False)" with list of symbols')
        return
    if len(o_list.find_all(10)) is not 1:
        print('Error in function "delete(all = False)" with list of symbols')
    #Test 'delete(all = True)'
    o_list.add_in_tail(Node(1))
    try:
        o_list.delete(1, True)
    except Exception:
        print('Error in function "delete(all = True)" with list of symbols')
        return
    if len(o_list.find_all(1)) is not 0 or o_list.len() is not 9:
        print('Error in function "delete(all = True)" with list of symbols')
        return
    #Test 'insert'
    o_list.insert(Node(5), Node(5))
    if o_list.len() is not 10:
        print('Error in function "insert" with list of symbols')
        return
    #Test 'clean'
    try:
        o_list.clean()
    except Exception:
        print('Error in function "clean" with list of symbols')
        return
    if o_list.get_head() is not None and o_list.get_tail() is not None:
        print('Error in function "clean" with list of symbols')
        return
    return "All right"
