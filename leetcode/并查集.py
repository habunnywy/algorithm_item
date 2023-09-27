class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0

    def merge(self, other):
        self_parent = self.find()
        other_parent = other.find()
        if self_parent == other_parent:
            return
        if self_parent.rank < other_parent.rank:
            self_parent.parent = other_parent
        elif self_parent.rank > other_parent.rank:
            other_parent.parent = self_parent
        else:
            other_parent.parent = self_parent
            self_parent.rank += 1