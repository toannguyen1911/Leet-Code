from collections import defaultdict
from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.numbers = defaultdict(SortedSet);
        self.index_to_number = {};

    def change(self, index: int, number: int) -> None:
        # old index, just remove
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.numbers[old_number].remove(index)
            if len(self.numbers[old_number]) == 0:
                del self.numbers[old_number]
        # add new index
        self.index_to_number[index] = number
        self.numbers[number].add(index)

    def find(self, number: int) -> int:
        if number in self.numbers:
            return self.numbers[number][0]
        return -1 


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)