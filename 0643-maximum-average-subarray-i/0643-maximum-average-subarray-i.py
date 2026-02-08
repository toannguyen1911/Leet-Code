class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums);
        total = sum(nums[:k]);
        res = total / k;

        for i in range(k, n):
            total += (nums[i] -nums[i -k]);
            res = max(res, total / k);

        return res;