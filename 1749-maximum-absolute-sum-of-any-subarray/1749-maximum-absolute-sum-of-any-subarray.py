class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Kadane’s algorithm 
        # for each nums: 
        # choice 1: sub array + current num; 
        # choic2 2: start new sub array
        # maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) 
        max_ending = nums[0];
        min_ending = nums[0];
        max_so_far = nums[0];
        min_so_far = nums[0];

        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i]);
            min_ending = min(nums[i], min_ending + nums[i]);
            max_so_far = max(max_so_far, max_ending);
            min_so_far = min(min_so_far, min_ending);

        return max(abs(max_so_far), abs(min_so_far));