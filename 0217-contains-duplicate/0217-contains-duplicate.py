class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memory = {};
        for num in nums:
            if num in memory:
                return True;
            memory[num] = 1;
        return False;