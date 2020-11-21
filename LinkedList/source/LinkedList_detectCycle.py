
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

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insertAtBeg(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def insertAtEnd(self, item):
        current = self.head

        while current.get_next() != None:
            current = current.get_next()

        node = Node(item)
        current.set_next(node)

    def insertBeforeItem(self, inItem, item):
        current = self.head
        previous = None
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
                stop = True
            else:
                previous = current
                current = current.get_next()

        node = Node(inItem)
        previous.set_next(node)
        node.set_next(current)

    def insertAfterItem(self, inItem, item):
        current = self.head

        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
                stop = True
            else:
                #                previous = current
                current = current.get_next()
        successor = current.get_next()
        node = Node(inItem)
        current.set_next(node)
        node.set_next(successor)

    def printList(self):
        current = self.head

        while current != None:
            print(current.get_data())
            current = current.get_next()

    def remove(self, item):
        found = False
        current = self.head
        previous = None

        while current.get_next() != None and not found:
            if current.get_data() == item:
                print(current.get_data())
                print(previous.get_data())
                found = True
                previous.set_next(current.next)
            else:
                previous = current
                current = current.get_next()

    def induceCycle(self, end, start):
        current = self.head
        stop = False
        endnodePointer = None
        count = 0
        while current != None and not stop:
            count += 1
            if count == end:
                endnodePointer = current.get_next()

            else:
                if count == start:
                    stop = True
                else:
                    current = current.get_next()

        current.set_next(endnodePointer)

    def detectCycle(self):
        hare = self.head
        tortoise = self.head

        while (hare and tortoise):
            hare = hare.get_next()
            if (hare == tortoise):
                return True

            if hare == None:
                return False

            hare = hare.get_next()
            if (hare == tortoise):
                return True

            tortoise = tortoise.get_next()

    def detectCycleStart(self):
        if None == self.head or None == self.head.next:
            return None

        slow = self.head.next
        fast = slow.next
        while slow != fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return None
        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.get_data()

