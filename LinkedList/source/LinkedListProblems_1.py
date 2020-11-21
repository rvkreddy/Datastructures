import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode
from LinkedList import LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

# start 2 pointers at different speeds
# Note: move fastptr first, compare, move fastptr again,compare and increment slowptr
def detectCycleinLL(headNode):
    slowptr = headNode
    fastptr = headNode

    while slowptr and fastptr:
        fastptr = fastptr.next
        if slowptr == fastptr:
            return True

        if fastptr == None:
            return False

        fastptr = fastptr.next
        if slowptr == fastptr:
            return True

        slowptr = slowptr.next

# Find the nth node from end
# Take 2 pointers, find the length of linked list, move the one pointer to len-n
# move both together
def findnthNode(headNode,length, n):

    if n > length or n < 0:
        print(" value out of range")

    tempNode1 = headNode
    tempNode2 = headNode

    count = 0
    while count < (length - n):
        count = count + 1
        tempNode2 = tempNode2.next

    while count < length:
        if tempNode1 != None:
            tempNode1 = tempNode1.next

        if tempNode2 != None:
            tempNode2 = tempNode2.next

        count = count + 1

    print("The value at nth node is ", tempNode1.get_data())
    return tempNode1

# Take 2 pointers, faster one reaches the end, slower one will be at middle
# Note: odd and even can be different, do comparision after each next update of fast
def findMiddleNode(headNode):
    fastPtr = headNode
    slowPtr = headNode

    while (fastPtr != None):
        fastPtr = fastPtr.next
        if (fastPtr == None):
            return slowPtr

        fastPtr = fastPtr.next
        slowPtr = slowPtr.next
    return slowPtr


# Find the intersection point, move the first node to head and move both pointers one at a time
# Note:
def getIntersectionNode(head1, head2):

    # get the length of first list
    length1 = getListLength(head1)

    length2 = getListLength(head2)

    diff = length1 - length2

    tempNode1 = head1
    tempNode2 = head2

    count = 0
    if diff > 0:

        while count < diff:
            tempNode1 = tempNode1.next
    else:
        while count < diff:
            tempNode2 = tempNode2.next

    while (tempNode1 != None) and (tempNode2 != None):
        if tempNode1  == tempNode2:
            return tempNode2

        tempNode1 = tempNode1.next
        tempNode2 = tempNode2.next

    return None



def getListLength(head2):

    # get the length of second list
    temphead2 = head2
    list2_length = 0
    while temphead2 is not None:
        list2_length += 1
        temphead2 = temphead2.next
    return list2_length


def printLinkedListfromEnd(headNode):

    tempNode = headNode
    # go till the next pointer is none
    if tempNode.next != None:
        printLinkedListfromEnd(tempNode.next)
    print(tempNode.get_data())

# Create a new node
# compare the 2 list nodes of 2 linked lists
# set the next pointer of the new node appropriately
def mergeTwoSortedLists(list1, list2):
    temp = LinkedListNode(0)
    pointer = temp
    count = 0
    while list1 is not None and list2 is not None:
        print("count:",count)
        count += 1
        if list1.get_data() < list2.get_data():
            pointer.set_nextnode(list1)
            list1 = list1.next
        else:
            pointer.set_nextnode(list2)
            list2 = list2.next
        pointer = pointer.get_nextnode()
    if list1 == None:
        pointer.set_nextnode(list2)
    else:
        pointer.set_nextnode(list1)
    return temp.nextnode





node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node5 = LinkedListNode(5)
node6 = LinkedListNode(6)
node7 = LinkedListNode(7)
node8 = LinkedListNode(8)

LL1 = LinkedList()
LL2 = LinkedList()


LL1.addNode(node1)
LL2.addNode(node2)
LL1.addNode(node3)
LL2.addNode(node4)
LL1.addNode(node5)
LL2.addNode(node6)
LL1.addNode(node7)
LL2.addNode(node8)
print("First Linked list:")
LL1.print_list()
LL2.print_list()

# print(" --- Test start")
# testnode = LL1.get_head()
# while testnode is not None:
#     print(testnode.get_data())
#     testnode = testnode.next
# print(" --- Test end")
#
# print(" --- Test start - 2")
# testnode2 = LL2.get_head()
# while testnode2 is not None:
#     print(testnode2.get_data())
#     testnode2 = testnode2.next
# print(" --- Test end - 2")

mergedheadnode = mergeTwoSortedLists(LL1.get_head(), LL2.get_head())

while mergedheadnode is not None:
    print(mergedheadnode.get_data())
    mergedheadnode = mergedheadnode.nextnode


# Create Linkedlist
# Test the data
# node1 = LinkedListNode(1)
# node2 = LinkedListNode(2)
# node3 = LinkedListNode(3)
# node4 = LinkedListNode(4)
# node5 = LinkedListNode(5)
# node6 = LinkedListNode(6)
# node7 = LinkedListNode(7)
# node8 = LinkedListNode(8)
# LL1 = LinkedList()
# LL1.addNode(node1)
# LL1.addNode(node3)
# LL1.addNode(node4)
# LL1.addNode(node5)
# LL1.addNode(node6)
#
# printLinkedListfromEnd(LL1.head)

# cycleLL = LinkedList()
# cycleLL.addNode(node1)
# cycleLL.addNode(node2)
# cycleLL.addNode(node3)
# cycleLL.addNode(node4)
# cycleLL.addNode(node5)
# cycleLL.addNode(node6)
# node6.set_nextnode(node3)
# print("The nodes in cycle Linked list")
# cycleLL.print_list()
# print(detectCycleinLL(cycleLL.head))



# ll = LinkedList()
# ll.addNode(node1)
# ll.addNode(node2)
# ll.addNode(node3)
# ll.addNode(node4)
# ll.addNode(node5)
# ll.addNode(node6)
# ll.addNode(node7)
# ll.addNode(node8)
# #ll.print_list()
# headNode = ll.get_head()
# #findMiddleNode(headNode)
# findnthNode(headNode,7,3)



