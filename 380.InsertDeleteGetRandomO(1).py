import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.index = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index:
            return False
        self.arr.append(val)
        self.index[val] = len(self.arr)-1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index:
            return False
        tail = self.arr.pop()
        index = self.index[val]
        del self.index[val]
        if tail != val:
            self.index[tail] = index
            self.arr[index] = tail
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr)-1)]
