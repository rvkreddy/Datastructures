
# Define the node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def set_next(self, nextnode):
        self.next = nextnode

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class circularLinkedList(object):

    def __init__(self):
        self.head = None
        self.length = 0

    def get_length(self):
        return self.length

    # method to add a node in the linked list
    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)

    # method to add a node at the beginning of the list with a data
    def addBeg(self, node):
        newnode = node
        newnode.next = self.head
        self.head = newnode
        self.head.next = self.head
        self.length += 1


    # 1.Traverse from head to the last node
    # 2.set its next node to given node
    # 3. set given nodes next to None
    # 4.Increment the length
    # method to add a node at the end of a list
    def addLast(self, node):
        currentnode = self.head

        while currentnode.next != self.head:
            currentnode = currentnode.next

        newNode = node
        newNode.next = self.head
        currentnode.next = newNode
        self.length = self.length + 1


    def findnodeno(self):
        temp = self.head.next
        count = 1
        while temp is not self.head:
            temp = temp.next
            count += 1

        return count



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
print("create circular linked list")
ll = circularLinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
ll.addNode(node6)
ll.addNode(node7)
ll.addNode(node8)
print("No of nodes in circular linked list")
print(ll.findnodeno())
print(ll.get_length())