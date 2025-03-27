class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l_count = 0;
        dominant, r_count = max(Counter(nums).items(), key=lambda x: x[1]);
        for i, x in enumerate(nums):
            l_count += x == dominant;
            r_count -= x == dominant;
            if l_count > (i + 1) // 2 and r_count > (len(nums) - (i + 1)) // 2:
                return i;
        return -1;