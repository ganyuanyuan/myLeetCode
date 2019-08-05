class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.hash_prev = {}


    def push_back(self, node):
        self.tail.next = node
        self.hash_prev[node.key] = self.tail
        self.tail = node

    def pop_top(self):
        head = self.dummy.next
        del self.hash_prev[head.key]
        self.dummy.next = head.next
        self.hash_prev[head.next.key] = self.dummy

#############################################################################
#
#    KICK: prev -> NODE -> next_node ... self.tail -> None
#          prev -> next_node ... self.tail -> NODE -> None
#                                          self.tail
#
##############################################################################

    def kick(self, prev):
        if prev.next == self.tail:
            return
        node = prev.next
        prev.next = node.next
        self.hash_prev[node.next.key] = prev
        node.next = None
        self.push_back(node)


    def get(self, key: int) -> int:
        if key not in self.hash_prev:
            return -1
        self.kick(self.hash_prev[key])
        return self.hash_prev[key].next.value


    def put(self, key: int, value: int) -> None:
        if key in self.hash_prev:
            self.kick(self.hash_prev[key])
            self.hash_prev[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash_prev) > self.capacity:
                self.pop_top()


#####################################################################################
#
#      hash_map -->  store { key: LinkedNode_KEY,  value: the PREV_NODE in the linked_list}
#         +
#      single_linked_list  -->  self.dummy -> node -> node ... node -> node -> None
#                                                                        |
#                                                                      self.tail
#      3 helping methods: PUSH_BACK, POP_TOP , KICK
#
#####################################################################################
