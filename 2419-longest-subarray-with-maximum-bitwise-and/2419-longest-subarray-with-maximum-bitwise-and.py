class Solution:
    def longestSubarray(self, nums):
        maxi = max(nums);
        ans = 0;
        length = 0;

        for num in nums:
            if num == maxi:
                length += 1;
                ans = max(ans, length);
            else:
                length = 0;

        return ans;