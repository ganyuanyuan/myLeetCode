import heapq
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

#############################################################################
#
#      use:  a double-linked-List --> store stack
#            a max-heap --> store max --> (-val, -index, node)
#                                              |
#                                        python heapq is min heap
#
##############################################################################


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.head = self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        node = Node(x)

        prev = self.tail.prev
        prev.next, node.prev = node, prev
        node.next, self.tail.prev = self.tail, node

        self.count  += 1

        heapq.heappush(self.heap, (-x, -self.count, node))


    def pop(self):
        """
        :rtype: int
        """
        node = self.tail.prev
        if not node.prev:
            return
        prev = node.prev
        prev.next, self.tail.prev = self.tail, prev
        node.next, node.prev = None, None
        return node.val




    def top(self):
        """
        :rtype: int
        """
        return self.tail.prev.val



    def peekMax(self):
        """
        :rtype: int
        """
        _, _, node = self.heap[0]
        while node.next == None and node.prev == None:
            heapq.heappop(self.heap)
            _, _, node = self.heap[0]

        return node.val


    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        _, _ , node = heapq.heappop(self.heap)
        node.prev.next, node.next.prev = node.next, node.prev
        node.next , node.prev = None, None
        return node.val
