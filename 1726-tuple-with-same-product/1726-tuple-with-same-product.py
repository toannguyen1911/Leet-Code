import math 
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0;
        memory = {};
        for i in range (len(nums) -1):
            for j in range(i +1, len(nums)):
                key = nums[i] * nums[j];
                if key in memory:
                    memory[key] += 1;
                    continue;
                memory[key] = 1;

        # check valid key
        for num in memory.values():
            if num >= 2:
                ans += math.comb(num, 2) * 8
        # print(memory)
        return ans;