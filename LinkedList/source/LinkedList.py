import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode


class LinkedList(object):

    # initializing a list
    def __init__(self):
        self.length = 0
        self.head = None

    def get_length(self):
        return self.length

    def get_head(self):
        return self.head

    # method to add a node in the linked list
    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)

    # method to add a node at the beginning of the list with a data
    def addBeg(self, node):
        newnode = node
        newnode.nextnode = self.head
        self.head = newnode
        self.head.nextnode = None
        self.length += 1


    # 1.Traverse from head to the last node
    # 2.set its next node to given node
    # 3. set given nodes next to None
    # 4.Increment the length
    # method to add a node at the end of a list
    def addLast(self, node):
        currentnode = self.head

        while currentnode.nextnode != None:
            currentnode = currentnode.nextnode

        newNode = node
        newNode.nextnode = None
        currentnode.nextnode = newNode
        self.length = self.length + 1



    # method to add a node after the node having the data=data. The data of the new node is value2
    def addAfterValue(self, data, node):
        newNode = node
        currentnode = self.head

        while currentnode.next != None and currentnode.data != data:
            currentnode = currentnode.nextnode

        newNode.set_nextnode(currentnode.nextnode)
        currentnode.nextnode = newNode
        self.length += 1

        print("The data provided is not present")

    # method to add a node at a particular position
    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.nextnode != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.nextnode = node
                    node.nextnode = currentnode
                    self.length += 1
                    return

                else:
                    previousnode = currentnode
                    currentnode = currentnode.nextnode

    # method to delete a node in the beginning
    def deleteBeg(self):
        if self.length == 0:
            print("Empty linked list")
        else:
            self.head.next = self.head
            self.length -= 1

    # method to delete a node in the beginning
    def deleteLast(self):
        if self.length == 0:
            print("Empty linked list")
        else:
            tempnode = self.head
            count = self.length
            while count > 1:
                tempnode = tempnode.nextnode

            tempnode.nextnode = None
            self.length -= 1

    # method to delete the last node of the linked list
    def deleteLast_1(self):

        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.nextnode != None:
                previousnode = currentnode
                currentnode = currentnode.next

            previousnode.nextnode = None

            self.length -= 1

    # method to delete a node at a specific position
    def deletenodeAtpos(self, pos):

        if pos > self.length or pos < 0:
            print("Provide a value in the range")

        if self.length == 0:
            print("Empty linked list")

        if pos == 1:
            self.deleteBeg()

        tempnode = self.head
        count = 0
        while count != pos-1 and count < self.length:
            tempnode = tempnode.nextnode
            count = count + 1

        nextnode = tempnode.nextnode
        tempnode.nextnode = nextnode.nextnode
        self.length -= 1

    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print
            "The position does not exist. Please enter a valid position"
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.delete_beg()
            self.length -= 1
        else:
            while currentnode.nextnode != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.nextnode = currentnode.nextnode
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.nextnode

    # method to print the whole list
    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.nextnode

        print(nodeList)

    def getValues(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.nextnode

        return nodeList

    def getfirst(self):
        if self.length == 0:
            print("Linked list is empty!")
            return -1
        else:
            return self.head.get_data()

    # returns the length of the list
    def getLength(self):
        return self.length

    # returns the first element of the list
    def getFirst(self):
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    # returns the last element of the list
    def getLast(self):

        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head

            while currentnode.nextnode != None:
                currentnode = currentnode.nextnode

            return currentnode.data

    # returns node at any position
    def getAtPos(self, pos):
        count = 0
        currentnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.nextnode != None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.nextnode

    # Deleting a single linked list
    # time complexity : O(1)
    def clear(self):
        self.head = None

    # Reverse a linked list
    # do iterations
    #    in each iteration
    #         set the current node pointer to last
    #         update the current node to next node
    def reverseLL(self):
        last = None
        current = self.head

        while current is not None:
            nextnode = current.nextnode
            current.nextnode = last
            last = current
            current = nextnode

        self.head = last

    def reverseRecursive(self):
        self.reverseRecursiveLL(self.head)

    def reverseRecursiveLL(self,node):
        if node != None:
            nextNode = node.nextnode
            if node != self.head:
                node.nextnode = self.head
                self.head = node
            else:
                self.head.nextnode = None
            self.reverseRecursiveLL(nextNode)



# Test the data
# node1 = LinkedListNode(1)
# node2 = LinkedListNode(2)
# node3 = LinkedListNode(3)
# node4 = LinkedListNode(4)
# node5 = LinkedListNode(5)
# ll = LinkedList()
# ll.addNode(node1)
# ll.addNode(node2)
# ll.addNode(node3)
# ll.addNode(node4)
# ll.addNode(node5)
# ll.print_list()
# ll.reverseLL()
# ll.print_list()
# ll.reverseRecursive()
# ll.print_list()