import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

# Import Modules
from LinkedListNode import LinkedListNode
import pytest

# Message to print
@pytest.fixture(scope="session", autouse=True)
def setupModule():
    print("\n Starting test_linkedlistnode testcases....")

@pytest.fixture(params=[5])
def createLinkedListNode(request):
    data = request.param
    return LinkedListNode(data)


def createnodeObj(data):
    return LinkedListNode(data)


def test_nodetype():
    node = createnodeObj(10)
    assert isinstance(node, LinkedListNode)

def test_getdata(createLinkedListNode):
    node = createLinkedListNode
    data = node.get_data()
    assert data == 5

def test_nextNode():
    node = createnodeObj(5)
    nextnode = createnodeObj(6)
    node.set_nextnode(nextnode)
    assert node.get_nextnode() == nextnode