class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos_count = neg_count = 0;

        for num in nums:
            if num < 0:
                neg_count += 1;
            elif num > 0:
                pos_count += 1;
        
        return max(neg_count, pos_count);