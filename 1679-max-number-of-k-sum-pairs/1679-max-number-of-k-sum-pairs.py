class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0;
        l, r = 0, len(nums) -1;
        nums.sort();

        while (l < r):
            s = nums[l] + nums[r];

            if (s == k):
                res += 1;
                l += 1;
                r -= 1;
            elif s > k:
                r -= 1;
            else:
                l += 1;

        return res;