import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode
from LinkedList import LinkedList
from LinkedListProblems_1 import findMiddleNode,findnthNode,getIntersectionNode


def createLinkedlist():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)
    node4 = LinkedListNode(4)
    node5 = LinkedListNode(5)
    node6 = LinkedListNode(6)
    node7 = LinkedListNode(7)
    node8 = LinkedListNode(8)
    ll = LinkedList()
    ll.addNode(node1)
    ll.addNode(node2)
    ll.addNode(node3)
    ll.addNode(node4)
    ll.addNode(node5)
    ll.addNode(node6)
    ll.addNode(node7)
    ll.addNode(node8)
    return ll


def test_findMiddlenode():
    ll = createLinkedlist()
    headNode = ll.get_head()
    node = findMiddleNode(headNode)
    assert node.get_data() == 5

def test_findnthNode():
    ll = createLinkedlist()
    headNode = ll.get_head()
    length = ll.get_length()
    node = findnthNode(headNode,length,3)
    assert node.get_data() == 4

def test_reverseLL():
    ll = createLinkedlist()
    beforereverse = ll.getValues()
    ll.reverseLL()
    afterreverse = ll.getValues()
    reversed_list = afterreverse[::-1]
    assert beforereverse == reversed_list

def test_intersectingNodes():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)
    node4 = LinkedListNode(4)
    node5 = LinkedListNode(5)
    node6 = LinkedListNode(6)
    node7 = LinkedListNode(7)
    node8 = LinkedListNode(8)
    LL1 = LinkedList()
    LL1.addNode(node1)
    LL1.addNode(node3)
    LL1.addNode(node4)
    LL1.addNode(node5)
    LL1.addNode(node6)

    LL2 = LinkedList()
    LL2.addNode(node2)
    LL2.addNode(node3)
    LL2.addNode(node4)
    LL2.addNode(node5)
    LL2.addNode(node6)

    intersectNode = getIntersectionNode(LL1.head, LL2.head)
    print(intersectNode.get_data())