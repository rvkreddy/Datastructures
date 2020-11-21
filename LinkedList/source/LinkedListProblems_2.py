import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode
from LinkedList import LinkedList

# Testcases
def test_LinkedListLength(LinkedList):
    assert findLinkedListLen(LinkedList) == 7

def test_findMiddleNode(LinkedList):
    assert findMiddleNode(LinkedList).get_data() == 4

def test_isPalindrome(LL1_node, LL2_node):
    flag = isPalindrome(LL1_node,LL2_node)
    assert flag == True



def isPalindrome(LL1_node, LL2_node):

    if LL1_node is None or LL2_node is None:
        return False

    while LL1_node is not None and LL2_node is not None:
        if LL1_node.get_data() != LL2_node.get_data():
            return False

        LL1_node = LL1_node.get_nextnode()
        LL2_node = LL2_node.get_nextnode()

    return True




def reverseandclone(headnode):
    temp = headnode
    if temp is None:
        return None

    head = None
    while temp is not None:
        newnode = LinkedListNode(temp.get_data())
        newnode.set_nextnode(head)
        head = newnode
        temp = temp.get_nextnode()
    return head


def findMiddleNode(LinkedList):
    headnode = LinkedList.get_head()
    if headnode == None:
        return None

    slowptr = headnode
    fastptr = headnode

    while fastptr.get_nextnode() is not None:
        slowptr = slowptr.get_nextnode()
        fastptr = fastptr.get_nextnode()
        if fastptr is not None:
            fastptr = fastptr.get_nextnode()

    return slowptr


def findLinkedListLen(LinkedList):
    headnode = LinkedList.get_head()
    if headnode == None:
        return 0

    count = 0
    while headnode != None:
        headnode = headnode.get_nextnode()
        count += 1

    return count


def isPalindrome_recursive(LL):
    length = findLinkedListLen(LL)
    result = isPalindrome_r(LL.get_head(), length)
    return result.flag



def isPalindrome_r(headnode, length):

    if length == 1:
        return Result(headnode.nextnode,True)

    if length <= 0 or headnode == None:
        return Result(headnode,True)


    result = isPalindrome_r(headnode.nextnode, length-2)
    if result.flag == False or result.node == None:
        return result

    result.flag = (headnode.get_data() == result.node.get_data())
    result.node = result.node.nextnode

    return result


class Result:

    def __init__(self, node, flag):
        self.node = node
        self.flag = flag



# find root nth node of a linked list
def findrootnthnode(head):

    i = j = 1
    rootnthnode = None
    while head != None:
        if i == j * j:
            if rootnthnode == None:
                rootnthnode = head
            else:
                rootnthnode = rootnthnode.nextnode
            j += 1
        i += 1
        head = head.nextnode
    return rootnthnode.get_data()



# delete duplicate elements from a linked list
#note:2 while
def deleteduplicates(head):
    temp = head
    if head == None:
        print("List is empty")

    while temp is not None and temp.get_nextnode() is not None:
        while temp.get_data() == temp.get_nextnode().get_data():
            tempnext = temp.nextnode
            temp.set_nextnode(tempnext.nextnode)
        temp = temp.get_nextnode()
    return head


# Create a Linkedlist
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node21 = LinkedListNode(2)
node22 = LinkedListNode(2)
node3 = LinkedListNode(3)
node4 = LinkedListNode(4)
node5 = LinkedListNode(3)
node6 = LinkedListNode(2)
node7 = LinkedListNode(1)
node8 = LinkedListNode(8)

LL1 = LinkedList()
LL1.addNode(node1)
LL1.addNode(node2)
LL1.addNode(node21)
LL1.addNode(node22)
LL1.addNode(node3)
LL1.addNode(node4)
# LL1.addNode(node5)
# LL1.addNode(node6)
# LL1.addNode(node7)
# LL1.addNode(node8)
LL1.print_list()
# test_LinkedListLength(LL1)
# test_findMiddleNode(LL1)


# test reverse and clone
LL2_headnode = reverseandclone(LL1.get_head())
# while LL2_headnode != None:
#     print(LL2_headnode.get_data())
#     LL2_headnode = LL2_headnode.get_nextnode()

print("First linked list")
headnode_ll1 = LL1.get_head()
# while headnode_ll1 != None:
#     print(headnode_ll1.get_data())
#     headnode_ll1 = headnode_ll1.get_nextnode()

print(isPalindrome(headnode_ll1,LL2_headnode))
#test_comparereverselist(LL1.get_head(),LL2_headnode )

print("THe result of recursive palindrome:", isPalindrome_recursive(LL1))

print(findrootnthnode(headnode_ll1))

LL1_headnode = LL1.get_head()
tmpnode = deleteduplicates(LL1_headnode)
print("With out duplicates")
while tmpnode != None:
    print(tmpnode.get_data())
    tmpnode = tmpnode.get_nextnode()