import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode
from LinkedList import LinkedList


def test_creation():
    newlinkedlist = LinkedList()
    assert isinstance(newlinkedlist, LinkedList)

def test_addhead():
    newlinkedlist = LinkedList()
    newnode = LinkedListNode(2)
    newlinkedlist.addNode(newnode)
    assert newlinkedlist.get_length() == 1

def test_checkheadvalue():
    newlinkedlist = LinkedList()
    newnode = LinkedListNode(2)
    newlinkedlist.addNode(newnode)
    assert newlinkedlist.getfirst() == 2

def test_checkemptylist():
    newlinkedlist = LinkedList()
    assert newlinkedlist.getfirst() == -1


def test_deleteatpos():
    newlinkedlist = LinkedList()
    newnode = LinkedListNode(2)
    newlinkedlist.addNode(newnode)
    newnode1 = LinkedListNode(3)
    newlinkedlist.addNode(newnode1)
    newnode2 = LinkedListNode(4)
    newlinkedlist.addNode(newnode2)
    newnode3 = LinkedListNode(5)
    newlinkedlist.addNode(newnode3)
    newlinkedlist.deletenodeAtpos(3)
    assert newlinkedlist.get_length() == 3
