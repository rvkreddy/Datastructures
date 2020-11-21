import sys
sys.path.insert(1, 'C:\\Users\\kondared\\PycharmProjects\\datastructures\\LinkedList\\source')

from LinkedList_detectCycle import LinkedList


def createLinkedListwithCycle():
    linkedlst = LinkedList()
    linkedlst.insertAtBeg(1)
    linkedlst.insertAtBeg(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertBeforeItem(4, 3)
    linkedlst.insertAfterItem(5, 1)
    linkedlst.insertAtEnd(6)
    linkedlst.insertAtEnd(8)
    linkedlst.insertAtEnd(7)

    linkedlst.printList()

    linkedlst.induceCycle(2, 8)
    return linkedlst


def test_detectCycle():
    linkedlst = createLinkedListwithCycle()
    assert linkedlst.detectCycle() == True

def test_detectStartpoint():
    linkedlst = createLinkedListwithCycle()
    assert linkedlst.detectCycleStart() == 5