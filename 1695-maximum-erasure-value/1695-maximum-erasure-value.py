class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set();  # To track unique elements in current window
        left = 0;
        cur_score = 0;
        ans = 0;

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left]);
                cur_score -= nums[left];
                left += 1;

            seen.add(nums[right]);
            cur_score += nums[right];
            ans = max(ans, cur_score);

        return ans;
