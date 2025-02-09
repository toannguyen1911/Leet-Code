class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good_pairs = 0;
        freq = {};

        for  index, num in enumerate(nums):
            key = num - index;
            good_pairs += freq.get(key, 0);
            freq[key] = freq.get(key, 0) + 1;
        n = len(nums)
        total_pairs = (n * (n -1)) // 2; 
        return total_pairs - good_pairs;
        