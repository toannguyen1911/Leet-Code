class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        ans = 1;
        nums.sort();
        min_val = nums[0];

        for i in range(1, len(nums)):
            if nums[i] - min_val > k:
                ans += 1;
                min_val = nums[i];
        return ans;