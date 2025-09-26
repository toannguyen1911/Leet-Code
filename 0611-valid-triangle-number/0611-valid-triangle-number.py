class Solution:
    def triangleNumber(self, nums):
        nums.sort();
        n, ans = len(nums), 0;
        
        for k in range(2, n):
            i, j = 0, k - 1;
            while i < j:
                if nums[i] + nums[j] <= nums[k]:
                    i += 1;
                    continue;
                ans += j - i;
                j -= 1;

        return ans;