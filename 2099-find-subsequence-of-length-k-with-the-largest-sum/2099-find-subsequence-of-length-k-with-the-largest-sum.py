class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Sort by value descending
        sorted_nums = list(enumerate(nums));
        sorted_nums.sort(reverse = True, key = lambda x: x[1]);

        # Get top k values
        top_k_nums = sorted_nums[:k];
        top_k_nums.sort(key = lambda x: x[0]);

        return [num for index, num in top_k_nums];