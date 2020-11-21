

class LinkedListNode(object):

    def __init__(self, data):
        self.data = data
        self.nextnode = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_nextnode(self):
        return self.nextnode

    def set_nextnode(self,nextnode):
        self.nextnode = nextnode;

    def has_nextnode(self):
        return self.nextnode != None

    # To compare node objects directly
    def __eq__(self, other):
        if isinstance(self,other.__class__):
            return self.data == other.data
        return False


