
class RandomizedSet:

    def __init__(self):
        self.lst = []

    def insert(self, val: int) -> bool:
        for i in self.lst:
            if val == i:
                return False
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        for i in range (len(self.lst)):
            if val == self.lst[i]:
                del self.lst[i]
                return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()